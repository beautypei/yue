cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw': #两个等号是发问
        print(car.upper())
    else:
        print(car.title())#循环打印列表元素,if语句判断car的名字为bmw则全部大写,其余首字母大写

requested_topping= 'mushrooms'
if requested_topping != 'achovies': #判断两个值是否不等
    print('Hold the anchovies')

requested_toppings = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_toppings:
    print('Yes!')#判断元素是否在列表里
if 'onions' in requested_toppings:
    print('Oh Yes!')

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users: #not in 判断元素不在列表之中
    print(user.title() + ',you can post a response if you wish.')

age = 19
if age >= 18:
    print('You are old enough to votel!')

age = 17
if age >= 18:
    print('You are old enough to votel!')
else:
    print('NO!')


age = 12
if age < 4:
    print('you admission cost is 0.')
elif age < 18:
    print('your admission cost is 5.')
else:
    print('your admission cost is 10.')

###如果你只想执行一个代码快,就使用if-elif-else结构,如果运行多个代码快,就使用一系列独立的if语句

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '.')
print('\nFinished making your pizza')

requested_topping = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print('Sorry,we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')

print('\nFinished making your pizza')


requested_toppings = []
if requested_toppings:  #判断列表是否为空
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('\nFinished making your pizza')
else:
    print('Are you sure you want a plain pizza?')

available_toppings = ['mushrooms','olives','green peppers','peppernoi','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry,we don't have " + requested_topping + '.')

print('\nFinished making your pizza')
