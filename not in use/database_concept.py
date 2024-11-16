a = [i for i in range(1, 10)]

file = open("store.txt", "a+")


for i in a:
    print('-------',i)
    file.writelines('-------'+str(i)+'\n')
    for j in a:
        b = (j!=i)
        if b:
            print('|_',j)
            file.writelines('|_'+str(j)+'\n')
            for k in a:
                c = (k != i) and (k != j)
                if c :
                    print('   |_',k)
                    file.writelines('   |_' +str(k)+'\n')
                    for l in a:
                        d = (l != i) and (l != j) and (l != k)
                        if d:
                            print('     |_',l)
                            file.writelines('     |_'+str(l)+'\n')
                            for m in a:
                                e = (m != i) and (m != j) and (m != k) and (m != l)
                                if e:
                                    print('       |_', m)
                                    file.writelines('       |_'+ str(m)+'\n')
                                    for n in a:
                                        f = (n != i) and (n != j) and (n != k) and (n != l) and (n != m)
                                        if f:
                                            print('          |_', n)
                                            file.writelines('          |_'+ str(n)+'\n')
                                            for o in a:
                                                g = (o != i) and (o != j) and (o != k) and (o != l) and (o != m) and ( o !=  n)
                                                if g:
                                                    print('            |_', o)
                                                    file.writelines('            |_' + str(o)+'\n')
                                                    for p in a:
                                                        h = (p != i) and (p != j) and (p != k) and (p != l) and ( p != m) and (p != n) and (p!=o)
                                                        if h:
                                                            print('               |_', p)
                                                            file.writelines('               |_'+str(p)+'\n')
                                                            for q in a:
                                                                hi = (q != i) and (q != j) and (q != k) and (q != l) and (q != m) and (q != n) and (q != o) and (q != p)
                                                                if hi:
                                                                    print('                 |_', q)
                                                                    file.writelines('                 |_'+ str(q)+'\n')


