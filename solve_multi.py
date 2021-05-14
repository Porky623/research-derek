from sympy import Matrix, latex, simplify


def replace(s, ind, char):
    return s[:ind]+char+s[ind+1:]

# p = symbols('p')
p = 0.5
n, k = 6, 3
######
startSpots = [0, 1]
start = '0' * n
for s in startSpots:
    start = start[:s] + '2' + start[s + 1:]
adj = [(start, [])]
getIndex = {start: 0}
added_adj = set()
set_adj = {start}
while len(added_adj) < len(adj):
    startInd = len(added_adj)
    curString = adj[startInd][0]
    numZeros = curString.count('0')
    added_adj.add(curString)
    if numZeros > 2:
        numTwos = curString.count('2')
        if numTwos==1:
            ind_2 = curString.index('2')
            ind_p = (ind_2 + 1) % n
            ind_q = (ind_2 + n - 1) % n
            str_pp = replace(replace(curString, ind_2, '1'), ind_p, '2')
            str_qq = replace(replace(curString, ind_2, '1'), ind_q, '2')
            str_pq = replace(replace(replace(curString, ind_2, '1'), ind_q, '2'), ind_p, '2')
            adj[startInd] = (curString, [str_pp, str_qq, str_pq])
            if str_pp not in set_adj:
                getIndex[str_pp] = len(adj)
                adj.append((str_pp, []))
                set_adj.add(str_pp)
            if str_qq not in set_adj:
                getIndex[str_qq] = len(adj)
                adj.append((str_qq, []))
                set_adj.add(str_qq)
            if str_pq not in set_adj:
                getIndex[str_pq] = len(adj)
                adj.append((str_pq, []))
                set_adj.add(str_pq)
        else:
            x = curString.index('2')
            ind_2 = x, curString[x+1:].index('2')+x+1
            ind_p = (ind_2[0] + 1) % n, (ind_2[1]+1)%n
            ind_q = (ind_2[0]+ n - 1) % n, (ind_2[1]+n-1)%n
            str_pp = replace(replace(replace(replace(curString, ind_2[0], '1'), ind_2[1], '1'), ind_p[0], '2'), ind_p[1], '2')
            str_qq = replace(replace(replace(replace(curString, ind_2[0], '1'), ind_2[1], '1'), ind_q[0], '2'), ind_q[1], '2')
            str_pq = replace(replace(replace(replace(curString, ind_2[0], '1'), ind_2[1], '1'), ind_p[0], '2'), ind_q[1], '2')
            str_qp = replace(replace(replace(replace(curString, ind_2[0], '1'), ind_2[1], '1'), ind_q[0], '2'), ind_p[1], '2')
            adj[startInd] = (curString, [str_pp, str_qq, str_pq, str_qp])
            if str_pp not in set_adj:
                getIndex[str_pp] = len(adj)
                adj.append((str_pp, []))
                set_adj.add(str_pp)
            if str_qq not in set_adj:
                getIndex[str_qq] = len(adj)
                adj.append((str_qq, []))
                set_adj.add(str_qq)
            if str_pq not in set_adj:
                getIndex[str_pq] = len(adj)
                adj.append((str_pq, []))
                set_adj.add(str_pq)
            if str_qp not in set_adj:
                getIndex[str_qp] = len(adj)
                adj.append((str_qp, []))
                set_adj.add(str_qp)
# print(len(added_adj))
m = len(adj)
matrix_list = [[0] * (m + 1) for i in range(m)]
for ind, a in enumerate(adj):
    if a[1]:
        ind_pp = getIndex[a[1][0]]
        ind_qq = getIndex[a[1][1]]
        ind_pq = getIndex[a[1][2]]
        if len(a[1])==3:
            matrix_list[ind][ind_pq]-=2*p*(1-p)
        if len(a[1])==4:
            matrix_list[ind][ind_pq]-=p*(1-p)
            ind_qp = getIndex[a[1][3]]
            matrix_list[ind][ind_qp]-=p*(1-p)
        matrix_list[ind][ind_pp] -= p*p
        matrix_list[ind][ind_qq] -= (1 - p)*(1-p)
    matrix_list[ind][ind] += 1
    if a[0].count('0') ==2 and a[0].index('0') == k:
        matrix_list[ind][m] = 1
matrix = Matrix(matrix_list)
print(adj)
print(latex(simplify(matrix.rref()[0][0,m])))
