from math import floor

def solution(h, q):
    p = []
    root = 2**h-1   # the top of the binary tree
    for child in q:

        # in the case that child is orphan or non-existent
        if child >= root or child <= 0: 
            p.append(-1) 
            continue

        # parent is used to track the current node being searched
        # depth is used to adjust parent correctly when moving
        parent = root
        depth = root

        while True:
            # get the children (l,r) of the current parent node
            l = parent - ((floor(depth / 2)) + 1)
            r = parent - 1

            # test if the parent has found the child
            if child in (l,r):
                p.append(int(parent))
                break

            # if not, move the parent closer to the child
            if child <= l:
                parent = l
            else: parent = r
            
            depth = floor(depth / 2)

    return p

assert solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]
assert solution(5, [19, 14, 28]) == [21, 15, 29]
