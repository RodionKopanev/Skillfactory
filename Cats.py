from Cat import Catty

c1 = Catty('baron', 'male', 2)
c2 = Catty('Sam', 'male', 2)

print(c1.name, c1.gender, c1.age)
print(c2.name, c2.gender, c2.age)

# второй вариант

Cats = [{'name':'baron', 'gender':'male', 'age':2},
        {'name':'sam', 'gender':'male', 'age':2}]
for i in Cats:
    Cats_obj = Catty(name=i.get('name'), gender=i.get('gender'), age=i.get('age'))
    print(Cats_obj.name, Cats_obj.gender, Cats_obj.age)