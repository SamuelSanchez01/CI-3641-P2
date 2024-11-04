import time
import matplotlib.pyplot as plt

#Traduccion literal
def F_Traduct(n: int):
    if 0 <= n < 35:
        return n
    else: 
        return F_Traduct(n-5) + F_Traduct(n-10) + F_Traduct(n-15) + F_Traduct(n-20) + F_Traduct(n-25) + F_Traduct(n-30) + F_Traduct(n-35)   

#Recursion de cola
def F_Tail(n, acc1, acc2, acc3, acc4, acc5, acc6, acc7):
    if n < 5:
        return acc1
    else:
        return F_Tail(n-5, acc2, acc3, acc4, acc5, acc6, acc7, acc1+acc2+acc3+acc4+acc5+acc6+acc7)

#Wrapper para usar la recursion de cola
def F_TailWrapper(n):
    m = n % 5
    return F_Tail(n, 0 + m, 5 + m, 10 + m, 15 + m, 20 + m, 25 + m, 30 + m)

#De recursion de cola a iterativo
def F_Iter(n):
    if n < 5:
        return n
    
    m = n % 5

    acc1, acc2, acc3, acc4, acc5, acc6 , acc7 = 0 + m, 5 + m, 10 + m, 15 + m, 20 + m, 25 + m, 30 + m

    while n > 0:
        acc1, acc2, acc3, acc4, acc5, acc6 , acc7 = acc2, acc3, acc4, acc5, acc6 , acc7, acc1+acc2+acc3+acc4+acc5+acc6+acc7
        n -= 5
    return acc1

tras = []
tail = []
iter = []

for i in range(1,151):
    startTime = time.time()
    result = F_Traduct(i)
    endTime = time.time()
    tras.append(endTime - startTime)

    startTime = time.time()
    result = F_TailWrapper(i)
    endTime = time.time()
    tail.append(endTime - startTime)

    startTime = time.time()
    result = F_Iter(i)
    endTime = time.time()
    iter.append(endTime - startTime)
    print(i)

#1-50
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(range(1, 51), tras[:50], label='F_Traduct')
plt.plot(range(1, 51), tail[:50], label='F_TailWrapper')
plt.plot(range(1, 51), iter[:50], label='F_Iter')
plt.xlabel('n')
plt.ylabel('Tiempo de ejecucion (s)')
plt.title('De 1 a 20')
plt.legend()

#1-150 normal
plt.subplot(1, 3, 2)
plt.plot(range(1, 151), tras, label='F_Traduct')
plt.plot(range(1, 151), tail, label='F_TailWrapper')
plt.plot(range(1, 151), iter, label='F_Iter')
plt.xlabel('n')
plt.ylabel('Tiempo de ejecucion (s)')
plt.title('De 1 a 150')
plt.legend()

#1-150 log
plt.subplot(1, 3, 3)
plt.plot(range(1, 151), tras, label='F_Traduct')
plt.plot(range(1, 151), tail, label='F_TailWrapper')
plt.plot(range(1, 151), iter, label='F_Iter')
plt.xlabel('n')
plt.ylabel('Tiempo de ejecucion (s)')
plt.yscale('log')
plt.title('De 1 a 150 (Escala logaritmica)')
plt.legend()

plt.tight_layout()

#Se guarda la figura
plt.savefig('tiemposEjecucion.png')
plt.show()