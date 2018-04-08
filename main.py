#DState Structure
STATES = 50

Dstate={
    'name':None,
    'StateString':[None]*(STATES+1),
    'trans':[None]*10,
    'is_final':None
}

#List of Dstate
Dstates=[Dstate for i in range(STATES)]

#tran Structure
tran={
    'sym':None,
    'tostates':[None]*STATES,
    'notran':None
}

#state Structure
state={
    'no':None,
    tranlist=[tran for i in range(STATES)]
}

stackA = [None]*100
stackB = [None]*100
C = [None]*100
Cptr=-1
Aptr=-1
Bptr=-1

States = [state for i in range(STATES)]
temp = [None]*(STATES+1)
inp = [None]*10
nos=noi=nof=j=k=nods=-1

def pushA(z):
    Aptr+=1
    stackA[Aptr]=z

def pushB(z):
    Bptr+=1
    stackB[Bptr]=z

def popA():
    Aptr=Aptr-1
    return stackA[Aptr]

def copy(i):
    
