# -*- coding: UTF-8 -*-
import numpy
import math
from calculator import calculatorPublic

numpy.seterr(divide='ignore', invalid='ignore')


def FLSFList(dirPosition):
    answerList = calculatorPublic.getAnswer(dirPosition)
    gcovList = calculatorPublic.getGcov(dirPosition, 2).T
    fs = calculatorPublic.getFS(gcovList, answerList)
    ps = calculatorPublic.getPS(gcovList, answerList)
    tf = calculatorPublic.getTF(answerList)
    tp = calculatorPublic.getTP(answerList, tf)
    res = []
    r1 = []
    r2 = []
    for i in range(0, len(fs)):
        temp1 = 0
        temp2 = 0
        for j in range(0, len(fs[0])):
            try:
                flag1 = math.exp(fs[i][j] * 0.6)
            except OverflowError:
                flag1 = float('inf')
            try:
                flag2 = math.exp(-fs[i][j] * 0.6)
            except OverflowError:
                flag2 = 0
            temp1 = temp1 + (flag1 - flag2) / (flag1 + flag2)
        r1.append(temp1)
        for k in range(0, len(ps[0])):
            try:
                flag1 = math.exp(ps[i][k] * 0.6)
            except OverflowError:
                flag1 = float('inf')
            try:
                flag2 = math.exp(-ps[i][k] * 0.6)
            except OverflowError:
                flag2 = 0
            temp2 = temp2 + (flag1 - flag2) / (flag1 + flag2)
        r2.append(temp2)
        temp4 = r2[i] * tf
        temp5 = r1[i] * tp
        if temp5 == 0:
            if temp4 == 0:
                res = numpy.append(res, 1)
            else:
                res = numpy.append(res, 0)
        else:
            temp3 = 1 / (1 + temp4 / temp5)
            res = numpy.append(res, temp3)
    return res


def FLSFMain(dirPosition):
    resultList = calculatorPublic.getResultList(FLSFList(dirPosition))
    numpy.save(dirPosition + "/numpyDataDir/FLSF.npy", resultList)
