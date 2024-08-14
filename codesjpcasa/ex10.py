repeatvalue = 0
while (repeatvalue == 0):
    op = str(input("Digite a operação: "))
    if ( op == "S" ):
        print ("Fechando calculadora...")
        repeatvalue = 1
    else:
        n1 = float(input("Digite o numero um: "))
        n2 = float(input("Digite o numero dois: "))
        if ( op == "+" ):
            sm = n1 + n2
            print (sm)
        elif ( op == "-" ):
            sm = n1 - n2
            print (sm)
        elif ( op == "/" ):
            sm = n1 / n2
            print (sm)
        elif ( op == "*" ):
            sm = n1 *n2
            print (sm)
    

        else:
            "Erro, lembre se de usar + , - , / , * ou S caso voce feche"

    

    
    

    

    

    
