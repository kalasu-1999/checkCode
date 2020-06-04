# -*- coding: UTF-8 -*-
import numpy
from calculator import calculatorPublic
from calculator import tarantula
from sklearn.cluster import DBSCAN


# 判断是否在簇内
def check(cuMap, number):
    for i in range(cuMap.__len__()):
        for j in range(cuMap[i].__len__()):
            if cuMap[i][j] == number:
                return i
    return -1


# 将rankList矩阵转换为list类型
def getRank(rankList):
    rank = []
    for i in range(rankList.__len__()):
        for j in range(rankList[i].__len__()):
            if rankList[i][j] not in rank:
                rank.append(rankList[i][j])
    return rank


# 获取参数１：每个错误测试用例所包含的怀疑度行与怀疑度行总数的百分比
def getParameter_x(initMap, rank):
    parameter_x = []
    rankLen = rank.__len__()
    for i in range(initMap.__len__()):
        parameter_x.append(len(initMap[i]) / rankLen)
    return parameter_x


# 获取参数２：每个错误测试用例的轨迹相对于第一个测试用例轨迹的变化值
def getParameter_y(gcovList, unPassList):
    parameter_y = []
    for i in unPassList:
        # 获取交集
        len1 = list(set(gcovList[i]).intersection(set(gcovList[0]))).__len__()
        # 获取并集
        len2 = list(set(gcovList[i]).union(set(gcovList[0]))).__len__()
        parameter_y.append(len1 / len2)
    return parameter_y


# 对参数１和参数２进行整合形成一个对应的坐标矩阵
def getParameterMap(parameter_x, parameter_y):
    parameterMap = []
    for i in range(parameter_x.__len__()):
        temp = [parameter_x[i], parameter_y[i]]
        parameterMap.append(temp)
    return parameterMap


# 对得到的坐标矩阵进行DBSCAN聚类操作得到分类列表
def getClusteringList(parameterMap):
    clusteringList = DBSCAN(eps=0.05, min_samples=4).fit_predict(parameterMap)
    return clusteringList


# 对得到的分簇list进行分解
def getDbscanTestNumber(clusteringList, unPassList):
    # 记录被筛选过的测试用例数量
    count = 0
    # 分簇结果值标志,从-1开始
    flag = -1
    # 存放分解结果
    dbscanTestNumber = []
    while count != clusteringList.__len__():
        temp = []
        for i in range(clusteringList.__len__()):
            if clusteringList[i] == flag:
                count = count + 1
                temp.append(unPassList[i])
        if temp.__len__() > 0:
            dbscanTestNumber.append(temp)
        flag = flag + 1
    return dbscanTestNumber


# 对全体测试用例进行tarantula算法计算
# 对其结果进行聚类，将多错误问题转换为多个单错误问题
def dbscan(dirPosition):
    # tarantula算法得到结果
    initList = tarantula.tarantulaList(dirPosition)
    # 前２０％怀疑度矩阵
    rankList = calculatorPublic.getResultList(initList)
    # 将rankList矩阵装换为list类型方便之后计算等操作
    rank = getRank(rankList)
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
            for item in rank:
                if gcovList[i][item] == 1:
                    temp.append(item)
            if temp.__len__() != 0:
                initMap.append(temp)
    # 获取参数１：每个错误测试用例所包含的怀疑度行与怀疑度行总数的百分比
    parameter_x = getParameter_x(initMap, rank)
    # 获取参数２：每个错误测试用例的轨迹相对于第一个测试用例轨迹的变化值
    parameter_y = getParameter_y(gcovList, unPassList)
    # 对参数１和参数２进行整合形成一个对应的坐标矩阵
    parameterMap = getParameterMap(parameter_x, parameter_y)
    # 对得到的坐标矩阵进行DBSCAN聚类操作得到分类列表
    clusteringList = getClusteringList(parameterMap)
    # 对得到的分簇list进行分解
    dbscanTestNumber = getDbscanTestNumber(clusteringList, unPassList)
    print("dbscan:" + str(dbscanTestNumber.__len__()))
    # 对得到的结果进行存放
    numpy.save(dirPosition + "/numpyDataDir/dbscanTestNumber.npy", dbscanTestNumber)

# if __name__ == '__main__':
#     dbscan("/home/kalasu/PycharmProjects/tot_info")
