def strings(string):
    try:
        return float(string)
    except ValueError:
        print("Error!")

z = strings(101.1)
print(z)