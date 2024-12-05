reports = []

with open("input_02.txt") as input_file:
    reports = [line.rstrip() for line in input_file]

num_safe = 0

for report in reports:
    levels = [int(level) for level in report.split(" ")]
    pairs = zip(levels[:-1], levels[1:])
    differences = [a - b for a, b in pairs]
    if all(d in [1, 2, 3] for d in differences) or all(
        d in [-1, -2, -3] for d in differences
    ):
        num_safe += 1

print(num_safe)

num_safe_2 = 0

for report in reports:
    levels = [int(level) for level in report.split(" ")]
    pairs = zip(levels[:-1], levels[1:])
    differences = [a - b for a, b in pairs]

print(num_safe_2)  # 340 too high
