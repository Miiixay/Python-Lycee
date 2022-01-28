#Compléter la fonction récursive nbOperationsFibonacci.
def fibonacci(n):
    a,b = 0,1
    for i in range(1,n):
        a,b = b,a+b
    return b

r=str(fibonacci(40)-1)

print(f'Le millième terme de la suite de Fibonacci a {len(r)} chiffres et vaut {r}.')

#Vérifier que nbOperationsFibonacci(10)=54 et nbOperationsFibonacci(40)=102334154.