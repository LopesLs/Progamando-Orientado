# Crie funções pra tratar diferentes tipos de erro

def trata_int(input):
    
    try:
        return int(input)
    
    except ValueError as erro:
        return f'Falha de valor -> {erro}'

    except TypeError as erro:
        return f'Falha de tipo -> {erro}'

def trata_index(input):

    try:
        return input[20]
    
    except IndexError as erro:
        return f'Falha de index -> {erro}'
    
    except TypeError as erro:
        return f'Falha de tipo -> {erro}'
    
def trata_atribute(input):

    try:
        return input.att

    except AttributeError as erro:
        return f'Falha de atributo -> {erro}'

    except TypeError as erro:
        return f'Falha de tipo -> {erro}'

def trata_list(input):

    try:
        return list(input)
        
    except TypeError as erro:
        return f'Falha de tipo -> {erro}'

def trata_division(input):

    try:
        return 1/input
    
    except ZeroDivisionError as erro:
        return f'Falha de divisão -> {erro}'

    except TypeError as erro:
        return f'Falha de tipo -> {erro}'
