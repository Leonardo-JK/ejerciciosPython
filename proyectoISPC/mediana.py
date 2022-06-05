
def mediana(list):
    if len(list) % 2 == 0:
        return ((sorted(list)[len(list) // 2] + sorted(list)[len(list) // 2 - 1]) / 2)
    else:
        return sorted(list)[len(list) // 2]
