
def sumRandom(list):
    sum = []
    
    for i in range(len(list)):
        for j in range(len(list) - 1 -  i):
            sum.append(list[i] + list[j + 1 + i])
    
    return sum
            
