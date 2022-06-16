import random
import time

def genrnd(n):
    # rndList = [random.randint(0, 9) for x in range(n)]
    rndList = []
    for i in range(n):
        rndList.append(random.randint(0, 9))
    return rndList

nextT = 0
y = [0, 0]
x = []
c= []
p = 0

for i in range(10):
    try:
        Xi= 10**i * 5
        print("Array de ", Xi, "elementos:")
        inicio = time.time()
        a = genrnd(10**i * 1)
        t = time.time() - inicio
        print("Tarda: ", t, "s")
        
        if i == 0:
            c.append(t)
            y[0] = t
            x.append(Xi)
            
            p = c[i]
        
        if i == 1:
            y[1] = t
            x.append(Xi)
            
            c.append(( y[1] - y[0] ) / ( x[1] - x[0] ))
            print(p)
            p += (c[i] * (10**(i+1) * 1))
        
        if i > 1:
            y = [y[1], t]
            x.append(Xi)
            dStr = ""
            d = 1
            for j in range(i):
                d *= (x[i] - x[j])
            
            
            
            c.append(( y[1] - p * x[i]) / d)
            
            p += (c[i] * d)
            
        nextT = p
        
    except KeyboardInterrupt:
        print("interumpido")