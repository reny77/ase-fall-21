#calculator.py

def sum(m,n):
    x = m
    for _ in range(n):
        x = x+1
    return x

def divide(m,n):
    x = m
    for _ in range(n):
        x = x-n
    return x

def main():
    print(f"Result is: {sum(10,3)}")

if __name__ == "__main__":
    main()
