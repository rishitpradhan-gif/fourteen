from coloring import matchings, orient
from collections import deque
from pathlib import Path
import json

for n in [5,7,9,11]:
 count=0
 for q in range(n):
  for m in matchings(tuple(i for i in range(n) if i!=q)):
   orient(n,q,m);count+=1
 print('orientations',n,count,flush=True)

# Independent breadth-first shortest attacking win on the sharpness instance.
w,h,q=7,5,3;columns=((0,4),(1,5),(2,6));pairs=[(r*w+q,(r+1)*w+q) for r in range(1,h,2)]
for a,b in columns:
 pairs.append((a,b))
 for c in [a,b]:pairs.extend((r*w+c,(r+1)*w+c) for r in range(1,h,2))
mate={u:v for a,b in pairs for u,v in [(a,b),(b,a)]}
lines=[]
for r in range(h):
 for c in range(w):
  for dc,dr in [(1,0),(0,1),(1,1),(1,-1)]:
   if 0<=c+3*dc<w and 0<=r+3*dr<h:lines.append(sum(1<<((r+i*dr)*w+c+i*dc) for i in range(4)))
def won(b):return any(b&m==m for m in lines)
start=(1<<q,0);todo=deque([(start,0,[])]);seen={start};hist={}
while todo:
 (a,b),depth,path=todo.popleft();hist[depth]=hist.get(depth,0)+1;occ=a|b
 for c in range(w):
  r=0
  while r<h and occ>>(r*w+c)&1:r+=1
  if r==h:continue
  x=r*w+c;bb=b|1<<x
  if won(bb):
   result=dict(status="passed",earliest_second_player_win_ply=2*depth+2,witness_columns_zero_based=path+[c],discovered_states=len(seen),expanded_by_completed_rounds=hist,path_coloring_cases=11460)
   assert result["earliest_second_player_win_ply"]==14
   print(json.dumps(result,indent=2))
   Path("evidence").mkdir(exist_ok=True)
   Path("evidence/verification.json").write_text(json.dumps(result,indent=2)+"\n")
   raise SystemExit(0)
  y=mate[x];assert not(occ>>y&1);assert y<w or (occ|1<<x)>>(y-w)&1
  aa=a|1<<y
  if won(aa):continue
  state=(aa,bb)
  if state not in seen:seen.add(state);todo.append((state,depth+1,path+[c]))
raise RuntimeError('No win')
