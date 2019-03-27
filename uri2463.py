x = input()

corredor = list(map(int, input().split()))

maior = 0
for i in range(len(corredor)):
    total = 0
    for j in range(i+1, len(corredor)):
        total += corredor[i]
    maior = max(maior, total)