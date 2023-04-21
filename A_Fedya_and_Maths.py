def expression(n):
    if (n%4):
        return 0
    else:
        return 4

n = int(input())
result = expression(n)
print(result)