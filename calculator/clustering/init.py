# -*- coding: UTF-8 -*-
import numpy
from calculator import calculatorPublic
from calculator import tarantula


# 判断是否在簇内
def check(cuMap, number):
    for i in range(cuMap.__len__()):
        for j in range(cuMap[i].__len__()):
            if cuMap[i][j] == number:
                return i
    return -1


# 对全体测试用例进行tarantula算法计算
# 对其结果进行聚类，将多错误问题转换为多个单错误问题
def init(dirPosition):
    # tarantula算法得到结果
    initList = tarantula.tarantulaList(dirPosition)
    # 前２０％怀疑度矩阵
    rankList = calculatorPublic.getResultList(initList)
    # 程序是否通过的列表
    answerList = calculatorPublic.getAnswer(dirPosition)
    # 程序运行轨迹gcov矩阵
    gcovList = calculatorPublic.getGcov(dirPosition, 1)
    # 记录未通过测试用例编号(真实编号－１)
    unPassList = []
    # 未通过测试用例是否执行被怀疑语句的记录矩阵
    initMap = []
    # 获取记录矩阵（initMap）
    for i in range(answerList.__len__()):
        if answerList[i] == 0:
            temp = []
            unPassList.append(i)
            for j in range(rankList.__len__()):
                for k in range(rankList[j].__len__()):
                    if gcovList[i][rankList[j][k]] == 1:
                        temp.append(rankList[j][k])
            if temp.__len__() != 0:
                initMap.append(temp)
    # 相似度矩阵
    similarMap = []
    # 获取相似度矩阵
    for i in range(initMap.__len__()):
        temp = []
        for j in range(initMap.__len__()):
            if i == j:
                temp.append(0)
            else:
                # 获取交集
                len1 = list(set(initMap[i]).intersection(set(initMap[j]))).__len__()
                # 获取并集
                len2 = list(set(initMap[i]).union(set(initMap[j]))).__len__()
                temp.append(len1 / len2)
        similarMap.append(temp)
    # 存放簇
    cuMap = [[0]]
    # 获取簇(cuMap)
    for i in range(similarMap.__len__()):
        position = check(cuMap, i)
        if position == -1:
            maxnum = 0
            site = 0
            for j in range(cuMap.__len__()):
                for k in range(cuMap[j].__len__()):
                    if similarMap[cuMap[j][k]][i] > maxnum:
                        maxnum = similarMap[cuMap[j][k]][i]
                        site = j
            if maxnum >= 0.7:
                cuMap[site].append(i)
            else:
                cuMap.append([i])
    # 存放簇中对应的测试用例编号（实际编号－１的值）
    testNumberMap = []
    # 将簇中对应编号进行转换
    for i in range(cuMap.__len__()):
        temp = []
        for j in range(cuMap[i].__len__()):
            temp.append(unPassList[cuMap[i][j]])
        testNumberMap.append(temp)
    print(testNumberMap.__len__())
    # 将分簇后的测试用例编号矩阵（testNumberMap）进行物理存储
    numpy.save(dirPosition + "/numpyDataDir/testNumberMap.npy", testNumberMap)


# if __name__ == '__main__':
#     init("/home/kalasu/PycharmProjects/tot_info")
