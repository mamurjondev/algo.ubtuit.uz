n = int(input())
hafta = 0
oy = 0
if n%7==1:
    hafta="Payshanba"
elif n%7==2:
    hafta="Juma"
elif n%7==3:
    hafta="Shanba"
elif n%7==4:
    hafta="Yakshanba"
elif n%7==5:
    hafta="Dushanba"
elif n%7==6:
    hafta="Seshanba"
else:
    hafta="Chorshanba"
if 1<=n<=31:
    n = n+1-1
    oy="Yanvar"
elif 32<=n<=59:
    n = n+1-32
    oy="Fevral"
elif 60<=n<=90:
    n = n+1-60
    oy="Mart"
elif 91<=n<=120:
    n = n+1-91
    oy="Aprel"
elif 121<=n<=151:
    n = n+1-121
    oy="May"
elif 152<=n<=181:
    n = n+1-152
    oy="Iyun"
elif 182<=n<=212:
    n = n+1-182
    oy="Iyul"
elif 213<=n<=243:
    n = n+1-213
    oy="Avgust"
elif 244<=n<=273:
    n = n+1-244
    oy="Sentabr"
elif 274<=n<=304:
    n = n+1-274
    oy="Oktabr"
elif 305<=n<=334:
    n = n+1-305
    oy="Noyabr"
elif 335<=n<=365:
    n = n+1-335
    oy="Dekabr"
print(f"{n}-{oy}, {hafta}")    
