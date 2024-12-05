left = []
right = []

with open("input_01.txt") as input_file:
    for line in input_file:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

diff = 0
for l, r in zip(sorted(left), sorted(right)):
    diff += abs(l - r)

print(diff)

similarity_score = 0

for l in left:
    similarity_score += l * right.count(l)

print(similarity_score)
