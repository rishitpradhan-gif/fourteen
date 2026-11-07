"""Constructive theorem attack and independent direct-grid replay."""
from itertools import product
from pathlib import Path
import random,json
from coloring import orient, matchings
def replay(w,h,q,columns,ks):
 pairs=[((q,r),(q,r+1)) for r in range(1,h,2)]
 for (a,b),k in zip(columns,ks):
  pairs.extend(((a,r),(b,r)) for r in range(k))
  for c in (a,b):pairs.extend(((c,r),(c,r+1)) for r in range(k,h,2))
 mate={x:y for a,b in pairs for x,y in ((a,b),(b,a))}
 moves=None
 for (a,b),k in zip(columns,ks):
  if k>=3:moves=[a]*4;break
 if moves is None:
  colors=orient(w,q,columns);start=max(0,min(q,w-4));target=set(range(start,start+4))
  moves=[a if colors[a]==0 else b for a,b in columns if a in target or b in target]+list(range(start,start+4))
 board={(q,0):1};height=[0]*w;height[q]=1
 def won(player):
  return any(all(board.get((c+i*dc,r+i*dr))==player for i in range(4)) for (c,r),owner in board.items() if owner==player for dc,dr in ((1,0),(0,1),(1,1),(1,-1)))
 for j,c in enumerate(moves):
  x=(c,height[c]);assert x[1]<h
  board[x]=2;height[c]+=1
  if won(2):return 2*j+2
  y=mate[x];assert y not in board and y[1]==height[y[0]]
  board[y]=1;height[y[0]]+=1;assert not won(1)
 raise AssertionError('No win')
if __name__=='__main__':
 count=0;hist={}
 assert replay(7,5,3,((0,4),(1,5),(2,6)),(1,1,1))==14
 for h in (5,7,9):
  for q in range(5):
   for columns in matchings(tuple(c for c in range(5) if c!=q)):
    for ks in product(range(1,h+1,2),repeat=2):
     ply=replay(5,h,q,columns,ks);assert ply<=14
     count+=1;hist[ply]=hist.get(ply,0)+1
 rng=random.Random(20261107)
 for _ in range(2000):
  w=rng.randrange(2,51)*2+1;h=rng.randrange(2,11)*2+1;q=rng.randrange(w)
  cols=[c for c in range(w) if c!=q];rng.shuffle(cols);columns=tuple(zip(cols[::2],cols[1::2]))
  ks=tuple(1 if _<500 else rng.randrange((h+1)//2)*2+1 for unused in columns)
  ply=replay(w,h,q,columns,ks);assert ply<=14
  count+=1;hist[ply]=hist.get(ply,0)+1
 result=dict(status='passed',grid_replays=count,exhaustive_width=5,exhaustive_heights=[5,7,9],random_cases=2000,random_seed=20261107,win_ply_histogram=hist)
 Path('evidence/attack-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
