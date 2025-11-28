N = int(input())
dict_a = {}
dict_f = {}
dict_fs = {}

def f(n):
    return sum(list(map(int, str(n))))

for i in range(N+1):
    if i == 0:
        dict_f[i] = 1
        dict_fs[i] = 1
    elif i == 1:
        dict_f[i] = 1
        dict_fs[i] = 2
    else:
        dict_f[i] = f(dict_fs[i-1])
        dict_fs[i] = dict_fs[i-2] + dict_f[i-1]

print("dict_f", dict_f)
print("dict_fs", dict_fs)