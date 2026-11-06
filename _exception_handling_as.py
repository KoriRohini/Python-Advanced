try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    result = a / b

except Exception as e:
    print("Error:", e)