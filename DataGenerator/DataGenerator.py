import numpy as np
import random as rnd

# for inputs x0 to x8
x = np.zeros(9, np.float64)

# for outputs y0 to y4
y = np.zeros(5, np.float64)
y[0] = (2 * x[0] * x[1] * x[2]) + (x[3] * x[4]) - (3 * x[5] * x[6] * x[7]) - (7 * x[0] ** 2 * x[7]) + (2 * x[4])
y[1] = (2 * x[0] * x[4] * x[5]) - (x[2] * x[3] - 3 * x[1] * x[2] * x[3]) - x[2] ** 2 * x[4] - (2 * x[6] * x[7]) + 1
y[2] = (x[2] ** 2) - (x[4] * x[6]) - (3 * x[0] * x[3] * x[5]) - (12 * x[0] ** 2 * x[1] * x[3]) - 2
y[3] = (x[5] ** 3) - (5 * x[0] * x[2] * x[7]) - (x[0] * x[3] * x[6]) - (2 * x[4] ** 2 * x[1] * x[3]) - 3 * x[7]
y[4] = (x[2] ** 2 * x[4]) - (2 * x[2] * x[3] * x[7]) - (x[0] * x[1] * x[3]) - (3 * x[5]) + (x[0] ** 2 * x[6]) - 1

print (x)
print (y)

fh = open("test.txt", "w")


def generate_random_x():
    for index, x_i in enumerate(x):
        x[index] = rnd.random()
    print x


# initiate random inputs

def calculate_y(index):
    generate_random_x()
    # y1 = 2*x1 * x2 * x3 + x4 * x5 - 3*x6 * x7 * x8 - 7*x1^2 * x8 + 2*x5
    if index == 0:
        y[0] = (2 * x[0] * x[1] * x[2]) + (x[3] * x[4]) - (3 * x[5] * x[6] * x[7]) - (7 * x[0] ** 2 * x[7]) + (2 * x[4])
    elif index == 1:
        y[1] = (2 * x[0] * x[4] * x[5]) - (x[2] * x[3] - 3 * x[1] * x[2] * x[3]) - x[2] ** 2 * x[4] - (
                    2 * x[6] * x[7]) + 1
    elif index == 2:
        y[2] = (x[2] ** 2) - (x[4] * x[6]) - (3 * x[0] * x[3] * x[5]) - (12 * x[0] ** 2 * x[1] * x[3]) - 2
    elif index == 3:
        y[3] = (x[5] ** 3) - (5 * x[0] * x[2] * x[7]) - (x[0] * x[3] * x[6]) - (2 * x[4] ** 2 * x[1] * x[3]) - 3 * x[7]
    elif index == 4:
        y[4] = (x[2] ** 2 * x[4]) - (2 * x[2] * x[3] * x[7]) - (x[0] * x[1] * x[3]) - (3 * x[5]) + (
                x[0] ** 2 * x[6]) - 1

    #write x to file
    for x_i in x:
        fh.write(str(x_i))
        fh.write(" ")

    #write y to file
    fh.write(str(y[index]))
    fh.write("\n")


for i in range(0, 120, 1):

    for j in range(0, 5, 1):
        calculate_y(j)

# np.savetxt("hello.csv", x, delimiter=",")
# fh.write(str(x))
# fh.write("\n")
# print("writing")

print y
