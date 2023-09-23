def main():
    ans = 0
    n = int(input())
    vars = list(sorted(map(int, input().split())))
    if len(vars) == 2:
        print(vars[1] - vars[0])
    else:
        for i in range(0, len(vars), 2):
            if i == 0:
                ans += abs(vars[i + 1] - vars[i])
            elif i == len(vars) - 1:
                ans += abs(vars[i] - vars[i - 1])
            elif abs(vars[i] - vars[i - 1]) >= abs(vars[i + 1] - vars[i]):
                ans += abs(vars[i + 1] - vars[i])
            else:
                ans += abs(vars[i] - vars[i - 1])
    print(ans)


if __name__ == '__main__':
    main()