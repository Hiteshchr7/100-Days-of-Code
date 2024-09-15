def add(num1,num2) :
    return num1 + num2

def sub(num1,num2) :
    return num1 - num2

def mul(num1,num2) :
    return num1*num2

def mod(num1,num2) :
    if num2 != 0 :
        return num1/num2

n1 = float(input("What's the first number?: ")) 
start = True
while start :
    for operation in ["+","-","*","/"] :
        print(operation)

    op = input("Pick an operation: ")
    while op not in ["+","-","*","/"] :
        print("you didn't choose a valid operation. Choose again.\n")
        op = input("Pick an operation: ")

    n2 = float(input("what's the next number?: "))
    output = ""
    if op == "+" :
        output = add(n1,n2)
        print(f"{n1} + {n2} = {output} ")
    elif op == "-" :
        output = sub(n1,n2)
        print(f"{n1} - {n2} = {output} ")
    elif op == "*" :
        output = mul(n1,n2)
        print(f"{n1} * {n2} = {output} ")
    elif op == "/" :
        output = mod(n1,n2)
        print(f"{n1} / {n2} = {output} ")
    
    cont = input(f"Type 'y' to continue calculating with {output} or type 'n' to start a new calculation:\n")
    print()
    n1 = output
    if cont == 'n':
        start = False
