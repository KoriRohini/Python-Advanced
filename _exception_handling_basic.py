try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    result = a / b
    print(result)

except Exception:
    print("Cannot divide by zero")

print("Bye")