data = open("input.data").read().strip().splitlines()
data = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
""".strip().splitlines()


class Robot:
    type: str
    cost: {}

    def __init__(self, type, cost=None):
        self.type = type
        self.cost = {}

        if cost is not None:
            for cost in cost.strip().split(" and "):
                price, resource = cost.split(" ")
                self.cost[resource] = int(price)

    def __repr__(self):
        return "<Robot %s>" % self.type

    def collect(self):
        return (self.type, 1)


blueprints = {}
geodes_opened = 0

for line in data:
    line = line[9:].split(":")
    id = int(line[0])
    robots = line[1].replace("Each", "").split(". ")
    blueprints[id] = {"robots": []}
    for robot in robots:
        details = robot.strip().split(" robot costs")
        robot = Robot(details[0], details[1])
        blueprints[id]["robots"].append(robot)

print(blueprints)


def factory(blueprint):
    r2d2 = Robot("ore")
    minutes = 0
    robots = {"ore": [r2d2]}
    resources = {}

    """
    Blueprint 1: 
        Each ore robot costs 4 ore. 
        Each clay robot costs 2 ore. 
        Each obsidian robot costs 3 ore and 14 clay. 
        Each geode robot costs 2 ore and 7 obsidian.
    """

    while minutes < 24:
        minutes += 1
        print("== Minute %s ==" % minutes)

        new_robots = []
        for bp in blueprint["robots"]:
            # print("Spend", bp.cost)
            can_build = True
            build_cost = {}
            for bp_resource in bp.cost.keys():
                # print(bp_resource, bp.cost[bp_resource])
                if bp_resource not in resources or resources[bp_resource] < bp.cost[bp_resource]:
                    can_build = False
                build_cost[bp_resource] = bp.cost[bp_resource]

            if can_build:
                print("Spend", build_cost, "to start building", bp)
                robot = Robot(bp.type)
                robot.cost = bp.cost
                for bc in build_cost.keys():
                    resources[bc] -= build_cost[bc]
                # print(robot.type, robot.cost)
                # print("R", resources)
                # input()
                new_robots.append(robot)

        for robot_type in robots.keys():
            collected_now = 0
            for robot in robots[robot_type]:
                collected = robot.collect()
                if collected[0] not in resources:
                    resources[collected[0]] = 0
                collected_now += collected[1]
                resources[collected[0]] += collected[1]
            print(len(robots[robot_type]), "%s-collecting robot collects" % robot_type, collected_now,
                  "%s;" % robot_type, "you now have %s %s." % (resources[robot_type], robot_type))

        if new_robots:
            for robot in new_robots:
                if robot.type not in robots:
                    robots[robot.type] = []
                robots[robot.type].append(robot)

            print("The new robot(s) is ready.")
            print()
            print("------>", robots)
        input()


factory(blueprints[1])
