import json
from random import randint, shuffle


# 初始化
file_name = 'data.json' # 文件
data = [] # 初始化数据列表

while_id1, while_id2 = 0, 0


# 定义方向
up = 1
down = 2
left = 3
right = 4
up_left = 5
up_right = 6
down_left = 7
down_right = 8


# 获取参数
numbers = int(input('数据数量: ')) # 获取需要生成的数据数量
mins = int(input('坐标最小值: ')) # 获取坐标的最小值
maxs = int(input('坐标最大值: ')) # 获取坐标的最大值


# 生成水平移动数据
while while_id1 != int(numbers/2):
    # 定义元素列表
    item = []

    # 数据设置是x相等还是y相等
    way = randint(1, 2)

    # 随机生成数据
    if way == 1: # x相等
        x = randint(mins, maxs)

        target_x, ai_x = x, x

        target_y = randint(mins, maxs)
        ai_y = randint(mins, maxs)

    elif way == 2: # y相等
        y = randint(mins, maxs)

        target_y, ai_y = y, y

        target_x = randint(mins, maxs)
        ai_x = randint(mins, maxs)




    # 处理向上移动(ai在角色下面)
    if ai_x == target_x and ai_y > target_y:
        direction = up

        # 如果符合条件, id加1
        while_id1 = while_id1 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    # 处理向下移动(ai在角色上面)
    elif ai_x == target_x and ai_y < target_y:
        direction = down

        # 如果符合条件, id加1
        while_id1 = while_id1 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    # 处理向左移动(ai在角色右边)
    elif ai_x > target_x and ai_y == target_y:
        direction = left

        # 如果符合条件, id加1
        while_id1 = while_id1 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    # 处理向右移动(ai在角色左边)
    elif ai_x < target_x and ai_y == target_y:
        direction = right

        # 如果符合条件, id加1
        while_id1 = while_id1 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    else:
        # 如果不符合条件, id不变
        while_id1 = while_id1
        continue




# 生成斜向数据
while while_id2 != int(numbers/2):
    # 定义元素列表
    item = []

    # 随机生成数据
    target_x = randint(mins, maxs)
    target_y = randint(mins, maxs)
    ai_x = randint(mins, maxs)
    ai_y = randint(mins, maxs)




    # 处理左上移动(ai在角色右下方)
    if ai_x > target_x and ai_y > target_y:
        direction = up_left

        # 如果符合条件, id加1
        while_id2 = while_id2 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    # 处理右上移动(ai在角色左下方)
    elif ai_x < target_x and ai_y > target_y:
        direction = up_right

        # 如果符合条件, id加1
        while_id2 = while_id2 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    # 处理左下移动(ai在角色右上方)
    elif ai_x > target_x and ai_y < target_y:
        direction = down_left

        # 如果符合条件, id加1
        while_id2 = while_id2 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    # 处理右下移动(ai在角色左上方)
    elif ai_x < target_x and ai_y < target_y:
        direction = down_right

        # 如果符合条件, id加1
        while_id2 = while_id2 + 1

        # 写入列表
        item.append(direction)
        item.append(target_x)
        item.append(target_y)
        item.append(ai_x)
        item.append(ai_y)

        data.append(item)

    else:
        # 如果不符合条件, id不变
        while_id2 = while_id2
        continue


# 打乱数据
shuffle(data)


# 写入数据
with open(file_name, 'w') as file:
    json.dump(data, file)


# 打印数据和数据长度
print(data)
print('\n数据长度: ' + str(len(data)))

# 打印1234的长度
one, two, three, four, five, six, seven, eight = [], [], [], [], [], [], [], []
ottfs, fsses = [], []
for num in data:
    if num[0] == 1:
        one.append(num)
    elif num[0] == 2:
        two.append(num)
    elif num[0] == 3:
        three.append(num)
    elif num[0] == 4:
        four.append(num)
    elif num[0] == 5:
        five.append(num)
    elif num[0] == 6:
        six.append(num)
    elif num[0] == 7:
        seven.append(num)
    elif num[0] == 8:
        eight.append(num)

    if num[0] == 1 or num[0] == 2 or num[0] == 3 or num[0] == 4:
        ottfs.append(num)
    elif num[0] == 5 or num[0] == 6 or num[0] == 7 or num[0] == 8:
        fsses.append(num)

print('1的长度: ' + str(len(one)))
print('2的长度: ' + str(len(two))) 
print('3的长度: ' + str(len(three)))
print('4的长度: ' + str(len(four)))
print('5的长度: ' + str(len(five)))
print('6的长度: ' + str(len(six)))
print('7的长度: ' + str(len(seven)))
print('8的长度: ' + str(len(eight)))
print('1, 2, 3, 4的长度: ' + str(len(ottfs)))
print('5, 6, 7, 8的长度: ' + str(len(fsses)))