import csv

with open("st.csv", "w", newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])