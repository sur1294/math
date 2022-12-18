def frequency(l):
    count = {}
    for n in l:
        if n in count.keys():
            count[n] = count[n]+1
        else:
            count[n] = 1
    minlist = findmin(count)
    maxlist = findmax(count)
    return((minlist,maxlist))

def findmin(d):
    upperbound = 0
    for n in d.keys():
        if d[n] > upperbound:
            upperbound = d[n]

    minlist = []
    mincount = upperbound

    for n in d.keys():
        if d[n] < mincount:
            minlist = [n]
            mincount = d[n]
        elif d[n] == mincount:
            minlist.append(n)
    return(sorted(minlist))

            
def findmax(d):
    maxlist = []
    maxcount = 0

    for n in d.keys():
        if d[n] > maxcount:
            maxlist = [n]
            maxcount = d[n]
        elif d[n] == maxcount:
            maxlist.append(n)
    return(sorted(maxlist))
