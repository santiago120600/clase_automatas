# Instrucciones:  Realizar un un autómata finito que sea capas de reconocer un lenguaje que esta compuesto por números enteros sin signo, la suma, incremento y el producto, la suma esta representado por el signo +, el incremento por ++ y el producto *.

# El autómata deberá de estar programado en Python, el input del programa será una palabra creada por el language y el output será True en caso de que sea una palabra valida dentro de mi lenguaje o False en caso de que no sea una palabra validad.


def automata(cadena):
    alfabeto = ['1','2','3','4','5','6','7','8','9','0','+','*']
    # recorrer cada caracter de la cadena
    for c in cadena:
        if c in alfabeto:
           pass 
        else:
          return False 
    return True


print(automata('01234+'))
print(automata('01234w'))



