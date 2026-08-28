# n beriladi.
# while bilan 1..n yurib, juft sonlarni sanang.
# 3 ta juft son topilishi bilan break qiling.
# Nechanchi son (i) da to‘xtaganingizni chiqaring.
# Agar 3 ta juft son topilmasa, "No" chiqaring.

n = int(input())
yigindi = 0
found = False
for i in range(1, n + 1):
    if i % 2 == 0:
        yigindi += 1
        if yigindi == 3:
            print(i)
            found = True
            break
if not found:
    print("No")