def getNum():
    nums = []
    iNumStr = input('请输入数字（回车退出）：')
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr=input('请输入数字（回车退出）：')
    return nums
def mean(numbers):
    s=0
    for num in numbers:
        s+=num
    return s/len(numbers)


if __name__ == '__main__':
    print(mean(getNum()))
