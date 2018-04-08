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
nos=None
noi=None
nof=None
nods=-1

#global nos, noi, nof, nods

def pushA(z):
    global Aptr
    Aptr+=1
    stackA[Aptr]=z

def pushB(z):
    global Bptr
    Bptr+=1
    stackB[Bptr]=z

def popA():
    global Aptr
    val = stackA[Aptr]
    Aptr-=1
    return val

def copy(i):
    global Bptr
    temp=[None]*(STATES+1)
    temp[0]=" "
    k=0
    Bptr=-1
    temp = list(Dstates[i]['StateString'])
    while(temp[k] is not None):
        pushB(int(temp[k])-'0')
        k+=1


def popB():
    global Bptr
    val = stackB[Bptr]
    Bptr-=1
    return val

def peekB():
    global Bptr
    return stackA[Bptr]

def peekA():
    global Aptr
    return stackA[Aptr]

def seek(arr,ptr,s):
    for i in range(ptr+1):
        if s==arr[i]:
            return 1
    return 0

def sort():
    global Bptr
    tempo=None
    for i in range(Bptr):
        for j in range(Bptr-i):
            if stackB[j]>stackB[j+1]:
                tempo=stackB[j]
                stackB[j]=stackB[j+1]
                stackB[j+1]=tempo

def toString():
    global Bptr
    sort();
    for i in range(Bptr+1):
        temp[i]=str(stackB[i])
    temp[i+1]=None

def display_DTran():
    global Aptr
    global Bptr
    global nos, noi, nof, nods

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
    global Aptr
    global Bptr
    global nos, noi, nof, nods
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

#Main Code

print("\tNFA TO DFA CONVERTION\n\n")
final=[None]*20
fin = 0
c = None
ans = None
st = [None]*20

nos = input("Enter no. of States in NFA : ")
nos = int(nos)

for i in range(nos):
    States[i]['no']=i

start = input("Enter the start state : ")
start = int(start)

nof = input("Enter the number of final state : ")
nof = int(nof)

print("\nEnter the final state : \n")
'''
for i in range(nof):
    val = input()
    final[i] = int(val)
'''
final=map(int,input().split())
final=list(final)
noi = input("\nEnter the number of input symbols : ")
noi = int(noi)

print("\nEnter the input symbols : \n")
'''
for i in range(noi):
    val = input()
    inp[i] = val
inp[i+1]='e'
'''
inp=map(str,input().split())
inp=list(inp)
inp.append('e')

print("\nEnter the transitions : (-1 to stop)\n")
for i in range(nos):
    for j in range(noi):
        States[i]['tranlist'][j]['sym']=inp[j]
        k=0
        ans='y'
        while(ans=='y'):
            val = input("move({}, {}) : ".format(i,inp[j]))
            val = int(val)
            States[i]['tranlist'][j]['tostates'][k] = val
            k+=1
            if(States[i]['tranlist'][j]['tostates'][k-1]==-1):
                k-=1
                ans='n'
                break
        
        States[i]['tranlist'][j]['notran'] = k

i=nods=fin=0
pushA(start)
lambda_closure(peekA())
toString()
Dstates[nods]['name']='A'
nods+=1
Dstates[0]['StateString'] = list(temp)

while(i<nods):
    for j in range(noi):
        fin = 0
        copy(i)
        while(Bptr!=-1):
            move(popB(),j)
        while(Aptr!=-1):
            lambda_closure(peekA())
        toString()
        for k in range(nods):
            if temp==Dstates[k]['StateString']:
                Dstates[i]['trans'][j] = Dstates[k]['name']
                break
        
        if k==nods:
            nods+=1
            for k in range(nof):
                fin = seek(stackB,Bptr,final[k])
                if fin==1:
                    Dstates[nods-1]['is_final'] = 1
                    break
            
            Dstates[nods-1]['StateString'] = list(temp)
            convert = ord('A')
            convert=convert+(nods-1)
            convert=chr(convert)
            Dstates[nods-1]['name'] = convert
            Dstates[i]['trans'][j] = Dstates[nods-1]['name']
    
    i=i+1

display_DTran()


