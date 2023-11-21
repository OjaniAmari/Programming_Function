def Hello():
    print("Hello, How was your day.")
def goodbye():
    print("goodbye, have a good day")
def joke():
    print("What does a cow say? ")
    print("mooo")
def call_name(name):
    print(f"hello {name}")
def data_input(data1,data2):
    print(f"first data is: {data1}, second data: {data2}")
data_input(54,32)




def addition(number1, number2):
    print(number1 + number2)
addition(51, 32)
def data_call():
    test_data = 45
    return result

result = addition(78, 74)
print(result)


data = data_call()
print(data)

def subtraction(num1, num2):
    print(num1 - num2)
    return result

subtraction = subtraction(99, 9)
print(subtraction)

def multiply(num1, num2):
    print(num1 * num2)
    return result

multiply = multiply(45, 10)
print(multiply)

def division(num1, num2):
    print(num1 / num2)
    return result
division = division(55, 5)
print(division)


call_name("Ojani")
  
def main():
    while True:
        user = input("Enter Hello, goodbye or joke: ")
        if user == "Hello":
            Hello()
        if user == "goodbye":
            goodbye()
        if user == "joke":
            joke()
        elif user == "exit":
            print("Goodbye, you Waste of Time!")
            break

        else:
            print("Invalid input")
        
            
main()