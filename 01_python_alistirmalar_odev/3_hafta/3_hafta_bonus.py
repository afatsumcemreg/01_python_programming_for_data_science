#**Bonus 1

student_scores_list = ['Harry', 37.21, 'Berry', 37.21, 'Tina', 37.2, 'Akriti', 41, 'Harsh', 39]

# Liste sırasıyla öğrenci ve aldığı notu ifade etmektedir.
# 2. en düşük nota sahip kişilerin adlarını alfabetik sıraya göre yazınız.
# Not: Listedeki kişi sayısı değişiklik gösterebilir, birden fazla en düşük not veya en düşük ikinci nota sahip kşiler olabilir.

# Çıktı

# Berry
# Harry

a, b = [], []
[a.append(x) if i % 2 == 0 else b.append(x) for i, x in enumerate(student_scores_list)]
students = dict(zip(a, b))

threshold = sorted(set(students.values()))[1]
names = [i for i, k in students.values() if k == threshold]

for i in sorted(names):
    print(i)



# BONUS 2
text = 'BASARIHERGUNTEKRARLANANKUCUKCABALARINTOPLAMIDIR'
slide = 5
part_length = 10


# Text ifadeyi her seferinde 5 harf yana kayarak  10 harflik bölümlere ayıracak
# her bölümdeki en çok tekrar eden harfi satır satır basacak bir fonksiyon yazınız.
# NOT: text, slide, part_length değişiklik gösterebilir.
# En çok tekrar eden birden fazla harf varsa hepsini yazdırınız.


# adım 1'de elde edilecek liste:

# BASARIHERG
# IHERGUNTEK
# UNTEKRARLA
# RARLANANKU
# NANKUCUKCA
# CUKCABALAR
# BALARINTOP
# INTOPLAMID

# adım 2 nihai çıktı:
# AR
# E
# RA
# A
# NAKUC
# A
# A
# I

def str_op(t, p, s):
    for i in range(0, len(t), s):
        new_str = t[i:(i + p)]
        if len(new_str) != p:
            break;
        new_str2 = dict()
        for x in new_str:
            if x in new_str2.keys():
                new_str2[x] += 1
            else:
                new_str2[x] = 1
        new_str3 = ""
        for i, k in new_str2.items():
            if k == sorted(set(new_str2.values()), reverse=True)[0]:
                new_str3 += i
        print(new_str3)


str_op(text, part_length, slide)



############## ADIM 1

adim1=[]
def str_op(t, p, s):
    for i in range(0, len(t), s):
        new_str = t[i:(i + p)]
        if len(new_str) != p:
            break;
        adim1.append(new_str)
        print(new_str)

str_op(text,part_length,slide)


# ADIM 2

def str_unique_char(adim1_list):
    for new_str in adim1_list:
        new_str2 = dict()
        for x in new_str:
            if x in new_str2.keys():
                new_str2[x] += 1
            else:
                new_str2[x] = 1
        new_str3 = ""
        for i, k in new_str2.items():
            if k == sorted(set(new_str2.values()), reverse=True)[0]:
                new_str3 += i
        print(new_str3)


str_unique_char(adim1)

##### BONUS 3
moves="ULLLRULDRLUDLRRLUULDLULRLDDUULRDUUULRDLRR"

steps = {"U": 0, "D": 0, "L": 0, "R": 0}
for i in moves:
    steps[i] += 1

print(steps)


def hesapla(step_dict):
    vertical = step_dict["D"] - step_dict["U"]
    horizental = step_dict["L"] - step_dict["R"]
    direction=[]
    if vertical > 0:
        direction.append("aşağı")
    else:
        direction.append("yukarı")
    if horizental>0:
        direction.append("sola")
    else:
        direction.append("sağa")
    print(f"Kişi {abs(vertical)} adım {direction[0]},{abs(horizental)} adım {direction[1]} gitmiştir")


hesapla(steps)
