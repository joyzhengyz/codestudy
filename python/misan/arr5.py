p = []
n = 5
for i in 'abcde':
    for j in 'abcde':
        if i == j:
            continue;
        s = i+j
        p.append(s)
p = ['ab','ac','ad','ae','bc','bd','be','cd','ce','de']
print len(p)
for i1 in p:
    for i2 in p:
        for i3 in p:
            for i4 in p:
                for i5 in p:
                    t = set()
                    t.add(i1)
                    t.add(i2)
                    t.add(i3)
                    t.add(i4)
                    t.add(i5)
                    if len(t) != n:
                        continue
                    s = i1 + i2 + i3 + i4 + i5
                    s1 = list(s)
                    if sorted(s1) !=  list('aabbccddee'):
                        continue;
                    l = []
                    l.append(i1)
                    l.append(i2)
                    l.append(i3)
                    l.append(i4)
                    l.append(i5)
                    print l




