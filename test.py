def c1(x, y):
    i = str(-x) + " " + str(y) + " 0"
    return i

def c2(x, y, z):
    i = str(x) + " " + str(-y) + " " + str(-z) + " 0"
    return i

def c3(x, y):
    i = str(-x) + " " + str(-y) + " 0"
    return i

def c4(x, y):
    i = str(x) + " " + str(y) + " 0"
    return i

ns0 = 1
ns1 = 2
s0 = 3
s1 = 4
in0 = 5

k = 85

i = 1

with open('d.cnf', 'w') as f:
    f.write("c  d.cnf\n")
    f.write("c  question3.2.3\n")
    f.write("c  BUID is U85845640")
    
    f.write("c\n")
    if (k > 0):
        f.write("p cnf " + str(5+3*(k-1)) + " " + str(9+5*(k-1)) + "\n")
        while (i <= k):
            if (i>1):
                s0 = ns0
                s1 = ns1
            ns0 = ns0 + 5
            ns1 = ns1 + 5
            in0 = in0 + 3
            f.write(c1(ns1, in0) + "\n")
            f.write(c1(ns1, s0) + "\n")
            f.write(c2(ns1, in0, s0) + "\n")
            f.write(c3(ns0, in0) + "\n")
            f.write(c4(ns0, in0) + "\n")
            i = i+1
        f.write("-3 0\n")
        f.write("-4 0\n")
        f.write(str(-ns0) + " 0\n")
        f.write(str(ns1) + " 0\n")
    else:
        f.write("p cnf 5 9\n")
        f.write(c1(ns1, in0) + "\n")
        f.write(c1(ns1, s0) + "\n")
        f.write(c2(ns1, in0, s0) + "\n")
        f.write(c3(ns0, in0) + "\n")
        f.write(c4(ns0, in0) + "\n")


