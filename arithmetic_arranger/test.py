def getResultProblem(op1:str,op2:str,opi:str,calculate=False):
    
    a=(6-len(op1))*" "+str(op1)+"\n"+str(opi)+(6-(len(op2)+1))*" "+str(op2)
    a+="\n"
    a+="-"*6
    if calculate:
        
        a+="\n"
        x=" "*(6-(len(str(eval((str(op1)+str(opi)+str(op2)))))))
        a+=str(x)+str(eval(str(op1)+str(opi)+str(op2)))
    return a

print(getResultProblem("3","8888","+"))
print(getResultProblem("9999","9999","+",True))
print(getResultProblem("3","8","+",True))

