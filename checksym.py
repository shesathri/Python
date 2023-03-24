def checkrow(lis, n):
    if sum(lis[-1]) != n:
        return False
    return True


def checkcol(lis, n):
    sum1 = 0
    for i in range(len(lis)):
        sum1 += lis[i][-1]
    if sum1 != n:
        return False
    return True


def checkdia(lis, n):
    sum1 = 0
    sum2 = 0
    for i in range(len(lis)):
        sum1 += lis[i][i]
        sum2 += lis[i][len(lis) - i - 1]
    if sum1 != n or sum2 != n:
        return False
    return True


def checkmat(lis):
    val = sum(lis[0])
    row = checkrow(lis, val)
    col = checkcol(lis, val)
    dia = checkdia(lis, val)
    return row and col and dia


m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

if m == n:
    mat = []
    for i in range(m):
        mat.append(list(map(int, input("Enter the elements of row %d: " % i).split())))
    if checkmat(mat):
        print("Magic matrix")
    else:
        print("Not a magic matrix")
else:
    print("\nInvalid matrix")

print("Hih helo!!")
print("bye")
print("Hih helo!!")
print("bye")
print("Hi by shesathri")
