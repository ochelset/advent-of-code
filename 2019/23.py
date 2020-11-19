"""
--- Day 23: Category Six ---
The droids have finished repairing as much of the ship as they can.
Their report indicates that this was a Category 6 disaster - not because it was that bad, but because it destroyed the
stockpile of Category 6 network cables as well as most of the ship's network infrastructure.

You'll need to rebuild the network from scratch.

The computers on the network are standard Intcode computers that communicate by sending packets to each other.
There are 50 of them in total, each running a copy of the same Network Interface Controller (NIC) software (your puzzle input).
The computers have network addresses 0 through 49; when each computer boots up, it will request its network address via a single input instruction.
Be sure to give each computer a unique network address.

Once a computer has received its network address, it will begin doing work and communicating over the network by sending and receiving packets.
All packets contain two values named X and Y. Packets sent to a computer are queued by the recipient and read in the order they are received.

To send a packet to another computer, the NIC will use three output instructions that provide the destination address
of the packet followed by its X and Y values.
For example, three output instructions that provide the values 10, 20, 30 would send a packet with X=20 and Y=30 to the computer with address 10.

To receive a packet from another computer, the NIC will use an input instruction. If the incoming packet queue is empty,
provide -1. Otherwise, provide the X value of the next packet; the computer will then use a second input instruction to
receive the Y value for the same packet. Once both values of the packet are read in this way, the packet is removed from the queue.

Note that these input and output instructions never block. Specifically, output instructions do not wait for the sent
packet to be received - the computer might send multiple packets before receiving any. Similarly,
input instructions do not wait for a packet to arrive - if no packet is waiting, input instructions should receive -1.

Boot up all 50 computers and attach them to your network. What is the Y value of the first packet sent to address 255?
ANSWER:
"""

import multiprocessing as mp
import threading
from IntCodeProcessor import IntCodeProcessor

class Computer:

    def __init__(self, data):
        self.controller = IntCodeProcessor(data)
        #self.controller.silent = False

    def boot(self, address):
        self.address = address
        self.controller.inputValues = [address]
        print("Booting up computer on address", address)

    def run(self):
        print("RUN %d:" % self.address, packetQue[self.address])

        inPacket = None
        outPacket = []
        while not self.controller.isFinished:
            if len(self.controller.inputValues) == 0:
                if len(packetQue[self.address]) > 0:
                    if inPacket != None:
                        print("INPACK", inPacket)
                        self.controller.inputValues.extend(inPacket)
                        inPacket = None

            if len(self.controller.inputValues) == 0 or not self.controller.inputValues[-1] == -1:
                print("EMRGNCY -1")
                self.controller.inputValues.append(-1)

            #self.controller.inputValues = [self.packetQue.pop(0)]

            outPacket.append(self.controller.execute())
            if len(outPacket) == 3:
                print(self.address, "OUTPACK", outPacket)
                self.send(outPacket[0], outPacket[1:3])
                outPacket = []

            #input("%d >:" % self.address)
            break

    def send(self, recipient, packet=[]):
        print(self.address, "=> Send packet to", recipient, packet)
        packetQue[recipient].append(packet)
        print(recipient, "pq", packetQue[recipient])
        #network[recipient].run()

#
#

MAX = 10

data = open("data/23.data").read()
network = { "packets": {} }
packetQue = network["packets"]
threads = []

def setupNetwork():
    print("Setting up network")
    pool = mp.Pool(mp.cpu_count())
    #print("CPUs", mp.cpu_count())

    for address in range(MAX):
        packetQue[address] = []
        network[address] = Computer(data)
        network[address].boot(address)
        t = threading.Thread(target=network[address].run)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


setupNetwork()
