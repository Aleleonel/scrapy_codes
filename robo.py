class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Reward(Point):

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name


class Robot(Point):

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento Proibido!')

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento Proibido!')

    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento Proibido!')

    def move_rigth(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Movimento Proibido!')


reward1 = Reward(1, 1, 'moeda de ouro')
r2d2 = Robot(5, 5)

r2d2.move_down()

print(reward1.name)
print(r2d2.y)


