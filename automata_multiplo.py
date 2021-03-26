# Automata reconoce palabras multipo de 3 con abecedario {0,1}

def automata(palabra):
    edo = 0
    indx = 1
    if not palabra:
        return True
    if palabra[0]=='0' or palabra[0]=='1':
        edo = 1
    for letra in palabra:
        if edo == 0:
            if letra == '0' or letra =='1':
                edo = 1
            else: 
                return False
        elif edo == 1:
            if letra == '0' or letra =='1':
                if indx == len(palabra):
                    return False
                else:
                    edo = 2
            else: 
                return False
        elif edo == 2:
            if letra == '0' or letra =='1':
                if indx == len(palabra):
                    return False
                else:
                   edo  = 0
            else: 
                return False
        indx+=1            
    return True
print(automata('010'))
