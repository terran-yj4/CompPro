N = int(input())

skill = {i: False for i in range(1, N+1)}

for i in range(1, N+1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        skill[i] = True
    if skill[a] or skill[b]:
        skill[i] = True

print(skill.clear)
