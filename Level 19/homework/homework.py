# დავალება: მომხმარებელს შემოატანინეთ
#  რიცხვი, შემდეგ კი for
#  ლუპის დახმარებით გავლეთ
#  დიაპაზონი მომხმარებლის შემოტანილ რიცხვამდე.
num = int(input("Enter your number"))
for i in range(0,26,1):
    print(i)

# დავალება: 10-დან 20-მდე
#  გამოტანეთ
#  ყველა რიცხვი,
#  while ციკლის დახმარებით

i = 10
result = 0
while i <= 20:
    print(i)
    i = i + 1

# დავალება: while ციკლის დახმარებით
#  გამოტანეთ 0-დან 100-მდე,
#  მხოლოდ ლუწი რიცხვები

number = 1
while number <= 100:
    if number % 2 == 0:
        print(number)
    number += 1


# დავალება: მომხმარებელს
#  შემოატანინეთ სახელი,
#  მომხმარებლის სახელი
#  თუ არ უდრის თქვენ
# ს სახელს, კიდევ გაიმეოროს კითხვა

registered_name = "Giga"
authorized = False

while authorized != True:
    user_input = input("enter your name: ")

#     if user_input == registered_name:
#         print("სწორია")
#         authorized = True
#     else:
#         print("არასწორია")


