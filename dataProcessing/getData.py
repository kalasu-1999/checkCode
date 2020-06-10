# -*- coding: UTF-8 -*-
import os
import numpy
import re


def getTestNumber(dirPosition):
    files = os.listdir(dirPosition)
    return files.__len__() // 2


def getTrueAnswerList(dirPosition, times):
    s = []
    for i in range(1, times + 1):
        f = open(dirPosition + '/t' + str(i))
        iterF = iter(f)
        strTemp = ""
        for line in iterF:
            strTemp = strTemp + line
        s.append(strTemp)
    return s


def getTestAnswer(dirPosition, times):
    testPath = dirPosition + '/t' + str(times)
    try:
        txt = open(testPath, "r")
        testAnswer = txt.read()
    except UnicodeDecodeError:
        txt = open(testPath, "rb")
        testAnswer = txt.read()
    return testAnswer


def setAnswer(dirPosition, trueList, times):
    answerList = []
    for item in range(1, times):
        if getTestAnswer(dirPosition + "/testAnswerDir", item) == trueList[item - 1]:
            answerList.append(1)
        else:
            answerList.append(0)
    numpy.save(dirPosition + "/numpyDataDir/answerNumpy.npy", answerList)


def openGcov(dirPosition, times):
    gcov = open(dirPosition + "/testAnswerDir/t" + str(times) + ".gcov")
    return gcov.readlines()


def setGcov(dirPosition, numbers):
    gcov1 = []
    gcov2 = []
    findLines = numpy.load(dirPosition + "/numpyDataDir/findLines.npy")
    for item in range(1, numbers + 1):
        list1 = []
        list2 = []
        lines = openGcov(dirPosition, item)
        for line in lines:
            it = re.split(r":", line)
            temp1 = re.compile(' ').sub("", it[0])
            temp2 = int(re.compile(' ').sub("", it[1]))
            if temp2 == 0:
                continue
            elif temp2 - 1 in findLines:
                if temp1 == "#####" or temp1 == "-":
                    list1.append(0)
                    list2.append(0)
                else:
                    list1.append(1)
                    list2.append(int(temp1))
        gcov1.append(list1)
        gcov2.append(list2)
    gcovList = numpy.array(gcov1)
    temp = numpy.sum(gcovList, axis=0)
    rangeList = []
    for i in range(temp.__len__()):
        if temp[i] == 0 or temp[i] == gcov1.__len__():
            rangeList.append(i)
    gcov1 = numpy.array(gcov1)
    gcov2 = numpy.array(gcov2)
    newFindLines = []
    newGcov1 = []
    newGcov2 = []
    for i in range(findLines.__len__()):
        if i not in rangeList:
            newFindLines.append(findLines[i])
            newGcov1.append(gcov1[:, i])
            newGcov2.append(gcov2[:, i])
    newGcov1 = numpy.array(newGcov1).T
    newGcov2 = numpy.array(newGcov2).T
    numpy.save(dirPosition + "/numpyDataDir/findLines.npy", newFindLines)
    numpy.save(dirPosition + "/numpyDataDir/gcov1.npy", newGcov1)
    numpy.save(dirPosition + "/numpyDataDir/gcov2.npy", newGcov2)


def getDataMain(cDirPosition, answerDirPosition):
    testNumber = getTestNumber(cDirPosition + "/testAnswerDir")
    trueAnswerList = getTrueAnswerList(answerDirPosition, testNumber)
    setAnswer(cDirPosition, trueAnswerList, testNumber + 1)
    setGcov(cDirPosition, testNumber)
