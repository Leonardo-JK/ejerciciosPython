
def mediana(list):
    l = sorted(list)
    
    if len(list) % 2 == 0:
        return ((l[len(list) // 2] + l[len(list) // 2 - 1]) / 2)
    else:
        return l[len(list) // 2]
