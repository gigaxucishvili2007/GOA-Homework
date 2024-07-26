# დავალები: გაკეთეთ სარიგსტრაციო ფორმა, მომხმარებელს შემოატანინეთ ემაილი და პაროლი, თუ ემაილი და პაროლი ორივე შემოიტანა სწორად, დაგვიპრინტოს True ხოლო სხვა შემთხვევაში False

email = input('Enter your email')
password = input('Enter your password')

valid_email = '@' in email and '.' in email
valid_password = len(password) >= 6

if valid_email and valid_password:
    print(True)
else:
   print(False)