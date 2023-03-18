# multiplication_table.py
n = int(input("Enter a number: "))
print("Multiplication Table for", n)

# Generate multiplication table
for i in range(1, 11):
    result = n * i
    print(n, "x", i, "=", result)
