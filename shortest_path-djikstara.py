import graphviz as gv
import matplotlib
matplotlib.use('qt4agg')
import functools 
from matplotlib import pyplot as pt
from matplotlib import image as im


class node:
    def __init__(self,**kwargs):
        if list(kwargs.keys())[0]!='apex':
            self.distance=kwargs
            self.path_d=float("inf")            
        else:
            self.distance=None
            self.path_d=float("inf")
        



list_nodes={}
flag='y'
while(flag!='n'):
    name,weight=input('enter info').split()    
    if weight != '0' :
        list_nodes[name]=eval('node('+weight+')')
    else:
        list_nodes[name]=node(apex='T')        
    flag=input('continue?')

g1=gv.Digraph(format='png')
for i in list_nodes:
    g1.node(i)


for k,v in list_nodes.items(): 
    try:
        [g1.edge(k,x,str(v.distance[x])) for x in v.distance]
    except:
         continue
g1.render('img/ff')

nodes_found={}
nodes_left=list_nodes.copy()
source='a'
start=source
nodes_left[source].path_d=0

def add_vertex():
    node=min(nodes_left,key=lambda x: nodes_left[x].path_d)
    nodes_found[node]=nodes_left[node]
    del nodes_left[node]    
    return node

def update_distance(node):
    for k in nodes_left:
        try:            
            d=nodes_found[node].distance[k]+nodes_found[node].path_d
            if d<nodes_left[k].path_d:
                nodes_left[k].path_d=d
        except KeyError:
            continue

    
while (nodes_left):
    node=add_vertex()
    update_distance(node)
   
      

   
        

    
    
