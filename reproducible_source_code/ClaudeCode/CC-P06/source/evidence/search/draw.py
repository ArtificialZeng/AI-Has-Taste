import sys, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from slither import parse, all_solutions
rows=[l.strip() for l in open(sys.argv[1]) if l.strip()]; out=sys.argv[2]
g,clues=parse(rows); sols=sorted(all_solutions(g,clues), key=lambda s: sorted(s))
n=len(sols); R=len(rows); C=len(rows[0])
import math
cols=math.ceil((n+1)/2)
fig,axs=plt.subplots(2,cols,figsize=(3.3*cols,7.0))
axes=list(axs.flatten())
for a in axes[n+1:]: a.axis('off')
def grid(ax,title):
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title,fontsize=10)
    for (x,y) in g.vedges: ax.plot(x,y,'.',color='#888',ms=1.5)
    for (x,y),k in zip(g.cells,clues): ax.text(x+0.5,y+0.5,str(k),ha='center',va='center',fontsize=7)
grid(axes[0],f"{R}x{C} fully clued")
for i,s in enumerate(sols):
    ax=axes[i+1]; grid(ax,f"solution {i+1}")
    for e in s:
        (x1,y1),(x2,y2)=g.edges[e]; ax.plot([x1,x2],[y1,y2],color='#c0392b',lw=1.6,solid_capstyle='round')
plt.tight_layout(); plt.savefig(out,dpi=200)
print("saved",out,n,"solutions")
