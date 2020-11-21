import random, time

start = time.time()
# SEED=0
# random.seed(SEED)
NUMTRIALS = 50000
N = 4
results = [0 for i in range(N)]
increment = [1,2]
p=.9
for trial in range(NUMTRIALS):
    seen = {0}
    cur = 0
    while len(seen) < N-1:
        val = random.random()
        if val<p:
            cur=(cur+increment[0]) % N
        else:
            cur = (cur+increment[1]) % N
        seen.add(cur)
    for i in range(N):
        if i not in seen:
            results[i] += 1
for r in results:
    print(r/NUMTRIALS)
end = time.time()
print(end - start)
