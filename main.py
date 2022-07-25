import numpy as  np
import pandas as pd

from matplotlib import pyplot as plt


def regression(days, zarayeb, openn):
    # column 3 in zarayeb (t^2)
    powdays = np.arange(1, num_row - 9).reshape(-1, 1)
    powdays = powdays ** 2
    # zarayeb =X in X^TXB=X^Ty and we want B
    zarayeb = np.hstack((zarayeb, days, powdays))
    print(zarayeb)
    zarayeb_pow_transpose = np.transpose(zarayeb)
    XTX_pow = zarayeb_pow_transpose.dot(zarayeb)
    print("X^TX is :")
    print(XTX_pow)
    XTy_pow = zarayeb_pow_transpose.dot(openn)
    print("X^Ty is :")
    print(XTy_pow)
    answer_pow = np.linalg.solve(XTX_pow, XTy_pow)
    print("C0,C1,C2 are:")
    print(answer_pow)
    C0, C1, C2 = answer_pow
    C0 = C0.item()
    C1 = C1.item()
    C2 = C2.item()
    day = num_row - 10
    predict_pow = []
    errors_pow = []
    for j in range(10):
        predict_value_pow = C0 + (C1 * day) + (C2 * ((day) ** 2))
        print('for day number: ', day + 1)
        print('calculated value is : ', predict_value_pow)
        predict_pow.append(predict_value_pow)
        print('actual value is : ', df.at[day, 'Open'])
        errors_pow.append(-df.at[day, 'Open'] + predict_value_pow)
        print('error : ', errors_pow[j])
        day = day + 1
    print("avg of errors is:")
    sum = 0
    for _ in range(10):
        sum = sum + errors_pow[_]
    print(sum / 10)
    predict_pow = []
    day = 0
    for i in range(num_row):
        predict_pow.append(C0 + (C1 * day) + (C2 * ((day) ** 2)))
        day = day + 1

    return predict_pow


def linear_regression(days, zarayeb, openn):
    zarayeb = np.hstack((zarayeb, days))
    print("matrix zarayeb:")
    print(zarayeb)
    zarayeb_transpose = np.transpose(zarayeb)
    print(zarayeb_transpose)
    # zarayeb =X in X^TXB=X^Ty and we want B
    XTX = zarayeb_transpose.dot(zarayeb)
    print("X^TX is :")
    print(XTX)
    XTy = zarayeb_transpose.dot(openn)
    print("X^Ty is :")
    print(XTy)
    answer = np.linalg.solve(XTX, XTy)
    print("B0,B1 are:")
    print(answer)
    B0, B1 = answer
    B0 = B0.item()
    B1 = B1.item()
    day = num_row - 10
    predict = []
    errors = []
    for j in range(10):
        predict_value = B0 + (B1 * day)
        print('for day number: ', day + 1)
        print('calculated value is : ', predict_value)
        predict.append(predict_value)
        print('actual value is : ', df.at[day, 'Open'])
        errors.append(-df.at[day, 'Open'] + predict_value)
        print('error : ', errors[j])
        day = day + 1
    print("avg of errors is:")
    sum = 0
    for _ in range(10):
        sum = sum + errors[_]
    print(sum / 10)
    predicted_lin = []
    day = 0
    for i in range(num_row):
        predicted_lin.append(B0 + (B1 * day))
        day = day + 1

    return predicted_lin


if __name__ == '__main__':
    df = pd.read_csv("GOOGL.csv")
    print(df)
    num_row = len(df)
    # get row_number-10 of column Open
    openn = df.head(num_row - 10).Open.to_list()
    # make openn list to array with one column
    openn = np.array(openn).reshape((-1, 1))
    #     print("new array is: ")
    #     print(openn)
    # get all  elements in Open column
    list_openn = df.Open.to_list()
    # make 1 for num_row -10 in array
    zarayeb = np.ones((num_row - 10, 1))
    # make days in array
    days = np.arange(1, num_row - 9).reshape(-1, 1)
    #     print(days)

    print("polynomial")
    predict_pow = regression(days, zarayeb, openn)
    print("********************************************************")
    print("linear regression")
    predict_lin = linear_regression(days, zarayeb, openn)
    fig = plt.figure(figsize=(15, 8))
    plt.plot(predict_pow, color='blue', label='predict polynomial')
    # plt.plot(predict_lin, color='green', label='predict linear')
    plt.scatter(range(len(list_openn)), list_openn, color='red', label='actual values')
    plt.legend()
