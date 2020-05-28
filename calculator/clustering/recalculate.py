# -*- coding: UTF-8 -*-
import numpy
from calculator import calculatorPublic


# 载入分簇后的测试用例编号矩阵
def lordTestNumberMap(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/testNumberMap.npy")


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


# 对分簇后的测试用例进行再次计算
def recalculate(dirPosition):
    # 载入分簇后的测试用例编号矩阵
    testNumberMap = lordTestNumberMap(dirPosition)
    # 获取成功轨迹的簇
    trueNumberList = getTrueNumberList(dirPosition)
    # 存放再次计算得到的高怀疑度行号
    resultMap = []
    # 进行二次tarantula算法运算
    for tests in testNumberMap:
        # 存放成功轨迹的簇和分簇后得到的一个簇整合的集合
        testsList = list(set(trueNumberList).union(set(tests)))
        # 获取tarantula算法计算得到的结果,存放在resultList中
        resultList = calculatorPublic.getResultList(tarantula(dirPosition, testsList))
        # 对运算得到数据进行处理整合
        for i in range(resultList.__len__()):
            if i >= resultMap.__len__():
                resultMap.append(resultList[i])
            else:
                resultMap[i] = list(set(resultMap[i]).union(set(resultList[i])))
    # 对resultMap进行按怀疑度高保留原则的去重,将最终结果保存至result中
    # 保用于存最终结果
    result = []
    # 去重用临时存储列表
    tempList = []
    for i in range(resultMap.__len__()):
        temp = []
        for j in range(resultMap[i].__len__()):
            if resultMap[i][j] not in tempList:
                temp.append(resultMap[i][j])
                tempList.append(resultMap[i][j])
        result.append(temp)
    # 对最终结果进行物理存储
    numpy.save(dirPosition + "/numpyDataDir/clustering.npy", result)


# if __name__ == '__main__':
#     recalculate("/home/kalasu/PycharmProjects/tot_info")
