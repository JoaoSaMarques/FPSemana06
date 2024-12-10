#1
def mul_all(lista): #Recebe uma lista de números
    
    if lista == []:
        return 0
    
    resultado = 1 #Needed so we can multiply it by quadrado
    
    for i in lista: #Goes through each number in the list
        quadrado = i * i #square
        resultado *= quadrado #multiplication of the square
        
    return resultado

print(mul_all([]))
#0

print(mul_all([1, 2, 3]))
#36

#===============================================================================

#2
def to_grid(lista, n, m): #Elementos 
    
    grid = [] 
    elementos = n * m
    
    if len(lista) < elementos: #If the list of numbers is smaller than n * m
        return grid
    
    else:
        for i in range(n):
            start = i * m # = 0
            end = start + m # next loop lets you start on the next number
            linha = lista[start : end] #from start to end
            grid.append(linha)
            
        return grid
    
print(to_grid([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 3)) #Lina * Coluna

#       M
#   [ 1 2 3 ]
# N [ 4 5 6 ]
#   [ 7 8 9 ]

#===============================================================================

#3

def count_words(sentence):
    dicionario  = {}
    
    word_list = sentence.split(" ")
    
    for word in word_list:
        if word in dicionario:
            dicionario[word] += 1
        else:
            dicionario[word] = 1
            
    for word, count in dicionario.items():
        print(f'The word "{word}" appears {count} times.')

print(count_words("BANANA COM PURE DE BATATA, FEITO DE BANANA"))

#===============================================================================

#4

def is_leap_year(year):
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
print(is_leap_year(1900))

print(is_leap_year(2000))

print(is_leap_year(2003))

print(is_leap_year(2024))

#===============================================================================

#5

def data_validator(data):
    componentes = data.split("/")
    
    if len(componentes) != 3:
        return "A data tem de ter formato dd/mm/yy"
    
    dia =  int(componentes[0])
    mes =  int(componentes[1])
    ano =  int(componentes[2])
    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        maximo = 31
        
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        maximo = 30
        
    elif mes == 2:
        if is_leap_year(ano):
            maximo = 29
        else:
            maximo = 28
        
    else:
        return "A data não é valida!"
    
    if dia < 1 or dia > maximo:
        return f"O mês {mes} só tem {maximo} dias!"
    
    return "A data é valida!"
    
print(data_validator("30/01/2003"))