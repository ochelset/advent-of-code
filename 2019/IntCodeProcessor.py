OP_CODE_ADD = 1
OP_CODE_MULTIPLY = 2
OP_CODE_INPUT = 3
OP_CODE_OUTPUT = 4
OP_CODE_JUMP_IF_TRUE = 5
OP_CODE_JUMP_IF_FALSE = 6
OP_CODE_LESS_THAN = 7
OP_CODE_EQUALS = 8
OP_CODE_ADJUST_RELATIVE_BASE = 9
OP_CODE_STOP = 99

PARAMETER_MODE_POSITION = 0
PARAMETER_MODE_IMMEDIATE = 1
PARAMETER_MODE_RELATIVE = 2

#
#

class IntCodeProcessor:

	relativeBase = 0
	inputValue = 0
	inputValues = []
	outputValue = None
	silent = True
	instructionPointer = 0
	opcode = 0

	@property
	def isFinished(self) -> bool:
		return self.memory[self.instructionPointer] == OP_CODE_STOP

	def __init__(self, inputs):
		if type(inputs) == type(''):
			inputs = list(map(int, inputs.strip().split(',')))
		self.inputs = inputs[:]
		self.memory = inputs[:]
		self.reset()

	def __repr__(self):
		return "<IntCodeProcessor X2 | Silent: %s>" % (self.silent)

	def reset(self):
		if len(self.memory) == len(self.inputs):
			self.memory.extend([0] * 3500000)
		self.resetMemory()
		self.instructionPointer = 0
		self.relativeBase = 0
		self.inputValue = 0
		self.inputValues = []
		self.outputValue = None

	def resetMemory(self):
		for i, v in enumerate(self.inputs):
			self.memory[i] = v

	def split(self, number) -> [int]:
		result = [number % 10]
		for n in range(2):
			number = int(number / 10)
			result.append(number % 10)
		return result

	def getInstruction(self):
		code = self.memory[self.instructionPointer]
		self.opcode = code % 100
		parameters = self.split(code // 100)
		while len(parameters) and parameters[-1] == 0:
			parameters.pop()
		return (self.opcode, parameters)

	def writeValue(self, value, position, mode=PARAMETER_MODE_POSITION):
		pointer = self.memory[position]
		if mode == PARAMETER_MODE_RELATIVE:
			position = self.relativeBase + pointer
		elif mode == PARAMETER_MODE_POSITION:
			position = pointer
		self.memory[position] = value

	def getValue(self, parameters=None):
		if parameters is None:
			parameters = []
		position = self.instructionPointer + 1
		pointer = self.memory[position]
		if len(parameters):
			if parameters[0] == PARAMETER_MODE_RELATIVE:
				pointer = self.relativeBase + pointer
			
			elif parameters[0] == PARAMETER_MODE_IMMEDIATE:
				pointer = position

		return self.memory[pointer]

	def get_value_pair(self, parameters=None):
		if parameters is None:
			parameters = []
		position = self.instructionPointer + 2
		pointer = self.memory[position]
		if len(parameters) > 1:
			if parameters[1] == PARAMETER_MODE_RELATIVE:
				pointer = self.relativeBase + pointer
			elif parameters[1] == PARAMETER_MODE_IMMEDIATE:
				pointer = position

		return (self.getValue(parameters), self.memory[pointer])

	def step_forward(self, length):
		self.instructionPointer += length

	def execute(self, noun=None, verb=None, step=False):
		self.isRunning = True
		if noun != None and verb != None:
			self.memory[1] = noun
			self.memory[2] = verb

		while self.isRunning:
			self.opcode, parameters = self.getInstruction()

			if self.opcode == OP_CODE_STOP:
				break

			value1, value2 = self.get_value_pair(parameters)
			mode = parameters[2] if len(parameters) == 3 else PARAMETER_MODE_POSITION
			output = None
			outputPosition = self.instructionPointer + 3
			instructionLength = 4

			if self.opcode == OP_CODE_ADD:
				output = value1 + value2

			elif self.opcode == OP_CODE_MULTIPLY:
				output = value1 * value2

			elif self.opcode == OP_CODE_INPUT:
				#print("INPUT", self.inputValues)
				mode = parameters[0] if len(parameters) == 1 else PARAMETER_MODE_POSITION
				self.inputValue = self.inputValues.pop(0) if len(self.inputValues) else int(input("> Please enter an input value: "))
				output = self.inputValue
				outputPosition = self.instructionPointer + 1
				instructionLength = 2

			elif self.opcode == OP_CODE_OUTPUT:
				mode = parameters[0] if len(parameters) == 1 else PARAMETER_MODE_POSITION
				self.outputValue = value1
				if not self.silent:
					print("> Output:", self.outputValue)
				self.writeValue(self.outputValue, self.instructionPointer + 1, mode)
				self.instructionPointer += 2
				return self.outputValue

			elif self.opcode == OP_CODE_JUMP_IF_TRUE:
				self.instructionPointer = value2 if value1 != 0 else self.instructionPointer + 3
				continue

			elif self.opcode == OP_CODE_JUMP_IF_FALSE:
				self.instructionPointer = value2 if value1 == 0 else self.instructionPointer + 3
				continue

			elif self.opcode == OP_CODE_LESS_THAN:
				output = 1 if value1 < value2 else 0

			elif self.opcode == OP_CODE_EQUALS:
				output = 1 if value1 == value2 else 0

			elif self.opcode == OP_CODE_ADJUST_RELATIVE_BASE:
				self.relativeBase = self.relativeBase + value1
				instructionLength = 2

			else:
				raise Exception("UNKNOWN opcode %s @ %s" % (self.opcode, self.instructionPointer), self.memory[self.instructionPointer - 1:self.instructionPointer + 30])

			if output != None:
				self.writeValue(output, outputPosition, mode)

			self.instructionPointer += instructionLength

			if step:
				self.isRunning = False