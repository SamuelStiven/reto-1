def group_words_by_letters(word_list):
    groups = {} 
    for word in word_list:
        letters = ''.join(sorted(word.lower()))
        if letters not in groups:
            groups[letters] = []
        groups[letters].append(word)
    return groups

amount = int(input("How many words do you want to analyze?: "))
words = []

for number in range(amount):
    word = input("insert words: ")
    words.append(word)

result = group_words_by_letters(words)



if len(result) == 1:
    print("all words use the same letters")
    print("Words:", list(result.values())[0])
else:
    print("The words have different letters")
    print(f"Found {len(result)} groups:")
    for number, group in enumerate(result.values(), 1):
        print(f"Group {number}: {group}")
"""Para llegar al resultado primero debiamos analizar cada palabra de una lista de palabras,
y a cada palabra debiamos asegurarnos que tuvieran los mismos caracteres, independientemente
de las mayusculas o el orden de los mismos. Luego con las palabras convertidas en minusculas y en
un order determinado(orden alfabetico), podiamos crear claves unicas para grupo de palabras que 
compartieran los mismos caracteres, es decir, un diccionario de grupos de palabras. Luego si
dicho diccionario solo tenia un grupo, o todos las palabras eran equivalentes o solo habia una palabra
y si habian distintos grupos, daba la posibilidad de que hubieran grupos de palabras equivalentes, 
dependiendo el numero de elementos que proporcionara esa clave del diccionario""" 