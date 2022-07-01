
def prod_elements(list):
    prod = []
    
    #Combinaciones posibles de elementos sin importar repeticion.
    for i in range(len(list)):
        for j in range(len(list) - 1 -  i):
            prod.append(list[i] * list[j + 1 + i])
            
    return prod

def prod_no_repeat(list):
    #Combinaciones posibles de elementos sin repetir.
    aux = []
    prod = []
    
    for num in list:
        if num in aux:
            continue
        else:
            aux.append(num)
        
    for i in range(len(aux)):
        for j in range(len(aux) - 1 -  i):
            prod.append(aux[i] * aux[j + 1 + i])
            
    return prod

def prod_no_repeat2(list):
    #Combinaciones posibles de elementos sin repetir.
    aux = []
    prod = []
    
    for num in list:
        if num not in aux:
            aux.append(num)            
        
    for i in range(len(aux)):
        for j in range(len(aux) - 1 -  i):
            prod.append(aux[i] * aux[j + 1 + i])
            
    return prod
