
def varianza(list, med):
    sum = 0
    
    for i in list:
        sum += (i - med)**2
        
    return sum / len(list)