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
    'tranlist':[tran for i in range(STATES)]
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
    val = stackA[Aptr]
    Aptr-=1
    return val

def copy(i):
    temp=[None]*(STATES+1)
    temp[0]=" "
    k=0
    Bptr=-1
    temp = list(Dstates[i]['StateString'])
    while(temp[k] is not None):
        pushB(int(temp[k])-'0')
        k+=1


def popB():
    val = stackB[Bptr]
    Bptr-=1
    return val

def peekB():
    return stackA[Bptr]

def peekA():
    return stackA[Aptr]

def seek(arr,ptr,s):
    for i in range(ptr+1):
        if s==arr[i]:
            return 1
    return 0

def sort():
    tempo=None
    for i in range(Bptr):
        for j in range(Bptr-1):
            if stackB[j]>stackB[j+1]:
                tempo=stackB[j]
                stackB[j]=stackB[j+1]
                stackB[j+1]=tempo

def toString():
    sort();
    for i in range(Bptr+1):
        temp[i]=str(stackB[i])
    temp[i]=None

def display_DTran():
    print("\n\t\t DFA Transition Table ")
    print("\n\t\t ---------------------")
    print("\nStates\tString\tInputs\n ")
    for i in range(noi):
        print("\t{}".format(inp[i]))
    print("\n \t------------------")

    for i in range(nods):
        if(Dstates[i]['is_final']==0):
            print("\n{}".format(Dstates[i]['name']))
        else:
            print("\n*{}".format(Dstates[0]['name']))
        
        print("\t{}".format(Dstates[i]['StateString']))

        for j in range(noi):
            print("\t{}".format(Dstates[i]['trans'][j]))
    
    print("\n")

def move(st,j):
    ctr=0
    while(ctr<States[st]['tranlist'][j]['notran']):
        pushA(States[st]['tranlist'][j]['tostates'][ctr])
        ctr+=1


def lambda_closure(st):
    ctr = 0
    in_state=st
    curst = st
    chk = None
    while(Aptr!=-1):
        curst = popA()
        ctr = 0
        in_state = curst
        while(ctr<=States[curst]['tranlist'][noi]['notran']):
            chk = seek(stackB,Bptr,in_state)
            if(chk==0):
                pushB(in_state)
            in_state = States[curst]['tranlist'][noi]['tostates'][ctr]
            ctr+=1
            chk = seek(stackA,Aptr,in_state)
            if(chk==0 and ctr<=States[curst]['tranlist'][noi]['notran']):
                pushA(in_state)