n = int(input("Enter a number: "))

words = ["Zero", "One", "Two", "Three", "Four",
         "Five", "Six", "Seven", "Eight", "Nine"]

if n == 0:
    print("Zero")
else:
    digits = []

    while n != 0:
        digit = n % 10
        digits.append(digit)
        n = n // 10

    digits.reverse()

    for digit in digits:
        print(words[digit], end=" ")