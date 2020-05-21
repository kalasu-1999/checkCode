# -*- coding: UTF-8 -*-
import numpy


def getAnswer(dirPosition):
    return numpy.load(dirPosition + "/numpyDataDir/answerNumpy.npy")


def getGcov(dirPosition, times):
    return numpy.load(dirPosition + "/numpyDataDir/gcov" + str(times) + ".npy")


def clean(list1, list2):
    my_list = numpy.dot(list1, list2)
    new_list = []
    for temp1 in range(0, my_list[0].__len__()):
        list_temp = [x[temp1] for x in my_list]
        if any(list_temp):
            new_list.append(list_temp)
    mat = numpy.array(new_list)
    mat = mat.T
    return mat


def getTF(answerList):
    count = 0
    for item in answerList:
        if item == 1:
            count = count + 1
    return count


def getTP(answerList, Tf):
    return len(answerList) - Tf


def getEF(gcovList, answerList):
    return numpy.dot(gcovList, answerList)


def getEP(gcovList, answerList):
    return numpy.dot(gcovList, 1-answerList)


def getNF(gcovList, answerList):
    return numpy.dot(1 - gcovList, answerList)


def getFS(gcovList, answerList):
    RS = numpy.diag(answerList)
    return clean(gcovList, RS)


def getPS(gcovList, answerList):
    RS = numpy.diag(answerList)
    return clean(gcovList, numpy.identity(RS.__len__()) - RS)


def getResultList(tempList):
    result = []
    try:
        count = 0
        times = 0
        nanmin = 0
        while count < 20 and nanmin != 2:
            nanmin = numpy.nanmin(tempList)
            temp = numpy.where(tempList == nanmin)[0]
            if len(temp) < 20:
                count = count + len(temp)
                result.append(temp)
            times = times + 1
            for i in range(0, len(tempList)):
                if tempList[i] == nanmin:
                    tempList[i] = 2
    except RuntimeError:
        print("Runtime error")
    except RuntimeWarning:
        print("RuntimeWaring")
    for i in range(0, result.__len__()):
        for j in range(0, len(result[i])):
            result[i][j] = result[i][j] + 1
    return result
