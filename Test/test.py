import math
# for i in range(3):
#     for j in range(3):
#         for k in range(9):
#             I = (math.ceil((i + 1) / 3) - 1)
#             J = (math.ceil((j + 1) / 3) - 1)
#             print(I, " - ", J)
for i in range(3):
    for j in range(3):
        for k in range(9):
            I = (math.ceil((k + 1) / 3) - 1) + i*3
            J = (math.ceil((k + 1)) - 1) % 3 + j*3
            print(I,J, end="    ")
        print("")