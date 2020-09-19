class operation:
    def __init__(self, num):  # 初始化
        self.num = num

    def Square_root_operation(self, num):
        '''平方根运算'''
        if num < 0:
            print('\n错误，负数无法进行开平方\n')

        num_sqrt = num ** 0.5

        print('\n%0.3f的平方根为±%0.3f\n' % (num, num_sqrt))

    def Square_operation(self, num):
        '''平方运算'''
        num_sqrt = num * num
        print('\n%0.3f的平方数为%0.3f\n' % (num, num_sqrt))

    def Cubic_operation(self, num):
        '''立方运算'''
        num_sqrt = num ** 3

        print('\n%0.3f的立方数为%0.3f\n' % (num, num_sqrt))

    def Cube_root_operation(self, num):
        '''立方根运算'''

        if num < 0:
            # 负平方根处理
            power = (1 / 3)
            data = -num
            num_sqrt = data ** power
            answer = -num_sqrt
            print('\n%0.3f的立方根为%0.3f\n' % (num, answer))

        if num > 0:
            num_sqrt = num ** (1 / 3)

            print('\n%0.3f的立方根为%0.3f\n' % (num, num_sqrt))


while True:
    print('运算方法:\n1.平方根运算\n2.平方运算\n3.立方运算\n4.立方根运算')
    num_operation = operation
    operation_method = input('请输入运算方法>>>')

    if operation_method == "1":
        while True:
            # 执行平方根运算
            print('输入000 跳出循环(无输入则继续运算)')
            try:
                num = float(input('请输入一个数字>>>'))
                num_operation = operation(num)
                num_operation.Square_root_operation(num)
            except:
                pass
            if num == 000:
                break

    if operation_method == "2":
        while True:
            # 执行平方运算
            print('输入000 跳出循环(无输入则继续运算)')
            try:
                num = float(input('请输入一个数字>>>'))
                num_operation = operation(num)
                num_operation.Square_operation(num)
            except:
                pass
            if num == 000:
                break

    if operation_method == "3":
        while True:
            # 执行立方运算
            print('输入000 跳出循环(无输入则继续运算)')
            try:
                num = float(input('请输入一个数字>>>'))
                num_operation = operation(num)
                num_operation.Cubic_operation(num)
            except:
                pass
            if num == 000:
                break

    if operation_method == "4":
        while True:
            # 执行立方根运算
            print('输入000 跳出循环(无输入则继续运算)')
            try:
                num = float(input('请输入一个数字>>>'))
                num_operation = operation(num)
                num_operation.Cube_root_operation(num)
            except:
                pass
            if num == 000:
                break
