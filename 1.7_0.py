#nested collection
'''
#1)nested-list
l1=[["Amy",80000,"BE"],["Ben",45000,"SSLC"],["Chad",89000,"Diploma"]]
for i in l1:
    if i[1]>50000:
        print(i[0])

l2=[["Amy",80000,"BE"],["Ben",45000,"SSLC"],["Chad",89000,"Diploma"]]
l2[1].append("metch")
print(l2)
'''
'''
#nested dictionary
company={'emp1':{'name':'Amy','age':21,'salary':80000,'dept':'accounts'},
        'emp2':{'name':'Ben','age':32,'salary':32000,'dept':'sales'},
         'emp3':{'name':'Chad','age':44,'salary':49000,'dept':'marketing'}}
for key in company:
    print(key)
    
for i in company.values():
    print(i)

for k,v in company.items():
    print(v)
for t in company.values():
   # print(t['name'])
    print(t['salary'])

for y in company.values():
    if y['salary']>48000:
        print(y['name'])

for x in company.values():
    if x['age']>40:
        x['salary']+=5000
        print(x)
print(company)
'''
'''
#list of dictionary
company=[{'name':'Amy','age':21,'salary':80000,'dept':'accounts'},
        {'name':'Ben','age':32,'salary':32000,'dept':'sales'},
        {'name':'Chad','age':44,'salary':49000,'dept':'marketing'}]

for i in company:
    print(i)

for i in company:
    print(i['name'])
for i in company:
    if i['salary']>49000:
        print(i['name'])

for i in range(2,-1,-1):
    print(company[i]['name'])
'''       
#dict of list
companys={'names':['Amy','Ben','chad'],
          'ages':[21,32,48],
          'salary':[82000,48000,36000],
          'depts':['HR','Sales','Accounts']
          }
for i in companys['names']:
    print(i)

for i in companys.values():
    print(i[0])
#zip
for names,salary in zip(companys['names'],companys['salary']):
    if salary>50000:
        print(names)
        
for i in companys:
    x=list(companys.values())
    if x['salary']>50000:
        print(x['names'])





















