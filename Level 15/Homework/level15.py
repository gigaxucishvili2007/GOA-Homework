# 1)for loop-ის საშუალებით ტერმინალში გამოიტანეთ 2-დან 50-ის ჩათვლით ნომრები ოღონდ ნაბიჯი იყოს 4
# ანუ ყოველ i-ს თითეულ ნაბიჯზე დაემატოს 4
for i in range(2,51,4):
    print(i)

# 2) for loop-ის საშუალებით ტერმინალში გამოიტანეთ  10-ჯერ ყოველი ( i ელემენტი და გვერდით მიუწერეთ, "GOA")
# i --------- საიტერაციო ცვლადი
for i in range(0,11,1):
    print(i, "GOA")

# 3) დაწერეთ პროგრამა for loop-ის გამოყენებით, რომელიც გამოგვიტანს ჯერ ლუწს და შემდეგ კენტს.
# თუ გაიაზრებთ მარტივია ძალიან.
for i in range(0,11,2):
    print(i)

for i in range(1,11,3):
    print(i)

#4) შექმენით პროგრამა სადაც გამოიყენებთ While loop - ს. 
# თქვენი დავალება იქნება ის, რომ მომხამრებელს შემოატანინოთ რიცხვი და თქვენ უნდა გამოიცნოთ ეს რიცხვი, ხოლო ყოველ არ გამოცნობილ რიცხვზე ისევ თავიდან უნდა შეგეკითხოთ და შეიყვანოთ რიცხვი.
num = int(input("shemoitanet ricxvi: "))

guess = None

while guess != num:
    guess = int(input("gamoicanit ricxvi:"))

    if guess < num:
        print("ricxvi aris patara, cadet ufro didi ricxvi")
    elif guess > num:
        print("ricxvi aris didi, cade ufro patara")
    else:
        print("shen moige uraaa")