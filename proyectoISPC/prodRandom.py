
def prodRandom(list):
    prod = []
    
    for i in range(len(list)):
        for j in range(len(list) - 1 -  i):
            prod.append(list[i] * list[j + 1 + i])
    
    return prod
            