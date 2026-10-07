from pathlib import Path
from collections import defaultdict
import csv, json, math
BASE = Path(__file__).resolve().parent

def auroc(rows, score):
    pos = sum(int(r['label']) for r in rows); neg = len(rows)-pos
    grouped = defaultdict(lambda:[0,0])
    for r in rows: grouped[float(r[score])][int(r['label'])] += 1
    lower_neg = 0; numerator = 0.0
    for value in sorted(grouped):
        n,p = grouped[value]; numerator += p*(lower_neg+0.5*n); lower_neg += n
    return numerator/(pos*neg)

def ap(rows, score):
    pos=sum(int(r['label']) for r in rows); grouped=defaultdict(lambda:[0,0])
    for r in rows: grouped[float(r[score])][int(r['label'])]+=1
    seen=0; captured=0; result=0.0
    for value in sorted(grouped,reverse=True):
        n,p=grouped[value]; seen+=n+p;captured+=p
        result += (p/pos)*(captured/seen)
    return result

results=[]
for p in sorted((BASE/'data').glob('B2_*.csv')):
    with p.open() as f: rows=list(csv.DictReader(f))
    metrics={}
    for score in ['terrain_landcover','terrain_landcover_ae']:
        ordered=sorted(rows,key=lambda r:(-float(r[score]),r['sample_id']))
        metrics[score]={'AUROC':auroc(rows,score),'AP':ap(rows,score),
                        'captured_at_20pct':sum(int(r['label']) for r in ordered[:math.ceil(.20*len(rows))])}
    result={'variant':rows[0]['variant'],'N':len(rows),'K':math.ceil(.20*len(rows)),
            'traces':sum(int(r['label']) for r in rows),'metrics':metrics}
    results.append(result)
print(json.dumps(results,indent=2))
