def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

def division(a,b):
    if b==0:
        raise ValueError("Cannot divide by o")
    return a/b


if __name__ == "__main__":
    print("Addition:", add(7,5))
    print("Subtraction:", sub(7,5))
    print("Multiplication:", mul(7,5))
    print("Division:", division(7,5))
