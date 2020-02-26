alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points']) #创建一个字典

alien_0 = {'color': 'green','points': 5}
new_points = alien_0['points'] #设置一个变量
print('You just earned ' + str(new_points) + ' points!')

alien_0 = {'color': 'green','points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25 #在字典中添加键-值对
print(alien_0)

alien_0 = {} #创建一个空字典并添加键-值对
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color':'green'}
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow'#修改字典中的值
print('The alien is now ' + alien_0['color'] + '.')

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print('Original x_position: ' + str(alien_0['x_position']))
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x_position: ' + str(alien_0['x_position']))

alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points'] #删除键值对，永久删除
print(alien_0)

user_0 = {
    'username':'efemi',
    'first':'enrico',
    'last':'femi',
}
for key,value in user_0.items(): #for循环遍历列表
    print('\nkey: ' + key)
    print('value:' + value)
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in sorted(favorite_languages.keys()): #按顺序遍历字典中的所有
    print(name.title() + ", thank you for taking the poll.")