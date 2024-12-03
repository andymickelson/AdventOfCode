import sys

safeNumber = 0

def is_report_ascending_or_descending(report):
    return all(x < y for x,y in zip(report, report[1:])) or all(x > y for x,y in zip(report, report[1:]))

def are_adjacent_within_limits(report):
    return all(abs(int(x) - int(y)) <= 3 for x,y in zip(report, report[1:]))

def is_report_safe(report):
    return is_report_ascending_or_descending(report) and are_adjacent_within_limits(report)

with open(sys.argv[1]) as file:
    while line := file.readline():
        report = [int(i) for i in line.split()]
        if is_report_safe(report):
            safeNumber += 1

print(safeNumber)
