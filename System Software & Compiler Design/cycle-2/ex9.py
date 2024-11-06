class Operation:
    def __init__(self, left, right):
        self.left = left
        self.right = right
n = int(input("Enter the Number of Values: "))
ops = [Operation(input("left: "), input("\tright: ")) for _ in range(n)]
print("\nIntermediate Code")
for op in ops:
    print(f"{op.left} = {op.right}")
pr = []
for i in range(n - 1):
    temp = ops[i].left
    if any(temp in op.right for op in ops):
        pr.append(Operation(ops[i].left, ops[i].right))
pr.append(Operation(ops[n - 1].left, ops[n - 1].right))
print("\nAfter Dead Code Elimination\n")
for op in pr:
    print(f"{op.left}\t= {op.right}")
for m in range(len(pr)):
    tem = pr[m].right
    for j in range(m + 1, len(pr)):
        if pr[j].right in tem:
            t = pr[j].left
            pr[j].left = pr[m].left
            for i in range(len(pr)):
                if t in pr[i].right:
                    a = pr[i].right.index(t)
                    pr[i].right = pr[i].right[:a] + pr[m].left + pr[i].right[a + 1:]

print("\nEliminate Common Expression")
for op in pr:
    print(f"{op.left}\t= {op.right}")
optimized_pr = []
for i in range(len(pr)):
    if any(op.left == pr[i].left and op.right == pr[i].right for op in optimized_pr):
        continue
    optimized_pr.append(pr[i])
print("\nOptimized Code")
for op in optimized_pr:
    print(f"{op.left} = {op.right}")