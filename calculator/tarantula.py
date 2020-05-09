# -*- coding: UTF-8 -*-
import numpy
from calculator import calculatorPublic

numpy.seterr(divide='ignore', invalid='ignore')


def tarantulaList(dirPosition):
    answerList = calculatorPublic.getAnswer(dirPosition)
    gcovList = calculatorPublic.getGcov(dirPosition, 1).T
    ef = calculatorPublic.getEF(gcovList, answerList)
    ep = calculatorPublic.getEP(gcovList, answerList)
    tf = calculatorPublic.getTF(answerList)
    tp = calculatorPublic.getTP(answerList, tf)
    return 1 / (1 + (numpy.dot(ep, tf)) / (numpy.dot(ef, tp)))


def tarantulaMain(dirPosition):
    resultList = calculatorPublic.getResultList(tarantulaList(dirPosition))
    numpy.save(dirPosition + "/numpyDataDir/tarantula.npy", resultList)
