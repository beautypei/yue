bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])#----访问列表的第一个元素，列表的第一个元素从0开始
print(bicycles[0].title())#访问列表的第一个元素，并且首字母大写
print(bicycles[-1])#访问列表的最后一个元素

bicycles = ['trek','cannondale','redline','specialized']
message = 'my first bicycle was a ' + bicycles[0] + '.'
print(message)#使用表中的值来进行拼接

motorcycles = ['honda','yamaha','suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)#将列表的第一个元素修改为ducati

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')# 在列表的末尾添加一个元素
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)#创建一个空列表，使用append在列表中添加元素

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)#将元素插入至列表的第一位，其他所有元素右移一个位置

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)#删除列表中的第一个元素

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)# 将列表中的最后一个元素弹出，将它储存到变量popped_motorcycle中

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print('The last motorcycle i owned was a ' + last_owned.title() + '.')

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)#使用pop元可以删除指定位置的元素
print('The first motorcycle i owned was a ' + first_owned.title() + '.')

motorcycles = ['honda','yamaha','suzuki']
motorcycles.remove('yamaha')
print(motorcycles)#使用remove可以直接删除想要删除的元素不需要知道元素的位置，被删除的元素可以继续使用

motorcycles = ['honda','yamaha','suzuki']
remove_motorcycle = 'yamaha'#将值存储在变量中，再将值进行删除操作
motorcycles.remove(remove_motorcycle)
print('The remove motorcycle i owned was a ' + remove_motorcycle.title() + '.')

cars = ['bnw','audi','toyota','subaru']
cars.sort()#使用sort对列表中的元素按照字母大小的顺序永久性排列
print(cars)

cars = ['bnw','audi','toyota','subaru']
cars.sort(reverse=True)#向sort方法传递参数reverse=True，实现倒序排列
print(cars)