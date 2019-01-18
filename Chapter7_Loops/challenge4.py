numbers = [15, 32, 199, 22, 11]

while True:
    answer = input("Guess a number:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Error! Please type a number!")
    if answer in numbers:
        print("Correct")
    else:
        print("Incorrect!")