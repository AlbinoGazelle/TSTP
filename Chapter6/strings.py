""" y = "cat" + "in" + "the" + "hat"
print(y)

z = "We hold these truths...".upper()
print(z)

x = "SO IT GOES.".lower()
print(x)

t = "four score and...".capitalize()
print(t)

last = "Faulkner"
b = "Willian {}".format(last)
print(b) """

n1 = input("Enter a noun:")
v = input("Enter a verb:")
adj = input("Enter an adj:")
n2 = input("Enter a noun:")

r = """The {} {} the {} {}
    """.format(n1, v, adj, n2)

print(r)