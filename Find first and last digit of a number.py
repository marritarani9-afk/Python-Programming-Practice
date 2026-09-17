n = int(input("Enter a number: "))

last_digit = n % 10

while n >= 10:
    n = n // 10

first_digit = n

print("First digit =", first_digit)
print("Last digit =", last_digit)