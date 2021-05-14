import random, time

start = time.time()
# SEED=0
# random.seed(SEED)
NUMTRIALS = 50000
N = 6
p = 0.5
results = [0 for i in range(N)]
ties = [0 for i in range(N)]
for trial in range(NUMTRIALS):
    seen = {0,1}
    cur = [0,1]
    last=[0,0]
    while len(seen) < N - 1:
        cur = [(cur[i] + (-1) ** (random.random() < p) + N) % N for i in range(2)]
        last=cur
        for x in cur:
            seen.add(x)
    for i in range(N):
        if i not in seen:
            results[i] += 1
    if len(seen)==N:
        for x in last:
            ties[x]+=1
for r in results:
    print(r)
print('---------------------')
for t in ties:
    print(t)
end = time.time()
print(end - start)
