day = str(input("enter day :"))
hours = int(input("enter your time :"))
work0 = 10#დან 21
work1 = 21#საათამდე
if work0 == 10:
    print("მაღაზია ღიაა")
elif work1 == 21:
    print("ღია")
else:
    print("მაღაზია დაკეტილია")
    კვირის_დღეები = "არ ვმუშაობთ"
    if კვირის_დღეები == "არ ვმუშაობთ":
        print("მაღაზია დაკეტილია")