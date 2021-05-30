import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
from pandas import DataFrame
from numpy.linalg import inv
import math

def read_data(filename):
    data = pd.read_csv(filename)
    # replace nan with average column value
    data = data.fillna(data._get_numeric_data().mean())
    data = np.array(data)
    print(len(data))
    for i in range(len(data)):
        dt = data[i][0]
        mm = int(dt.split(' ')[-2].split('-')[-2])
        dd = int(dt.split(' ')[-2].split('-')[-1])
        tt = int(dt.split(' ')[-1].split(':')[0])
        data[i][0] = 10000*mm + 100*dd + tt
    # sort the array with respect to date
    data = data[data[:, 0].argsort()]
    return data

def predict(indices, data):
    # predict the values of PM10(column 7) and PM25(column 8)
    sum10 = 0
    sum25 = 0
    for idx in indices:
        sum10 += data[idx][7]
        sum25 += data[idx][8]
    if len(indices)!=0:
        sum10 /= len(indices)
        sum25 /= len(indices)
    return sum10, sum25

def KNN(data, n, knn):
    # error for PM10(column 7) and PM25(column 8)
    error10_recur = np.zeros(576)
    error25_recur = np.zeros(576)
    error10_roll = np.zeros(576)
    error25_roll = np.zeros(576)
    # 576 is the number of predictions for one day
    for i in range(0,576):
        # RECURSIVE WINDOW
        sim = np.zeros(n+576)
        p = (i//24)*24
        for j in range(0, n+p):
            station_i = data[i+n]
            station_j = data[j]
            if station_i[-1]== station_j[-1]:
                station_i[-1] = 0
                station_j[-1] = 0
                # print("meeee")
            else:
                station_i[-1] = 0
                station_j[-1] = 1
            sim[j] = np.linalg.norm(station_i - station_j)

        # finding k nearest neighbors
        recur_idx = np.argpartition(-sim, knn)[-knn:]
        pred10, pred25 = predict(recur_idx, data)
        error10_recur[i] = (data[i][7]-pred10)
        error25_recur[i] = (data[i][8]-pred25)

        # ROLLING WINDOW
        sim = sim[i-1:i+n-1]
        # finding k nearest neighbors
        roll_idx = np.argpartition(-sim, knn)[-knn:]
        pred10, pred25 = predict(roll_idx, data)
        error10_roll[i] = (data[i][7]-pred10)
        error25_roll[i] = (data[i][8]-pred25)
        # print(error10_recur)
    print(error10_recur)
    print(error25_recur)
    print(error10_roll)
    print(error25_roll)
    return error10_recur, error25_recur, error10_roll, error25_roll


def main():
    data16 = read_data("./air-quality-madrid/csvs_per_year/madrid_2016.csv")
    data17 = read_data("./air-quality-madrid/csvs_per_year/madrid_2017.csv")
    data17 = data17[0:576, :]
    print(len(data16))
    print(len(data16[0]))
    print(len(data17))
    print(len(data17[0]))
    data = np.append(data16, data17, axis=0)
    # mod = np.linalg.norm(data[:, 1:-1], axis=0)
    mod = (np.sum(data**2, axis=0))**0.5
    data_norm = data/mod
    # print(len(data))
    knn = 5
    # print(data_norm[:,-1])
    # error10_recur, error25_recur, error10_roll, error25_roll = KNN(data[:,1:], len(data16), knn)
    #
    # plt.plot(data[-576:,0], error10_recur, 'rx')
    # plt.plot(data[-576:,0], error25_recur, 'bx')
    # plt.show()
    # plt.plot(data[-576:,0], error10_roll, 'rx')
    # plt.plot(data[-576:,0], error25_roll, 'bx')
    # plt.show()

    error10_recur, error25_recur, error10_roll, error25_roll = KNN(data_norm[:,1:], len(data16), knn)

    plt.plot(data[-576:,0], error10_recur, 'rx')
    plt.plot(data[-576:,0], error25_recur, 'bx')
    plt.show()
    plt.plot(data[-576:,0], error10_roll, 'rx')
    plt.plot(data[-576:,0], error25_roll, 'bx')
    plt.show()

if __name__ == "__main__":
	main()
