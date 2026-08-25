# n (butun, musbat) beriladi.
# while yordamida n raqamlari yig‘indisini topib chiqar.
# Masalan: 123 -> 6

n = int(input())
yigindi = 0
while n > 0:
    raqam = n % 10
    yigindi += raqam
    n = n // 10
print(yigindi)