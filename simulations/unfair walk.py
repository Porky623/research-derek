import random, time

start = time.time()
# SEED=0
# random.seed(SEED)
NUMTRIALS = 50000
N = 20
p = 0.55
results = [0 for i in range(N)]
for trial in range(NUMTRIALS):
    seen = {0}
    cur = 0
    while len(seen) < N - 1:
        cur = (cur + (-1) ** (random.random() < p) + N) % N
        seen.add(cur)
    for i in range(N):
        if i not in seen:
            results[i] += 1
for r in results:
    print(r)
end = time.time()
print(end - start)
    