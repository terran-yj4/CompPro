N, A, B = map(int, input().split())
ab = list(input())
a_list = []
b_list = []
for i in range(N):
    if ab[i] == "a":
        a_list.append(1)
        b_list.append(0)
    else:
        a_list.append(0)
        b_list.append(1)

a_sum_list = [0]
b_sum_list = [0]
a_sum = 0
b_sum = 0
for i in range(N):
    a_sum += a_list[i]
    b_sum += b_list[i]
    a_sum_list.append(a_sum)
    b_sum_list.append(b_sum)
print("asl:", a_sum_list)
print("bsl:", b_sum_list)

################################
"""
asl: [0, 1, 1, "1", "2", 3, 4, 4, "5", 6, 6, 7]      
bsl: [0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4]
"""

sums = []
err_sum = 0

for i in range(1, N+1):
    start = i
    last = i
    
    while a_sum_list[start] - a_sum_list[i-1] >= A and start < N:
        start += 1
    while b_sum_list[last] - b_sum_list[i-1] < B and last < N:
        last += 1
    
    if start >= N:
        continue
    h = last-1 if last <= N else N
    if start <= h:
        err_sum = last - start + 1

print(err_sum)
