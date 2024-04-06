inf = open("input1b.txt", "r")
outf = open("output1b.txt", "w")
v, e = list(map(int, inf.readline().strip().split()))
ad_l = [[] for i in range(v+1)]
visit = [0 for i in range(v+1)]
visit_cycle = [0 for i in range(v+1)]
indgree = [0 for i in range(v+1)]


def BFS_tplgcl_srt(ad_l, indgree):
    queue = []
    for i in range(1, (v+1)):
        if indgree[i] == 0:
            queue.append(i)
    rslt = []
    while queue:
        temp = queue.pop(0)
        rslt.append(temp)
        for ad_nd in ad_l[temp]:
            indgree[ad_nd] -= 1
            if indgree[ad_nd] == 0:
                queue.append(ad_nd)

    return rslt

def cycle_dtct(selected):
    visit_cycle[selected] = 1
    for ad_nd in ad_l[selected]:
        if visit_cycle[ad_nd] == 0:
            Got_Cycle = cycle_dtct(ad_nd)
            if(Got_Cycle):
                return True
        elif visit_cycle[ad_nd] == 1:
            return True

    visit_cycle[selected] = 2
    return False

for i in range(1, (e+1)):
    f, t = list(map(int, inf.readline().strip().split()))
    ad_l[f].append(t)
    indgree[t] += 1


cycle_exst = False
for i in range(1, v+1):
    if visit_cycle[i] == 0:
        is_Cyclic= cycle_dtct(i)
        if is_Cyclic:
            cycle_exst = True
            break

if cycle_exst:
    print("IMMPOSSIBLE", file=outf)
else:
    print(*BFS_tplgcl_srt(ad_l, indgree), file=outf)


inf.close()
outf.close()