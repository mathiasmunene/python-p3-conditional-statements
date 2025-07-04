#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    return "Access denied"
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return ("It's brisk out there!")
    elif 40 <= temperature <= 65:
        return ("It's a little chilly out there!")
    elif temperature > 85:
        return("It's too dang hot out there!")
    else:
        return("It's perfect out there!")

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0 and number != 0:  # Exclude 0
        return "FizzBuzz"
    elif number == 0:  # Handle 0 explicitly
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return number

def calculator(operation, num1, num2):
    # your code here
    try:
        if operation == "+":
            return (num1 + num2)
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        else:
            print("Invalid operation!")
            return None
    except ZeroDivisionError:
        print("Invalid operation!")
        return None
    
