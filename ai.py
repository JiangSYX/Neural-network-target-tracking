import sys
import json
import time
import numpy
import pygame

pygame.init()


# 神经网络
class NeuralNetwork:

    # 初始化神经网络
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 初始化神经层
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # 初始化权值
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # 初始化学习率
        self.lr = learningrate

        # 初始化S型激活函数
        self.activation_function = lambda x: 1 / (pow(2.7182818, -x) + 1)

        pass

    # 训练神经网络
    def train(self, inputs_list, targets_list):
        # 输入数据数组和目标数据数组
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # 输入层到隐藏层的权值计算
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 隐藏层激活函数激活
        hidden_outputs = self.activation_function(hidden_inputs)

        # 隐藏层到输出层的权值计算
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 输出层激活函数激活
        final_outputs = self.activation_function(final_inputs)

        # 输出层误差
        output_errors = targets - final_outputs
        # 隐藏层误差
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 根据误差更新隐藏层到输出层的权值
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # 根据误差更新输出层到隐藏层的权值
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    # 查询神经网络
    def query(self, inputs_list):
        # 输入数据数组
        inputs = numpy.array(inputs_list, ndmin=2).T

        # 输入层到隐藏层的权值计算
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 隐藏层激活函数激活
        hidden_outputs = self.activation_function(hidden_inputs)

        # 隐藏层到输出层的权值计算
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # 输出层激活函数激活
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# 主函数
def main():
    # 初始化窗口及神经网络
    ai_speed = 1 # AI的速度
    target_speed = 2 # 目标速度
    running_times = 0 # 运行次数
    ai_coordinate_id = 1 # AI坐标id
    screen_size = (800, 600) # 窗口大小
    screen = pygame.display.set_mode(screen_size) # 创建窗口
    font = pygame.font.Font('C:/Windows/Fonts/msyh.ttc', 18) # 加载字体
    first_time = time.time() # 获取程序刚运行的时间 

    up_move, down_move, left_move, right_move = False, False, False, False

    target_coordinate = (screen_size[0]/2, screen_size[1]/2) # 目标坐标
    ai_coordinate_1 = (600, 100) # AI坐标 1
    ai_coordinate_2 = (100, 100) # AI坐标 2
    ai_coordinate_3 = (200, 50) # AI坐标 3
    ai_coordinate_4 = (150, 500) # AI坐标 4
    ai_coordinate_5 = (600, 550) # AI坐标 5
    ai_coordinate_6 = (target_coordinate[0], 100) # AI坐标 6
    ai_coordinate_7 = (target_coordinate[0], 500) # AI坐标 7
    ai_coordinate_8 = (100, target_coordinate[1]) # AI坐标 8
    ai_coordinate_9 = (600, target_coordinate[1]) # AI坐标 9
    ai_coordinate = ai_coordinate_1 # AI默认坐标
    change_ai_coordinate = False # 是否更改AI坐标

    # 加载数据
    with open('data.json', 'r') as objects:
        data = json.load(objects)
    lists = []
    for datum in data:
        for item in datum:
            lists.append(item)
    max_coordinate = max(lists) # 获取最大坐标值
    min_coordinate = min(lists) # 获取最小坐标值

    # 神经网络输入层, 隐藏层和输出层的神经元数量
    input_nodes = 4
    hidden_nodes = 200
    output_nodes = 8

    # 学习率
    learning_rate = 0.01

    # 迭代
    if_train = True # 是否训练
    learning_times = 0 # 当前学习次数
    iteration = 10 # 迭代次数


    # 创建神经网络实例
    neural_network = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)


    # 开始游戏主循环
    while True:
        # 更新运行次数和时间并显示AI当前坐标的id
        running_times = running_times + 1
        last_time = time.time()
 
        pygame.display.set_caption(
            '运行次数: ' + str(running_times) + 
            ' | AI坐标ID: ' + str(ai_coordinate_id) + 
            ' | 时间: ' + str(round(last_time - first_time, 1)) + 's' +
            ' | 目标坐标: X ' + str(target_coordinate[0]) + ' Y ' + str(target_coordinate[1]) +
            ' | AI坐标: X ' + str(round(ai_coordinate[0], 1)) + ' Y ' + str(round(ai_coordinate[1], 1))
            )

        # 响应键盘鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    up_move = True
                elif event.key == pygame.K_s:
                    down_move = True
                elif event.key == pygame.K_a:
                    left_move = True
                elif event.key == pygame.K_d:
                    right_move = True
                elif event.key == pygame.K_LEFT:
                    change_ai_coordinate = True
                    if ai_coordinate_id == 1:
                        ai_coordinate_id = 9
                    else:
                        ai_coordinate_id = ai_coordinate_id - 1
                elif event.key == pygame.K_RIGHT:
                    change_ai_coordinate = True
                    if ai_coordinate_id == 9:
                        ai_coordinate_id = 1
                    else:
                        ai_coordinate_id = ai_coordinate_id + 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    up_move = False
                elif event.key == pygame.K_s:
                    down_move = False
                elif event.key == pygame.K_a:
                    left_move = False
                elif event.key == pygame.K_d:
                    right_move = False

        # 绘制屏幕背景颜色
        screen.fill((0, 0, 0))

        # 绘制目标点
        if up_move == True:
            if target_coordinate[1] >= 0:
                target_coordinate = (target_coordinate[0], target_coordinate[1] - target_speed)
        if down_move == True:
            if target_coordinate[1] <= screen_size[1]:
                target_coordinate = (target_coordinate[0], target_coordinate[1] + target_speed)
        if left_move == True:
            if target_coordinate[0] >= 0:
                target_coordinate = (target_coordinate[0] - target_speed, target_coordinate[1])
        if right_move == True:
            if target_coordinate[0] <= screen_size[0]:
                target_coordinate = (target_coordinate[0] + target_speed, target_coordinate[1])
        target_rect = pygame.draw.circle(screen, (0, 255, 0), target_coordinate, 5, 0)

        # 直接干预更改AI坐标
        if change_ai_coordinate == True:
            if ai_coordinate_id == 1:
                ai_coordinate = ai_coordinate_1
            elif ai_coordinate_id == 2:
                ai_coordinate = ai_coordinate_2
            elif ai_coordinate_id == 3:
                ai_coordinate = ai_coordinate_3
            elif ai_coordinate_id == 4:
                ai_coordinate = ai_coordinate_4
            elif ai_coordinate_id == 5:
                ai_coordinate = ai_coordinate_5
            elif ai_coordinate_id == 6:
                ai_coordinate = ai_coordinate_6
            elif ai_coordinate_id == 7:
                ai_coordinate = ai_coordinate_7
            elif ai_coordinate_id == 8:
                ai_coordinate = ai_coordinate_8
            elif ai_coordinate_id == 9:
                ai_coordinate = ai_coordinate_9
            change_ai_coordinate = False


        # 更新迭代次数
        if learning_times <= iteration:
            learning_times = learning_times + 1
            if_train = True # 继续训练神经网络
        else:
            learning_times = iteration + 1
            if_train = False # 停止训练神经网络

        # 训练神经网络
        if if_train == True:
            for train_data in data:
                # 加载输入数据(输入数据 = (坐标 + 最小负值的绝对值的偏移值)/(最大值 + 最小负值绝对值 + 最小负值的绝对值的偏移值) + 0.01)
                inputs = []
                for item in train_data[1:]:
                    new = ((item + abs(min_coordinate))/(abs(max_coordinate) + abs(min_coordinate)*2)) + 0.01
                    inputs.append(new)

                # 加载目标数据
                targets = numpy.zeros(output_nodes) + 0.01 # 创建一个输出层神经元个数的列表, 元素值为0.01
                targets[int(train_data[0]) - 1] = 0.99 # 用0.99代替正确元素的位置

                # 训练神经网络
                neural_network.train(inputs, targets)

        # 每迭代一次就查询一次, 训练结束后继续查询
        inputs = []
        query_data = [target_coordinate[0], target_coordinate[1], ai_coordinate[0], ai_coordinate[1]]
        for item in query_data: # 加载查询数据(输入数据 = (坐标 + 最小负值的绝对值的偏移值)/(最大值 + 最小负值绝对值 + 最小负值的绝对值的偏移值) + 0.01)
            new = ((item + abs(min_coordinate))/(abs(max_coordinate) + abs(min_coordinate)*2)) + 0.01
            inputs.append(new)
        outputs = neural_network.query(inputs) # 查询神经网络
        label = numpy.argmax(outputs) + 1

        # 根据查询根据实时更改AI坐标
        if label == 1: # 向上
            direction = '上, up'
            ai_coordinate = (ai_coordinate[0], ai_coordinate[1] - ai_speed)
        elif label == 2: # 向下
            direction = '下, down'
            ai_coordinate = (ai_coordinate[0], ai_coordinate[1] + ai_speed)
        elif label == 3: # 向左
            direction = '左, left'
            ai_coordinate = (ai_coordinate[0] - ai_speed, ai_coordinate[1])
        elif label == 4: # 向右
            direction = '右, right'
            ai_coordinate = (ai_coordinate[0] + ai_speed, ai_coordinate[1])
        elif label == 5: # 左上
            direction = '左上, left up'
            ai_coordinate = (ai_coordinate[0] - ai_speed*0.7, ai_coordinate[1] - ai_speed*0.7)
        elif label == 6: # 右上
            direction = '右上, right up'
            ai_coordinate = (ai_coordinate[0] + ai_speed*0.7, ai_coordinate[1] - ai_speed*0.7)
        elif label == 7: # 左下
            direction = '左下, left down'
            ai_coordinate = (ai_coordinate[0] - ai_speed*0.7, ai_coordinate[1] + ai_speed*0.7)
        elif label == 8: # 右下
            direction = '右下, right down'
            ai_coordinate = (ai_coordinate[0] + ai_speed*0.7, ai_coordinate[1] + ai_speed*0.7)

        # 绘制AI点
        ai_rect = pygame.draw.circle(screen, (255, 0, 0), ai_coordinate, 5, 0)


        # 在屏幕上绘制信息
        if if_train == True:
            surface = font.render('迭代次数: ' + str(learning_times) + ' | ' + str(iteration), True, (255, 255, 255)) # 绘制迭代次数
        elif if_train == False:
            surface = font.render('迭代次数: ' + str(iteration) + ' | ' + str(iteration), True, (255, 255, 255))
        rect = surface.get_rect()
        rect.topleft = (25, 25)
        screen.blit(surface, rect)

        surface = font.render('神经网络决策: ' + direction, True, (255, 255, 255)) # 绘制神经网络的决策
        rect = surface.get_rect()
        rect.topleft = (25, 75)
        screen.blit(surface, rect)

        if if_train == True: # 绘制当前状态
            surface = font.render('Learning', True, (255, 255, 255))
            rect = surface.get_rect()
            rect.topright = (screen_size[0] - 25, 25)
            screen.blit(surface, rect)


        # 更新屏幕
        pygame.display.flip()


if __name__ == '__main__':
    main()

