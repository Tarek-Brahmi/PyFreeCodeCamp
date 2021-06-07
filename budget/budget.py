class Category:
    def __init__(self, categorie) -> None:
        self.ledger = list()
        self.catigory = categorie

    def deposit(self, amount, description=""):
        self.ledger.append(
            {"amount": amount, "description": description}
        )

    def withdraw(self, amount, description="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        first_amont = self.ledger[0]["amount"]
        for k in self.ledger[1:]:
            first_amont += k["amount"]
        return first_amont

    def transfer(self, amount, other) -> bool:
        if self.check_funds(amount):
            self.deposit(description="Transfer to %s" %
                         (other.catigory), amount=-amount)
            other.deposit(description="Transfer from %s" %
                          (self.catigory), amount=-amount)
            return True
        else:
            return False

    def check_funds(self, amount):
        result = False
        if amount < self.get_balance():
            result = True
        return result

    def __repr__(self):
        x = self.catigory.center(23, "*")+"\n"
        for k in self.ledger:
            y = 23-(len(str(k["amount"]))+len(str(k["description"])))
            if (y <= 0):
                x += "%s" % (str(k["description"])[:23]
                             [:22-len(str(float(k["amount"])))])
                x += " "
            else:
                x += "%s" % (str(k["description"]))
                x += " "*(y)
            x += "%.2f\n" % (float(k["amount"]))
        x += "Total: %.2f\n" % (self.get_balance())
        return x


def create_spend_chart(categories):
    x = "Percentage spent by category\n"
    c_names = [c.catigory for c in categories]

    c_percenteg = []
    for k in categories:
        p = 0

        if(len(k.ledger[1:])) > 1:
            for i in k.ledger[1:]:
                p += abs(i['amount'])
            c_percenteg.append(
                int(round(
                    (k.ledger[0]['amount']-k.get_balance()
                     )//len(k.ledger[1:])//100
                ))
            )
        else:
            if (len(k.ledger)) == 1:
                p += abs(k.ledger[0]['amount'])
                c_percenteg.append(
                    int(round(
                        (k.ledger[0]['amount']-k.get_balance()
                         )//100
                    ))
                )
    print(c_percenteg)
    y = ' '*4+'---'*len(c_names)+"-\n"
    z = "     "

    def show_catigories(names: list):
        w = max([len(i) for i in names])
        for k in range(len(names)):
            s = list()
            s.extend(names[k])
            if len(s) < w:
                for i in range(w-len(s)):
                    s.append(' ')
            names[k] = s

    def make_oos(length: list, maxx=11):
        for k in range(len(length)):
            s = list()
            s.extend("o"*(length[k]+1))
            if len(s) < maxx:
                for i in range(maxx-len(s)):
                    s.append(' ')
            length[k] = s[::-1]

    make_oos(c_percenteg)
    show_catigories(c_names)

    f = ""
    for e in range(len(c_percenteg[0])):
        g = '%d' % (100-e*10)
        f += " "*(3-len(g))+g+"|"
        for l in range(len(c_percenteg)):
            f += ' %c ' % (c_percenteg[l][e])
        f += '\n'

    x += f
    x += y  # seppp
    for k in range(len(c_names[0])):
        x += z
        for i in range(len(c_names)):
            x += ' %c ' % (c_names[i][k])
        x += "\n"
    return x


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(505.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(business)
print(food)
print(entertainment)
actual = create_spend_chart([business, food, entertainment])
print(actual)
