import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:

        self.contents = []
        for (k, i) in kwargs.items():
            setattr(self, k, i)
            for e in range(i):
                self.contents.append("%s" % k)

    def draw(self, balls):
        balls_to_dell = list()
        if balls > 0 and balls < len(self.contents):
            for k in range(balls):
                x = random.choice(self.contents)
                balls_to_dell.append(x)
                self.contents.remove(x)
            return balls_to_dell
        elif balls > 0 and balls >= len(self.contents):
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i = 0
    m = 0
    while i < num_experiments:
        balls_to_dell = hat.draw(num_balls_drawn)
        expected = []
        for k, e in expected_balls.items():
            for j in range(e):
                expected.append(k)
        for x in expected:
            if x in balls_to_dell:
                m += 1
        i += 1
    return m/num_experiments