import pandas as pd
a={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
A=pd.DataFrame(a,columns=['Student','Math'])
b={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
B=pd.DataFrame(b,columns=['Student','Electronics'])
c={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
C=pd.DataFrame(c,columns=['Student','GEAS'])
d={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
D=pd.DataFrame(d,columns=['Student','ESAT'])
E=pd.merge(A,B)
F=pd.merge(E,C)
G=pd.merge(F,D)
H=pd.melt(G,id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
I=H.rename(columns={'variable':'Subject','value':'Grades'})
J=I.sort_values('Student')
K=J.reset_index()
LongFormat=K.drop(columns=['index'])