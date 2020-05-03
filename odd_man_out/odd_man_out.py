"""
Input
    The first line of input gives the number of cases, N.
    N test cases follow. For each test case there will be:
        - One line containing the value G, the number of guests.
        - One line containing a space-separated list of G integers.
          Each integer C indicates the invitation code of a guest.
    You may assume that 1≤N≤50,0<C<231,3≤G<1000

Output
    For each test case, output one line containing
    “Case #x: ” followed by the number C of the guest who is alone.
"""
n = int(input())
found=set()
for i in range(n):
    # There may be optimization around knowing G,
    # but since Sets do not allow an initial size
    # I could not think of any. If they did, we
    # eliminate set resize time (should the set
    # initial list size be exceeded).
    input()
    # Iterating through the list of codes,
    # we are operating under the assumption that
    # only two occurrences of any number can appear
    for c in input().split(' '))
        # Add new elements to a set
        if c in found:
            found.discard(c)
        # Delete duplicate elements from the set
        else:
            found.add(c)
    # Since the only item without a duplicate is the
    # solution, and we deleted all duplicates, popping
    # the found set should return the solution AND empty
    # the set for the next loop
    print(f"Case #{i+1}: {int(found.pop())}")
