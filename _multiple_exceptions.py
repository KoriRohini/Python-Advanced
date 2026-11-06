try:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    result = a / b

except ZeroDivisionError as zde:
    print(zde)

except ValueError as ve:
    print(ve)

except Exception as e:
    print(e)