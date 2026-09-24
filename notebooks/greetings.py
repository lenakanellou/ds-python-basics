print("Top-level code ran")

def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(f"This file is being run directly: __name__ is {__name__}")
    print(hello("student"))