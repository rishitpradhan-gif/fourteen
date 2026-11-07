from itertools import combinations,product
from collections import deque
import json
from pathlib import Path

def matchings(xs):
 if not xs:yield ();return
 for j in range(1,len(xs)):
  for tail in matchings(xs[1:j]+xs[j+1:]):yield ((xs[0],xs[j]),)+tail

def protector(n,q):
 if q%2==0:return tuple([(i,i+1) for i in range(0,q,2)]+[(i,i+1) for i in range(q+1,n,2)])
 return tuple([(i,i+1) for i in range(0,q-1,2)]+[(q-1,q+1)]+[(i,i+1) for i in range(q+2,n,2)])
def orient(n,q,m):
 g=protector(n,q);adj=[set() for _ in range(n)]
 for a,b in m+g:adj[a].add(b);adj[b].add(a)
 c=[None]*n;c[q]=1
 for root in range(n):
  if c[root] is not None:continue
  c[root]=0;todo=[root]
  while todo:
   a=todo.pop()
   for b in adj[a]:
    if c[b] is None:c[b]=1-c[a];todo.append(b)
    assert c[b]!=c[a]
 assert all(len(set(c[i:i+4]))==2 for i in range(n-3))
 return c

