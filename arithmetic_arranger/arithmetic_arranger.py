import re
p = r"(?P<op1>\d+)\s(?P<opi>[+-])\s(?P<op2>\d+)"


def arithmetic_arranger(problems: list, calc=False):
    def is_digit(s: str):
        is_d = False
        m = re.search(r'\d+', s)
        if m:
            return True
        return is_d

    def eq4(t: str):

        return len(t) == 4

    def show(l: list, calc=False):
        s = ""
        if not calc:
            for k in range(3):
                for i in range(len(l)):
                    s += l[i][k]+" "*4
                s += '\n'
        else:

            for k in range(4):
                for i in range(len(l)):
                    s += l[i][k]+" "*4
                s += '\n'
        return s

    def getResultProblem(op1: str, op2: str, opi: str, calculate=False):

        a = (6-len(op1))*" "+str(op1)+"\n" + \
            str(opi)+(6-(len(op2)+1))*" "+str(op2)
        a += "\n"
        a += "-"*6
        if calculate:
            a += "\n"
            x = " "*(6-(len(str(eval((str(op1)+str(opi)+str(op2)))))))
            a += str(x)+str(eval(str(op1)+str(opi)+str(op2)))
        return a
    if isinstance(problems, list):
        x = ""
        if(len(problems) >= 5):
            return "Error: Too many problems."
        for i, k in enumerate(problems):
            ss = k.split(' ')

            if len(ss) == 3:
                if ss[1] not in ['-', '+']:
                    return "Error: Operator must be '+' or '-'."
                if not (is_digit(ss[0]) and is_digit(ss[2])):
                    return "Error: Numbers must only contain digits."
                if not eq4(ss[0]) and eq4(ss[2]):
                    return "Error: Numbers cannot be more than four digits."
                x += getResultProblem(ss[0], ss[2], ss[1], calculate=calc)
                x += '#'
        s = [i.split('\n') for i in x.split('#')]
        s.pop()

    else:
        print('Error')

    return show(s, calc)
