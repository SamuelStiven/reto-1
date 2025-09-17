def look_those_prime_numbers(prime):
    if prime <=1:
        return False
    if prime ==2:
        return prime
    for i in range(2, int(prime**0.5)+1):
        if prime % i ==0:
            return False
    if True: 
        return prime
    

amount_numbers = int(input("how many numbers do you want to evaluate?:"))
list_numbers = []    
for i in range(amount_numbers):
    numbers = int(input("insert those numbers to evaluate:"))
    list_numbers.append(look_those_prime_numbers(numbers))
print(list_numbers)

"""Un ejercicio sencillo, el cual pregunta la cantidad de numeros a evaluar, en ese sentido se empieza
a preguntar por un numero, el cual se analiza en una funcion y dependiendo si es primo o no
retorna determinado valor. En ese mismo ciclo que pregunta la cantidad de numeros, se ingresa el valor
que retorno dicha funcion para el numero a una lista -False si no es primo y el numero como tal, si lo es."""
            