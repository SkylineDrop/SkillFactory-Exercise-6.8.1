from cat_origin import Cat

cat_1 = Cat("Baron", "male", 2)
cat_2 = Cat("Sam", "male", 2)

l = [cat_1, cat_2]

for cat in l:
    print(cat.getName(), cat.getGender(), cat.getAge())
