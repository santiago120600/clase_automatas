# Automata reconoce palabras multipo de 3 con abecedario {0,1}

def automata(palabra):
    edo = 0
    if not palabra:
        return True
    for letra in palabra:
        if edo == 0:
            if letra == '0' or letra =='1':
                edo = 1
            else: 
                return False
        elif edo == 1:
            if letra == '0' or letra =='1':
                edo = 2
            else: 
                return False
        elif edo == 2:
            if letra == '0' or letra =='1':
               edo  = 0
            else: 
                return False
    return True
print(automata('0000'))
