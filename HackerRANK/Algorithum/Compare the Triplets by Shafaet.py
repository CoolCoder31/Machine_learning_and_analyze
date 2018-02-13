# import sys
# a = b = None
# def solve(a0, a1, a2, b0, b1, b2):
#         A = B = 0
#         for i in range(3):
#             a = 'a' + str(i)
#             b = 'b' + str(i)
#             if a > b:
#                 A = A + 1
#                 return A
#             if a < b:
#                 B = B + 1
#                 return B
#         return str(str(A) + '' + str(B))
# a0, a1, a2 = input().strip().split(' ')
# a0, a1, a2 = [int(a0), int(a1), int(a2)]
# b0, b1, b2 = input().strip().split(' ')
# b0, b1, b2 = [int(b0), int(b1), int(b2)]
# result = solve(a0, a1, a2, b0, b1, b2)
# print (" ".join(map(str, result)))
# not able to do