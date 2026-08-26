# Sonlar ketma-ket kiritiladi (har qatorda bitta).
# 0 kiritilganda to‘xtang.
# O‘rtacha qiymatni chiqaring.
# Agar 0 birinchi bo‘lsa, 0 chiqaring.
# Eslatma: o‘rtacha butun bo‘lsa ham float chiqishi mumkin.

yigindi = 0
sanoq = 0
while True:
    n = float(input())
    if n == 0:
        break
    yigindi += n
    sanoq += 1
if sanoq == 0:
    print(0)
else:
    print(yigindi/sanoq)