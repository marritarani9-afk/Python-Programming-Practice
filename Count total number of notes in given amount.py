amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10]
total_notes = 0

for note in notes:
    count = amount // note
    total_notes = total_notes + count
    amount = amount % note

print("Total number of notes:", total_notes)