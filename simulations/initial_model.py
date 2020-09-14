import random
# SEED=0
# random.seed(SEED)
NUMTRIALS=1000
N = 20
results=[0 for i in range(N)]
for trial in range(NUMTRIALS):
    seen={0}
    cur=0
    while len(seen)<N-1:
        cur=(cur+(-1)**random.randint(0,1)+N)%N
        seen.add(cur)
    for i in range(N):
        if i not in seen:
            results[i]+=1
print(results)