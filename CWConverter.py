# coding:utf-8

import sys

A='/-'
B='-///'
C='-/-/'
D='-//'
E='/'
F='//-/'
G='--/'
H='////'
I='//'
J='/---'
K='-/-'
L='/-//'
M='--'
N='-/'
O='---'
P='/--/'
Q='--/-'
R='/-/'
S='///'
T='-'
U='//-'
V='///-'
W='/--'
X='-//-'
Y='-/--'
Z='--//'
n1='/----'
n2='//---'
n3='///--'
n4='////-'
n5='/////'
n6='-////'
n7='--///'
n8='---//'
n9='----/'
n0='-----'

listsignal=[]
listresult=[]
for line in open(sys.argv[1],'r'):
    listsignal=line[:-1].split(' ')

print listsignal

for text in listsignal:
    if text==A:
        listresult.append('A')
        print 'A'
    elif text==B:
        listresult.append('B')
    elif text==C:
        listresult.append('C')
    elif text==D:                                                               
        listresult.append('D') 
    elif text==E:
        listresult.append('E')
    elif text==F:
        listresult.append('F')
    elif text==G:
        listresult.append('G')
    elif text==H:
        listresult.append('H') 
    elif text==I:
        listresult.append('I') 
    elif text==J:
        listresult.append('J') 
    elif text==K:
        listresult.append('K') 
    elif text==L:
        listresult.append('L') 
    elif text==M:
        listresult.append('M')
    elif text==N:
        listresult.append('N')
    elif text==O:
        listresult.append('O') 
    elif text==P:
        listresult.append('P') 
    elif text==Q:
        listresult.append('Q') 
    elif text==R:
        listresult.append('R') 
    elif text==S:
        listresult.append('S') 
    elif text==T:
        listresult.append('T') 
    elif text==U:
        listresult.append('U') 
    elif text==V:
        listresult.append('V') 
    elif text==W:
        listresult.append('W') 
    elif text==X:
        listresult.append('X') 
    elif text==Y:
        listresult.append('Y') 
    elif text==Z:
        listresult.append('Z')
    elif text==n1:
        listresult.append('1')
    elif text==n2:
        listresult.append('2')
    elif text==n3:
        listresult.append('3')
    elif text==n4:
        listresult.append('4')
    elif text==n5:
        listresult.append('5')
    elif text==n6:
        listresult.append('6')
    elif text==n7:
        listresult.append('7')
    elif text==n8:
        listresult.append('8')
    elif text==n9:
        listresult.append('9')
    elif text==n0:
        listresult.append('0')
    else:
        listresult.append('?')

        
print '結果'
print listresult

if len(sys.argv)>2:
    f=open(sys.argv[2],'w')
else:
    f=open('CWresult.txt','w')

for list in listresult:
    f.write(list)
    f.write(' ')

f.close()
