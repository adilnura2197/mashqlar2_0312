#7-misol
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

eng_katta = a

if b > eng_katta:
    eng_katta = b
if c > eng_katta:
    eng_katta = c

print("Eng katta son:", eng_katta)


#8-misol
yil = int(input("Yilni kiriting: "))

# Kabisa yil shartlari:
# yil 4 ga bo'linsa va (yil 100 ga bo'linmasa yoki yil 400 ga bo'linsa)
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Kabisa yili")
else:
    print("Oddiy yil")


#9-misol
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

eng_kichik = a

if b < eng_kichik:
    eng_kichik = b
if c < eng_kichik:
    eng_kichik = c

print("Eng kichik son:", eng_kichik)


#10-misol
raqam = int(input("Raqam kiriting: "))

if raqam == 0:
    print("0")
elif raqam == 1:
    print("1")
else:
    print("Boshqa raqam")


#11-misol
a = int(input("1-tomon: "))
b = int(input("2-tomon: "))

if a == b:
    print("Kvadrat")
else:
    print("To'rtburchak")


#12-misol
son = int(input("Son kiriting: "))

if son <= 100:
    print("Kichik yoki teng 100")
else:
    print("Katta")
