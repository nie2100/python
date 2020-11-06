# count = 0
#
#
# def hanoi(n, src, dst, mid):
#     global count
#     if n == 1:
#         print('{}:{}->{}'.format(1, src, dst))
#         count += 1
#     else:
#         hanoi(n - 1, src, mid, dst)
#         print('{}:{}->{}'.format(n, src, dst))
#         count += 1
#         hanoi(n - 1, mid, dst, src)
#
#
# hanoi(3, "a", "c", "b")
# print(count)

def hanoi(n, a, b, c):
    if n == 1:
        print("{}:{}->{}".format(1, a, c))
    else:
        hanoi(n - 1, a, c, b)
        # print("{}:{}->{}".format(n, a, b))
        hanoi(1, a, b, c)
        # print("{}:{}->{}".format(n, a, c))
        hanoi(n - 1, b, a, c)
        # print("{}:{}->{}".format(n, b, c))


hanoi(4, "a", "b", "c")

# def move(n, fr, sp, to):
#     """
#     fr: from, tower A
#     sp: spare, tower B
#     to: to, tower C
#     """
#     if n == 1:
#         print(n,fr, '->', to)
#     else:
#         move(n - 1, fr, to, sp)
#         move(1, fr, sp, to)
#         move(n - 1, sp, fr, to)
#
# move(2, 'A', 'B', 'C')
