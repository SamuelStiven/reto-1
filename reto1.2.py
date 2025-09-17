def palindrome_word(word):
    empty_list = []
    empty_list2 = []
    for i in word:
        empty_list.append(i)
    for i in range(len(empty_list)-1, -1, -1):
        empty_list2.append(empty_list[i])
        
    if empty_list == empty_list2:
        return True
    
word = str(input("insert a word for palindrome evaluation:"))

if palindrome_word(word) == True:
    print("that word indeed, is palindrome")
else:
    print("that word is not palindrome")
    
"""Como no se podia usar slicing, se creo uno de manera manual, cada vez que el usuario inserta
una palabra por el teclado, pasa al flujo de una funcion que recorre cada caracter de la palabra
dada y los inserta en una lista, ahora con esa lista de caracteres, se recorria desde el numero de
elementos de la lista -1, pues queremos ahora analizar posicion. Desde esa posicion positiva, se recorre
hacia atras dicha lista de caracteres, y para cada caracter en reversa se ingresa en otra segunda lista 
de caracteres. A lo ultimo simplemente comparamos la primer lista de caracteres en orden, con la segunda
lista de caracteres en reversa."""