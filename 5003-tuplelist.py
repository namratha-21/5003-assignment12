list =[("abc",93), ("mno",45), ("xyz",65)] 
dict1=dict() 
for student,score in list: 
    dict1.setdefault(student, []).append(score) 

print(dict1) 
