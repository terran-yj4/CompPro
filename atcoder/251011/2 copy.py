N = int(input())
dict_a = {}
dict_f = {}
dict_fs = {}

def f(n):
    return sum(list(map(int, str(n))))

dict_a[1] = 1
dict_fs[1] = 1
for i in range(2, 101):
    dict_a[i] = dict_fs[i-1]
    dict_f[i] = f(dict_a[i])
    dict_fs[i] = dict_fs[i-1] + dict_f[i]


print(dict_fs[N])