class Rectange():
    #this is a class variable
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))


r1 = Rectange(10, 24)
r2 = Rectange(20, 40)
r3 = Rectange(100, 200)


print(Rectange.recs)