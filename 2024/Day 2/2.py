from itertools import combinations

data = open("input.data").read().strip().splitlines()
datax = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip().splitlines()


def check_report(report: [int]) -> bool:
    prev_level = report[0]
    increasing = report[1] > report[0]
    for level in report[1:]:
        if (increasing and level < prev_level) or (not increasing and level > prev_level):
            return False

        diff = abs(level - prev_level)
        if diff < 1 or diff > 3:
            return False

        prev_level = level
    return True


safe_reports = []
unsafe_reports = []
for report in data:
    report = [int(x) for x in report.split(" ")]
    if check_report(report):
        safe_reports.append(report)
    else:
        unsafe_reports.append(report)

print("Part 1", len(safe_reports))

for report in unsafe_reports:
    length = len(report) - 1
    safe = False
    for test_report in combinations(report, length):
        if check_report(test_report):
            safe = True
            break

    if safe:
        safe_reports.append(report)

print("Part 2:", len(safe_reports))
