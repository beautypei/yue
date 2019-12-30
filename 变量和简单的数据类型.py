print('hello world!')

message = 'hello world'
print(message)  #定义一个变量

message = 'hello python crash course world'
print(message) #再次定义一个变量

name = 'pei yue'
print(name.title())#将小写字母变为大写

name = 'pei yue'
print(name.upper())#将小写字母变为大写

name = 'PEI YUE'
print(name.lower()) #将大写字母变为小写

first_name = 'pei'
last_name = 'yue'
full_name = first_name + ' ' + last_name
print(full_name) #用加号来连接两个字符串

first_name = 'pei'
last_name = 'yue'
full_name = first_name + ' ' + last_name
print('Hello, ' + full_name.upper() + '!')

first_name = 'pei'
last_name = 'yue'
full_name = first_name + ' ' + last_name
message = 'Hello, ' + full_name.upper() + '!'
print(message)#将拼接的字符串存储在一个变量中

print('\tPei yue')#\t 为制表符

print('Languages: \npython\nC\nnJavaScript')#\n为换行符
print('Languages: \n\tpython\n\tC\n\tnJavaScript')#\n\t的组合可以使字段串的内容进行换行并在下一行开头添加一个制表符

favorite_language = 'Python '
print(favorite_language.rstrip())#rstrip的方法可以暂时的去掉字符串中空格
print(favorite_language)

favorite_language = 'Python '
favorite_language = favorite_language.rstrip()
print(favorite_language)#永久性的删除必须将删除的结果存储到变量中

favorite_language = ' Python '
print(favorite_language.lstrip())#删除左边空白
print(favorite_language.rstrip())#删除右边空白
print(favorite_language.strip())#删除两边空白
#练习
name = 'eric'
message = 'would you like to learn some Python today?'
full_message = 'Hello,' + name.title() + ',' + ' ' + message
print(full_message)

print(2+3)
print(3-2)
print(3/2)
print(3**3)#两个*代表乘方
print(2+3*4)
print((2+3)*4)#可以用括号改变运算顺序
print(0.1*3)

age = 27
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message) #str函数将数值类型转换为字符串类型

