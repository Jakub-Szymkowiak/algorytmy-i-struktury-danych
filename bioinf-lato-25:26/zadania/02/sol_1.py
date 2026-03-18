A = [1, 2, 2, 5, 8]

out = True
i = 0

while i < len(A) - 1:
    if A[i] > A[i + 1]:
        out = False
        break
    i += 1

print(out)