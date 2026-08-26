# n beriladi.
# while yordamida 1..n ichida 7 ga karrali eng kichik sonni top.
# Agar topilmasa, "No" chiqarsin.

n = int(input())
i = 1
topildi = False
while i <= n:
    if i % 7 == 0:
        print(i)
        topildi = True
        break
    i += 1
if not topildi:
    print("No")