import random


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return '<%s, %s>: %s' % (self.x, self.y, self.name)
        return f'{self.x, self.y}'


class Reward(Point):

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name

    def __str__(self):
        # return '<%s, %s>: %s' % (self.x, self.y, self.name)
        return f'{self.x, self.y, self.name}'

    def __repr__(self):
        return f'Rewards: {str(self)}'


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

    def check_reward(robot, rewards):
        ok = False
        for reward in rewards:
            if reward.x == robot.x and reward.y == robot.y:
                print("O Robo encontrou a recompensa: %s" % reward.name)
                ok = True
        return ok


r1 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r2 = Reward(random.randint(0, 10), random.randint(0, 10), 'bala')
r3 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r4 = Reward(random.randint(0, 10), random.randint(0, 10), 'oleo')
r5 = Reward(random.randint(0, 10), random.randint(0, 10), 'chave')
r6 = Reward(random.randint(0, 10), random.randint(0, 10), 'engrenagem')
r7 = Reward(random.randint(0, 10), random.randint(0, 10), 'helice')
r8 = Reward(random.randint(0, 10), random.randint(0, 10), 'parafuso')
r9 = Reward(random.randint(0, 10), random.randint(0, 10), 'correia')
r10 = Reward(random.randint(0, 10), random.randint(0, 10), 'turbina')
r11 = Reward(random.randint(0, 10), random.randint(0, 10), 'gps')
r12 = Reward(random.randint(0, 10), random.randint(0, 10), 'memoria')
r13 = Reward(random.randint(0, 10), random.randint(0, 10), 'moeda')
r14 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r15 = Reward(random.randint(0, 10), random.randint(0, 10), 'grampo')
r16 = Reward(random.randint(0, 10), random.randint(0, 10), 'motolia')
r17 = Reward(random.randint(0, 10), random.randint(0, 10), 'parafuso')
r18 = Reward(random.randint(0, 10), random.randint(0, 10), 'turbina')
r19 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')
r20 = Reward(random.randint(0, 10), random.randint(0, 10), 'gasolina')


Rewards = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
R2D2 = Robot(random.randint(0, 10), random.randint(0, 10))

for i in range(10):

    moviment = input("Digite up, down, left or rigth para movimento: ")
    if moviment == 'up':
        R2D2.move_up()
    elif moviment == 'down':
        R2D2.move_down()
    elif R2D2.move_left():
        R2D2.move_left()
    elif moviment == 'rigth':
        R2D2.move_rigth()
    else:
        print('Movimento Inválido')
        continue
    print(R2D2)
    R2D2.check_reward(Rewards)

"""
print(r1)
print(r2.__repr__())
print(Rewards)
"""

