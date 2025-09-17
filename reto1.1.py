def basics_operations(operand, number1, number2):
    if operand == "+":
        return number1 + number2
    if operand == "-":
        return number1 - number2
    if operand == "*":
        return number1 * number2
    if operand == "/":
        return number1 / number2
operand = str(input("What kind of operation do you want to do?, |+, -, *, /|: "))   
number1 = float(input("insert the first number of operation: "))
number2 = float(input("insert the second number of operation: "))         

print(f"the {operand} among numbers is: {basics_operations(operand, number1, number2)}")

"""Para este ejercicio simplemente se pregunta al teclado, que operador y entre que numeros
se quiere hacer la operacion que represente el operador, y en una funcion asegurarnos de que
dependiendo el operador, se retorne una operacion entre el primer numero y el segundo con dicho
operador"""