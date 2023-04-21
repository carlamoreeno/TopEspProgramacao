t = int(input())

for x in range(t):
    s = list(input())
    open = ""
    total = 0
    for ch in s:
        if ch not in open:
            open += ch
        else:
            total += len(open)-1
            open = ""
    total += len(open)
    print(total)