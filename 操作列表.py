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