class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return "({0},{1})".format(self.x,self.y)


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

        
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)


    def __truediv__(self,other):
        if other.x == 0:
            raise Exception("The x of the second point is 0.")
        if other.y == 0:
            raise Exception("The y of the second point is 0.")
        x = self.x / other.x
        y = self.y / other.y
        return Point(x,y)


# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1+p2)

# p2+p1
# 1. x12345 + p1
# 2. x12345 + x12346
# 3. x12345.__add__(x12346)
#   4. other = x12346
#   5. x = self.x + other.x
#   6. x = 2(p2 er self.x) + other.x
#   7. x = 2 + 1(p1 er self.x)
#   8. x = 3
#   9. y = self.y + other.y
#   10. y = 3(p2 er self.y) +  other.y
#   11. y = 3 + 2(p1 er self.y)
#   12. y = 5
#   13. return Point(x, y)
#   14. return Point(3, 5)
#   15. return x12333
# x12333
# p3 = p2 + p1

# 1. p2-p1
# 2. x12345-p1
# 3. x12345 - x12346
# 4. x12345.__sub__(x12346)
#   5. other = x12346
#   6. x = self.x - other.x
#   7. x = 2(p2 er self.x) - other.x
#   8. x = 2 - 1(p1 er self.x)
#   9. x = 1
#   10. y = self.y - other.y
#   11. y = 3(p2 er self.y) - other.y
#   12. y = 3 - 2(p1 er self.y)
#   13. y = 1
#   14. return Point(x,y)
#   15. return Point(1,1)
#   16. return x12344
# x12344


# p2 er coordinate: (5,6)
# p1 er coordicate: (0,0)


# 1. p2/p1
# 2. x12345 / p1
# 3. x12345 / x12346
# 4. x12345.__truediv__(x12346)
#   5. 