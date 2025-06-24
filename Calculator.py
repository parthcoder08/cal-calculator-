
# calculator.py

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except Exception as e:
        return f"Invalid input: {e}"

def main():
    print("Simple Command-line Calculator")
    print("Enter expressions like a+b, a*b, a/b, a-b")
    print("Type 'exit' to quit.\n")
    
    while True:
        expr = input(">>> ")
        if expr.lower() == 'exit':
            break
        output = calculate(expr)
        print("= ", output)

if __name__ == "__main__":
    main()