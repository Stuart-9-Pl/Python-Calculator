def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Pomylka: dilennia na null!"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("5 + 3 =", add(5, 3))
    print("5 / 0 =", divide(5, 0))
