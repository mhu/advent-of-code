import re


def compute_instruction(instruction: str) -> int:
    matches = re.search(r"mul\((\d+),(\d+)", instruction)
    num1 = int(instruction[matches.start(1) : matches.end(1)])
    num2 = int(instruction[matches.start(2) : matches.end(2)])
    return num1 * num2


with open("input_03.txt") as input_file:
    memory = "".join(input_file.readlines())

regex = r"mul\(\d{1,3},\d{1,3}\)"
instructions = re.findall(regex, memory)
total = 0

for instruction in instructions:
    total += compute_instruction(instruction)

print(total)

regex2 = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
instructions = re.findall(regex2, memory)
total2 = 0

do = True
for instruction in instructions:
    if instruction == "do()":
        do = True
    elif instruction == "don't()":
        do = False
    elif do:
        total2 += compute_instruction(instruction)

print(total2)
