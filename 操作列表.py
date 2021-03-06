

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician) #将列表中的元素循环存储到magician中并打印出来

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')#将列表的每个元素打印出来并拼接为一句话

magicians = ['alice', 'david', 'carolina']
for magician in magicians:#冒号里面的部分都是for循环执行的部分
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')

for value in range(1,6):
    print(value)#使用range函数打印数字，但是打印从1开始到5结束，不包含6

numbers = list(range(1,6))
print(numbers)#用list打印一个数字列表

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2#两个**表示乘方
    squares.append(square)#将乘方加到列表的后面
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)#直接将value的乘方加到列表的后面
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) #打印列表的最小值
print(max(digits)) #打印列表的最大值
print(sum(digits)) #打印列表值的和

squares = [value ** 2 for value in range(1,11)]
print(squares) #列表解析

squares = [value ** 3 for value in range(1,11)]
print(squares) #练习，打印1-10的立方


squares = []
for value in range(1,21):
    squares.append(value)
print(squares) #练习，打印列表的1-20

players = ['charles','martina','michael','florence','eli']
print(players[0:3])#索引只会把列表的0、1、2的元素查找出来
print(players[1:4])#索引1、2、3的元素
print(players[:4])#没有指定其实就从开头提取
print(players[2:])#从第三个元素开始到末尾
print(players[-3:])#打印列表的最后三个元素

players = ['charles','martina','michael','florence','eli']
print(' Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())#用for循环打印列表的前三个元素


my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('my favorite foods are:')
print(my_foods)
print('\nmy friend favorite foods are:')
print(friend_foods)#复制一个列表在两个列表中都添加元素，并打印两个列表
#####不可变的列表称为元组

dimensions = (200,50)
print(dimensions[0])#创建一个元组,并打印元组中的元素
print(dimensions[1])

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)#for循环打印元组的元素

dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)#定义了一个新的元组
print('Modified dimension:')
for dimension in dimensions:
    print(dimension)

