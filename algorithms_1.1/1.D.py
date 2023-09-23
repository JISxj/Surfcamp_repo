a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif a == 0 and b == 0 and c == 0:
    print("MANY SOLUTIONS")
elif a != 0 and b == 0 and c == 0:
    print(0)
else:
    if a != 0:
        res = (c ** 2 - b) / a
        if int(res) == res:
            print(int(res))
        else:
            print("NO SOLUTION")
    elif b == c ** 2:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
