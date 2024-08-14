maior = float('-inf')
menor = float('inf')

x=0
while ( x < 5 ):
    num = float(input("digite um numero:"))

    if ( num > maior):
        maior = num
    elif ( num < menor):
        menor = num

    x = x + 1

print( maior , menor)