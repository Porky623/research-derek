from sympy import *

p = symbols('p')
n, k = 5,4
######
start = '2' + '0' * (n - 1)
adj = [(start, [])]
getIndex = {start: 0}
added_adj = set()
set_adj = {start}
while len(added_adj) < len(adj):
    startInd = len(added_adj)
    curString = adj[startInd][0]
    numZeros = curString.count('0')
    added_adj.add(curString)
    curInd = startInd
    if numZeros != 1:
        ind_2 = curString.index('2')
        ind_p = (ind_2 + 1) % n
        ind_q = (ind_2 + 2) % n
        str_p = curString[:ind_2] + '1' + curString[ind_2 + 1:]
        str_p = str_p[:ind_p] + '2' + str_p[ind_p + 1:]
        str_q = curString[:ind_2] + '1' + curString[ind_2 + 1:]
        str_q = str_q[:ind_q] + '2' + str_q[ind_q + 1:]
        adj[curInd] = (curString, [str_p, str_q])
        if str_p not in set_adj:
            getIndex[str_p] = len(adj)
            adj.append((str_p, []))
            set_adj.add(str_p)
            curInd += 1
        if str_q not in set_adj:
            getIndex[str_q] = len(adj)
            adj.append((str_q, []))
            set_adj.add(str_q)
            curInd += 1
    else:
        curInd += 1
# print(len(added_adj))
m = len(adj)
matrix_list = [[0] * (m + 1) for i in range(m)]
for ind,a in enumerate(adj):
    if a[1]:
        ind_p = getIndex[a[1][0]]
        ind_q = getIndex[a[1][1]]
        matrix_list[ind][ind_p] -= p
        matrix_list[ind][ind_q] -= 1-p
    matrix_list[ind][ind] += 1
    if a[0].count('0') == 1 and a[0].index('0') == k:
        matrix_list[ind][m] = 1
matrix = Matrix(matrix_list)
print(adj)
print(latex(simplify(matrix.rref()[0][0,m])))