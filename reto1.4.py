def most_valuated_adition(list):
    list_aditions = []
    while len(list) != 0:
        adition = list[0] + list[1]
        list_aditions.append(adition)
        list.pop(0)
        list.pop(0)
    return max(list_aditions)
         
amount_numbers = int(input("how many numbers do you want to evaluate?:"))
if amount_numbers % 2 !=0:
   amount_numbers = int(input("how many numbers do you want to evaluate?(even number):"))
    
    
list_numbers = []    
for i in range(amount_numbers):
    numbers = int(input("insert those numbers to evaluate:"))
    list_numbers.append(numbers)            
print("the most value in aditions betwen two numbers consecutives is:", most_valuated_adition(list_numbers))

"""Para este ejercicio se pregunta la cantidad de numeros a evaluar, la cual en este caso, es conveniente
asegurarnos que ese numero es par. Luego con esa cantidad, preguntamos al teclado cuales seran los numeros
y los ingresamos a una lista. En una funcion se analiza esa lista, la cual en un ciclo while, mientras
el numero de elementos de esa lista de numeros no sea cero, debe sumar los numeros de la posicion 0 y 1, 
y al mismo tiempo eliminarlos, para tener la posibilidad de operar siempre entre una cantidad par de numeros
esa suma se ingresa a una lista y la funcion retorna el maximo de dicha lista"""