
# key - value


# 35 => İzmir  34 =>istanbul

# cities =['İzmir','İstanbul']
# plaques=[35,34]

# print(plaques[cities.index('İzmir')])
# print (plaques[cities.index('İstanbul')])


# # print (plaques['İzmir']) => 35

# plaques = {'İzmir':35, 'İstanbul':34}
# print(plaques['İstanbul'])


# plaques['Ankara']=6
# print(plaques)

# plaques['İstanbul']= 'new value'
# print(plaques)


users = {
    'sadikturan': 
        {
        'age':36,
        'roles':['user'],
        'mail':'xxx.gmail.com',
        'adress':'kocaeli',
        'tel':'1513513'
        },
        
    'cinarturan':
        {
        'age':35,
        'roles':['user','admin'],
        'mail':'yyy.gmail.com',
        'adress':'Denizli',
        'tel':'15135'
        }
         }

print(users['sadikturan']['age'])
print (users['sadikturan']['adress'])
print (users['cinarturan']['roles'])
