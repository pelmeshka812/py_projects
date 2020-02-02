import re

result = re.findall(r'@\w+', "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz")

result2 = re.findall(r'@\w+.\w+',
                     'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')

result3 = re.findall(r'@\w+.(\w+)',
                     'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
result4 = re.findall(r'\d{2}-\d{2}-\d{4}',
                     'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')


result5 = re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
print(result5)
