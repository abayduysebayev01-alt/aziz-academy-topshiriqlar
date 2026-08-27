# Sonlar ketma-ket kiritiladi.
# Birinchi manfiy son kelishi bilan break qiling.
# Manfiygacha kiritilgan musbat/0 sonlar sonini chiqaring.

yigindi = 0
while True:
    son = int(input())
    if son < 0:
        break
    yigindi += 1
print(yigindi)    