# students= {
#     '120':{
#         'name':'Ali',
#         'surname':'Yılmaz',
#         'tel':'15131121'
#     },
#     '125':{
#         'name':'Can',
#         'surname':'Korkmaz',
#         'tel':'541534486'
#     },
#     '128':{
#         'name':'Volkan',
#         'surname':'Yükselen',
#         'tel':'424241313'
#     }
# }

students = {}

number = input ('student no: ')
name = input ('student name:' )
surname = input ('student surname:' )
phone = input ('phone: ' )

# students[number] ={
#     'name':name,
#     'surname':surname,
#     'phone':phone
# }

students.update({
    number:{
        'name':name,
        'surname':surname,
        'phone':phone
    }
})

number = input ('student no: ')
name = input ('student name:' )
surname = input ('student surname:' )
phone = input ('phone: ' )



students.update({
    number:{
        'name':name,
        'surname':surname,
        'phone':phone
    }
})


number = input ('student no: ')
name = input ('student name:' )
surname = input ('student surname:' )
phone = input ('phone: ' )

students.update({
    number:{
        'name':name,
        'surname':surname,
        'phone':phone
    }
})


print (students)

print ('*'*50)

studentNo = input ('student no: ')
student = students[studentNo]

print (student)