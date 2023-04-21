def maximumAmount(n):
    zeroAmount = n.count ('0')
    oneAmount = n.count('1')

    if (zeroAmount > oneAmount):
        maximumAmount = oneAmount
    elif (zeroAmount < oneAmount):
        maximumAmount = zeroAmount
    else:
        maximumAmount = 0

    return maximumAmount

t = int(input())
num_list = []

# Lê o array dado como input e coloca numa lista
for i in range(t):
    num = str(input())
    num_list.append(num)

# Calcula o número total de 0's ou 1's que podem ser removidos para cada caso
for j in range(t):
    maxAmount = 0
    maxAmount = maximumAmount(num_list[j])
    print(maxAmount)