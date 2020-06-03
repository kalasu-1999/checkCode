# -*- coding: UTF-8 -*-
import numpy
import math
from calculator import calculatorPublic


# 载入分簇后的测试用例编号矩阵
def lordTestNumberMap(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/dbscanTestNumber.npy")


# 获取成功轨迹的簇（运行结果与预期一致的所有测试用例）
def getTrueNumberList(dirPosition):
    # 所有测试结果的簇
    answerList = calculatorPublic.getAnswer(dirPosition)
    # 存放成功轨迹的簇
    trueNumberList = []
    # 获取成功轨迹的簇
    for i in range(answerList.__len__()):
        if answerList[i] == 1:
            trueNumberList.append(i)
    return trueNumberList


# tarantula算法
def tarantula(dirPosition, testsList):
    # 载入源数据中的测试结果
    answerList = calculatorPublic.getAnswer(dirPosition)
    # 载入源数据中的gcov图谱集
    gcovList = calculatorPublic.getGcov(dirPosition, 1)
    # 存放本次计算需要的测试结果集
    answer = []
    # 存放本次计算需要的gcov图谱集
    gcov = []
    # 获取对应于testsList中所包含的测试用例的测试结果
    for test in testsList:
        answer.append(answerList[test])
        gcov.append(gcovList[test])
    # 将answer和gcov两个list都转换为numpy矩阵类型
    answer = numpy.array(answer)
    gcov = numpy.array(gcov)
    # 对gcov进行翻转
    gcov = gcov.T
    ef = calculatorPublic.getEF(gcov, answer)
    ep = calculatorPublic.getEP(gcov, answer)
    tf = calculatorPublic.getTF(answer)
    tp = calculatorPublic.getTP(answer, tf)
    return 1 / (1 + (numpy.dot(ep, tf)) / (numpy.dot(ef, tp)))


def getResultList(tarantulaAnswerList, resultList):
    if resultList.__len__() == 0:
        resultList = tarantulaAnswerList
    else:
        for i in range(tarantulaAnswerList.__len__()):
            if not math.isnan(tarantulaAnswerList[i]):
                if tarantulaAnswerList[i] > resultList[i]:
                    resultList[i] = tarantulaAnswerList[i]
    return resultList


# 对分簇后的测试用例进行再次计算
def recalculate(dirPosition):
    # 载入分簇后的测试用例编号矩阵
    testNumberMap = lordTestNumberMap(dirPosition)
    # 获取成功轨迹的簇
    trueNumberList = getTrueNumberList(dirPosition)
    # 存放运算中得到的各行怀疑度最高的值
    resultList = []
    # 进行二次tarantula算法运算
    for tests in testNumberMap:
        # 存放成功轨迹的簇和分簇后得到的一个簇整合的集合
        testsList = list(set(trueNumberList).union(set(tests)))
        # 获取tarantula算法计算得到的结果,存放在resultList中
        resultList = getResultList(tarantula(dirPosition, testsList), resultList)
    # 用于存最终结果
    result = calculatorPublic.getResultList(resultList)
    # 对最终结果进行物理存储
    numpy.save(dirPosition + "/numpyDataDir/dbscan.npy", result)


# if __name__ == '__main__':
#     recalculate("/home/kalasu/PycharmProjects/tot_info")
