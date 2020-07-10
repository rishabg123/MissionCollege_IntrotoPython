import random
roleList = ['assistant', 'associate', 'full']
fp = open('Salary.txt', 'w')
salary = 0.0
for i in range(1, 1001):
    fname = "FirstName" + (str(i))
    lname = "LastName" + str(i)
    role = str(random.choice(roleList))
    if role == 'full':
        salary = random.randrange(7500000, 13000000) / 100
    elif role == 'assistant':
        salary = random.randrange(5000000, 8000000) / 100
    else:
        salary = random.randrange(6000000, 11000000) / 100
    #print(fname, end=' ')
    #print(lname, end=' ')
    #print(role, end=' ')
    #print(salary)
    #print()

    emprecord = fname.ljust(15)  + lname.ljust(15) + role.ljust(15) +str(salary).ljust(15) + str("\n")
    #print(emprecord)
    fp.write(emprecord)

fp.close()