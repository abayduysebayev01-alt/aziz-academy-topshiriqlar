# n beriladi.
# i=1 dan boshlang.
# 7 ga karrali son topilishi bilan break qiling va o‘sha sonni chiqaring.
# Agar 1..n ichida yo‘q bo‘lsa, "No" chiqaring.

n = int(input())
found = False
i = 1
while i <= n:
    if i % 7 == 0:
        print(i)
        found = True
        break
    i += 1
if not found:
    print("No")