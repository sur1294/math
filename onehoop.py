def onehop(l):
    direct = {}
    for (i,j) in l:
        if i in direct.keys():
            direct[i].append(j)
        else:
            direct[i] = [j]

    hopping = []

    for src in direct.keys():
        for dest in direct[src]:
            if dest in direct.keys():
                for remote in direct[dest]:
                    if src != remote:
                        hopping.append((src,remote))

    return(remdup(sorted(hopping)))
            
def remdup(l):
    if len(l) < 2:
        return(l)

    if l[0] != l[1]:
        return(l[0:1]+remdup(l[1:]))
    else:
        return(remdup(l[1:]))