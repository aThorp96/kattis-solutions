"""
CD
    Jack and Jill have decided to sell some of their Compact Discs, while they 
    still have some value. They have decided to sell one of each of the CD titles 
    that they both own. How many CDs can Jack and Jill sell?
    Neither Jack nor Jill owns more than one copy of each CD.

Input
    The input consists of a sequence of test cases. The first line of each test 
    case contains two positive integers N and M, each at most one million, 
    specifying the number of CDs owned by Jack and 
    by Jill, respectively. This line is followed by N lines listing the catalog 
    numbers of the CDs owned by Jack in increasing order, and M more lines listing 
    the catalog numbers of the CDs owned by Jill in increasing 
    order. Each catalog number is a positive integer no greater than one 
    billion. The input is terminated by a line containing two zeros. This last line 
    is not a test case and should not be processed.

Output
    For each test case, output a line containing one integer, the number of CDs 
    that Jack and Jill both own.

Algorithm
    Until reading "0 0",
        read the test case indicator
        read all of Jack's CDs into a set s
        read all of Jill's CDs out of the set s
        print the result

"""
def get_n_m():
    n_m = input()
    while n_m != "0 0":
        n_m = input()
        yield n_m


for n_m in get_n_m():
    n_m = n_m.split(' ')
    print(f"n m: {n_m}")

    n = int(n_m[0])
    m = int(n_m[1])

    s = set()
    for i in range(n):
        j = input()
        s.add(j)

    a = set()
    for i in range(m):
        j = input()
        if j in s:
            a.add(j)

    print(len(a))
