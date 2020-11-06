# def mergeSort(alist):
#     if len(alist)<=1:
#         print(alist)
#         return alist
#     mid = len (alist)//2
#     left = mergeSort(alist[:mid])
#
# alist = [54, 26]

# def x(i):
#     if i==3:
#         return i
#     i= i-1
#     x(i)
#     print(i)

def x(i):

    if i ==2:
        return i+1
    i-=1
    x(i)
    print(i)

x(9)