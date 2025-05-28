people=[]
for i in range(0, 50):
    people.append(100)
person2=32
for person1 in range(0, 50):
    person2=32
    people[person1]=people[person1]-1
    people[person2]=people[person2]+1
print(people)