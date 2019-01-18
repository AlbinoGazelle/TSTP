class Shape():
    def what_am_i(self):
        print("I am a shape")




class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_perm(self):
        return self.width * 2 + self.length * 2




class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def change_s1(self, new_size):
        self.s1 += new_size
    def calc_perm(self):
        return self.s1 * 4

a_rect = Rectangle(25, 30)
b_square = Square(20)

print(a_rect.calc_perm())
print(b_square.calc_perm())


a_rect.what_am_i()
b_square.what_am_i()