

def automata(palabra):
    estado = 0
    enteros = ['0','1','2','3','4','5','6','7','8','9']
    indice = 0
    numeros = []
    if palabra:
        print('***************************************\ncaracter | representa\n***************************************')
        # estado 0
        if palabra[0] in enteros:
            estado=1
        elif palabra[0] == '*':
            estado=3
        elif palabra[0] == '+':
            estado=2
        # estado 0
        for letra in palabra:
            # print("el edo es",estado," ","la letra es",letra," ","el indice es",indice)
            if(estado==1):
                if letra == '+':
                    if(indice+1 < len(palabra)):
                        if(not palabra[indice+1]=='+'):     
                            print('+ | suma')
                            print('---------------------------------------')
                            estado = 2
                        else:
                            estado = 4
                    else:
                        print('+ | suma')
                        print('---------------------------------------')
                        estado = 2
                elif letra in enteros:
                    # hacer que cheque si el siguiente es un numero
                    #primero checar que el siguiente no está fuera de rango
                    if(indice+1 < len(palabra)):
                        if(palabra[indice+1] in enteros):
                            # si el que le sigue es un numero no imprimir nada, solo meter a la lista
                            # vuelve al estado 1
                            estado = 1
                            numeros.append(letra)
                        else:
                            # si el siguiente no es un entero entonces imprimir la lista 
                            numeros.append(letra)
                            print(''.join(numeros),'| numero')
                            print('---------------------------------------')
                    else:
                        # si la cadena termina con un numero
                        numeros.append(letra)
                        print(''.join(numeros),'| numero')
                        print('---------------------------------------')
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    print('False')
                    return False
            elif(estado==2):
                if letra == '+':
                    if(indice+1 < len(palabra)):
                        if(not palabra[indice+1]=='+'):     
                            print('+ | suma')
                            print('---------------------------------------')
                            estado = 2
                        else:
                            estado = 4
                    else:
                        print('+ | suma')
                        print('---------------------------------------')
                        estado = 4
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                    numeros.append(letra)
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    print('False')
                    return False
            elif(estado==3):
                if letra == '+':
                    if(indice+1 < len(palabra)):
                        if(not palabra[indice+1]=='+'):     
                            print('+ | suma')
                            print('---------------------------------------')
                            estado = 2
                        else:
                            estado = 4
                    else:
                        print('+ | suma')
                        print('---------------------------------------')
                        estado = 2
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    print('False')
                    return False
            elif(estado==4):
                if letra == '+':
                    print('++ | incremento')
                    print('---------------------------------------')
                    estado = 2
                elif letra in enteros:
                    print(letra,'| numero')
                    print('---------------------------------------')
                    estado = 1
                    numeros.append(letra)
                elif letra == '*':
                    print('* | producto')
                    print('---------------------------------------')
                    estado = 3
                else:
                    print('False')
                    return False
            else:
                print('False')
                return False
            #aumentar indice
            indice += 1
        # print(numeros)
    else:
        print('False')
        return False

    

# automata('++00')#esto da un resultado incorrecto
# automata('*00')#esto da un resultado incorrecto
automata('00')
# automata(input())