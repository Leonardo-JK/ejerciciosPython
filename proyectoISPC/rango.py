def rango(list):
    max = 0
    min = 999999999999
    
    for i in list:
        if i < min:
            min = i
        
        if i > max:
            max = i
            
    return max - min