a = input('请输入数字')
W = '星期一星期二星期三星期四星期五星期六星期日'
print(W[(eval(a)-1)*3:eval(a)*3])