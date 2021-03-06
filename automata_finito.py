enteros = ['1','2','3','4','5','6','7','8','9','0']
datos = [] 

def automata(cadena):
    if cadena: 
        index = 0
        for c in cadena:
            if c in enteros:
                datos.append({'caracter':c,'valor':'entero'})
                edo_1(cadena,index+1)
                break
            elif c == '+':
                datos.append({'caracter':c,'valor':'suma'})
                edo_2(cadena,index+1)
                break
            elif c =='*':
                datos.append({'caracter':c,'valor':'producto'})
                edo_2(cadena,index+1)
                break
            else: 
                return False
        return print_table(datos)
    else: 
        return False

def edo_1(cadena,index):
    if index < len(cadena):
        caracter = cadena[index]
        if caracter in enteros:
            datos.append({'caracter':caracter,'valor':'entero'})
            edo_1(cadena,index+1)
        elif caracter == '+':
                datos.append({'caracter':caracter,'valor':'suma'})
                edo_2(cadena,index+1)
        elif caracter =='*':
            datos.append({'caracter':caracter,'valor':'producto'})
            edo_2(cadena,index+1)
        else: 
            return False
    else:
        return

def edo_2(cadena,index):
    pass

def edo_3(cadena,index):
    pass

def edo_4(cadena,index):
    pass

def print_table(datos):
    print('***************************************\ncaracter | representa\n***************************************')
    for dato in datos:
        print(dato['caracter'],'|',dato['valor'])
        print('------------------------------------------------------------')


print(automata('123'))
