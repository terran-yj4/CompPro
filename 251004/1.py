X, Y = input().split()

osver = {
    "Ocelot": 0,
    "Serval": 1,
    "Lynx": 2
}

if osver[X] >= osver[Y]:
    print("Yes")
else:
    print("No")