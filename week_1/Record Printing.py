record = [{'roll_num': 5, 'age':5 , 'name':5, 'marks':5},
          {'roll_num': 5, 'age': 5, 'name':5, 'marks':5},
          {'roll_num': 5,'age': 5, 'name':5, 'marks':5},
          {'roll_num': 5, 'age': 5, 'name':5, 'marks':5},
          {'roll_num': 5, 'age': 5, 'name':5, 'marks':5}]
for i in range(5):
    record[i]['roll_num'] = input('Enter Roll No.: ')
    record[i]['age']  = input('Enter Age: ')
    record[i]['name'] = input('Enter Name: ')
    record[i]['marks'] = input('Enter Marks: ')
print ('Roll No. || Age || Name || Marks')
    
for i in range(5):
  print(record[i]['roll_num'] + '       || ' + record[i]['age'] + '       || ' + record[i]['name'] + ' || ' + record[i]['marks'] )
    
    