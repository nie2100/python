获取温度 = input('请输入带有符号的温度值：')
if 获取温度[-1] in ['F', 'f']:
    C = (eval(获取温度[0:-1]) - 32) / 1.8
    print('转换后的温度是{:.2f}F'.format(C))
elif 获取温度[-1] in ['c', 'C']:
    F = 1.8*eval(获取温度[0:-1])+32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print('输入错误！')
