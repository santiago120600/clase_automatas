

def automata(palabra):
    estado = 0
    resultado = True
    suma = 0
    enteros = ['0','1','2','3','4','5','6','7','8','9']
    if palabra:
        for letra in palabra:
            if(estado==0):
                if letra == '+':
                    estado = 2
                elif letra in enteros:
                    estado = 1
                elif letra == '*':
                    estado = 3
                else:
                    return False
            elif(estado==1):
                if letra == '+':
                    estado = 2
                elif letra in enteros:
                    estado = 1
                elif letra == '*':
                    estado = 3
                else:
                    return False
            elif(estado==2):
                if letra == '+':
                    estado = 4
                elif letra in enteros:
                    estado = 1
                elif letra == '*':
                    estado = 3
                else:
                    return False
            elif(estado==3):
                if letra == '+':
                    estado = 2
                elif letra in enteros:
                    estado = 1
                elif letra == '*':
                    estado = 3
                else:
                    return False
            elif(estado==4):
                if letra == '+':
                    estado = 2
                elif letra in enteros:
                    estado = 1
                elif letra == '*':
                    estado = 3
                else:
                    return False
            else:
                return False
    else:
        return False


automata('0123')