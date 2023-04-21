def minimumSteps(n):
    str = []

    # Converte número em string para avaliarmos os últimos 2 digitos e checar divisibilidade por 25
    i = 0
    while (n != 0):
        rem = n % 10
        ch = chr(rem + ord('0'))
        str.append(ch)
        n = (n // 10)
    str.reverse()

    minimumSteps = (10 ** 18) + 1
    N = len(str)
    for i in range(N):
        for j in range(i + 1, N):

            # Últimos 2 digitos
            num = (ord(str[i]) - ord('0')) * 10 + (ord(str[j]) - ord('0'))

            if (num % 25 == 0):
                # Contagem de digitos indesejados entre i e j
                x = j - i - 1

                # Contagem de digitos indesejados depois de j
                y = N - (j + 1)
                minimumSteps = min(minimumSteps, x + y)

    return minimumSteps

t = int(input())
num_list = []

# Lê o array dado como input e coloca numa lista
for i in range(t):
    num = int(input())
    num_list.append(num)

# Para cada item da lista, é calculado o número mínimo de passos para se chegar em um número positivo divisível por 25
for j in range (t):
    minSteps = minimumSteps(num_list[j])
    if (minSteps > 10 ** 18):
        print("Number N exceeds limit accepted")
    else:
        print(minSteps)