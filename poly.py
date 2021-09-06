# !/usr/bin/env -S python3 -i
# !/opt/SageMath/src/bin/sage-python -i
#!/usr/bin/env -S sage --python -i

import sys
import os
sys.path.insert(0,'/opt/SageMath/local/lib/python3.9/site-packages')
os.environ['PATH']+='/opt/SageMath/local/bin'
from sage.all import *

# P=polytopes.icosahedron()

p=(1+sqrt(5))/2
q=p-1
r=(2*p-1)/sqrt(5*(p+2))
s=(p+2)/sqrt(5*(p+2))

p=p.n()/2
q=q.n()/2
e=1/2.0

r=r.n()
s=s.n()

S0=[[0,0,2*e],[0,0,-2*e],[0,2*e,0],[0,-2*e,0],[2*e,0,0],[-2*e,0,0]]
S1=[[+e,+p,+q],[+e,+p,-q],[+e,-p,+q],[+e,-p,-q],[-e,+p,+q],[-e,+p,-q],[-e,-p,+q],[-e,-p,-q]]
S2=[[+p,+q,+e],[+p,+q,-e],[+p,-q,+e],[+p,-q,-e],[-p,+q,+e],[-p,+q,-e],[-p,-q,+e],[-p,-q,-e]]
S3=[[+q,+e,+p],[+q,+e,-p],[+q,-e,+p],[+q,-e,-p],[-q,+e,+p],[-q,+e,-p],[-q,-e,+p],[-q,-e,-p]]
S4=[[0,+s,+r],[0,+s,-r],[0,-s,+r],[0,-s,-r]]
S5=[[+r,0,+s],[+r,0,-s],[-r,0,+s],[-r,0,-s]]
S6=[[+s,+r,0],[+s,-r,0],[-s,+r,0],[-s,-r,0]]
S=S0+S1+S2+S3+S4+S5+S6

def prod(l1,l2):
    return l1[0]*l2[0]+l1[1]*l2[1]+l1[2]*l2[2]
T=[]
for l in S:
    if prod(l,[r,0,s]) >= -0.0001:
        T+=[l]

print('Radius        :', 1)
print('Regular   Edge:', 2*p-1)
print('Irregular Edge:', sqrt(2.0)*sqrt(1.0-sqrt((2*p+1)/(2*p+2))))

# P=Polyhedron(vertices=[[0,0,0],[0,0,2*e],[q,e,p],[q,-e,p],[p,q,e],[p,-q,e],[r,0,s]])
# ,[-r,0,s],[r,0,-s],[-r,0,-s],[s,r,0],[-s,r,0],[s,-r,0],[-s,-r,0],[0,s,r],[0,-s,r],[0,s,-r],[0,-s,-r]])
P=Polyhedron(vertices=T)
P.plot(frame=false)
