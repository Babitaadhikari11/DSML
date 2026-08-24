class UnderageError(Exception):
    pass
def register_user(name, age):

    if not age.isdigit():
        raise ValueError("Age must be numeric")

    age = int(age)

    if age < 18:
        raise UnderageError("You must be 18 or above")

    print("Welcome", name)

name = input("Enter your name: ")
age = input("Enter your age: ")

try:
    register_user(name, age)

except UnderageError as e:
    print("age must be greater")
    print(e)

except ValueError as e:
    print(e)

else:
    print("Registration successful")

finally:
    print("Thank you for using MovieTime!")