answer = input("Whats you're favorite color?")
with open("Fav_color.txt", "w") as f:
    f.write(answer)