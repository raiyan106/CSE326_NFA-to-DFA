#a=" "*5
#a[2]='r'
#print(int('5')-0)

class Integer:
    def __init__(self,value):
        self.value = value

    def increase(self):
        self.value+=1
    def decrease(self):
        self.value-=1

lst=[None]*5
#global a
a= Integer(-1)
i = -1
j=0
def push(z):
    #global a
    #a.increase()
    global i
    i+=1
    lst[i]=z
def pop():
    global i, j
    val = lst[i]
    #a.decrease()
    i-=1
    j+=1
    return val

push(55)
push(56)
g = pop()
#f = pop()
print(i, j)