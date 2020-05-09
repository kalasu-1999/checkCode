# -*- coding: UTF-8 -*-
import numpy
from calculator import calculatorPublic

numpy.seterr(divide='ignore', invalid='ignore')


def ochiaiList(dirPosition):
    answerList = calculatorPublic.getAnswer(dirPosition)
    gcovList = calculatorPublic.getGcov(dirPosition, 1).T
    ef = calculatorPublic.getEF(gcovList, answerList)
    ep = calculatorPublic.getEP(gcovList, answerList)
    nf = calculatorPublic.getNF(gcovList, answerList)
    return ef / numpy.sqrt((ef + nf) * (ef + ep))


def ochiaiMain(dirPosition):
    resultList = calculatorPublic.getResultList(ochiaiList(dirPosition))
    numpy.save(dirPosition + "/numpyDataDir/ochiai.npy", resultList)
