with open('New Text Document.csv', 'r') as idfile:
    mails=[]
    ages=[]
    firs_names=[]
    last_names=[]
    print('========================================================================================== ')


    for line in idfile:
        data = line.strip().split(',')
        mails.append(data[0])
        ages.append(data[1])
        firs_names.append(data[2])
        last_names.append(data[3])

    print(mails)
    print(ages)
    print(firs_names)
    print(last_names)
print('========================================================================================== ')
print('\n')

print('mails'.center(25)+'ages'.center(15)+'firs_names'.center(15)+'last_names'.center(25))
print('\n')

table= zip(mails,ages,firs_names,last_names)
for mail ,age,firs_name,last_name in table:
    print(f'{mail:<30}  {age:<10}  {firs_name:<20} {last_name:10}')