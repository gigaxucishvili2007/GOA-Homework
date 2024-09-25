
# დავალება 2: სტრიქონის ფორმატირება შექმენით სტრინგი სახელად template შემდეგი # create

# შინაარსით: “გამარჯობა, {name}. კეთილი იყოს თქვენი მობრძანება {place}-ში.” # create

# გამოიყენეთ format() ფუნქცია {name}-ის შესაცვლელად “Alice”-ით და {place}-ის 

# შესაცვლელად “Wonderland”-ით. შედეგი შეინახეთ ცვლადში სახელად formatted_string და 

# დაბეჭდეთ იგი.
# begginer error “ტიპის შეცდომა: replace ფუნქციას მინიმუმ 2 არგუმენტი სჭირდება, მიღებულია 1.”

template = 'Hello Giga Welcome to you in place'

print(template.replace("Giga" , "Alice"))

print(template.replace("place" , "Wonderland"))

formatted_string = 'Hello Alice Welcome to you in Wonderland'

print(formatted_string)

#this is updated result
