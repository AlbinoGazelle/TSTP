import csv

with open("st.csv", "r") as csv_read:
    r = csv.reader(csv_read, delimiter=",")
    for row in r:
        print(",".join(row))