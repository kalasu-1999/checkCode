# -*- coding: UTF-8 -*-
import numpy
import sys
from calculator import calculatorPublic

numpy.seterr(divide='ignore', invalid='ignore')


def jaccardList(dirPosition):
    answerList = calculatorPublic.getAnswer(dirPosition)
    gcovList = calculatorPublic.getGcov(dirPosition, 1).T
    ef = calculatorPublic.getEF(gcovList, answerList)
    ep = calculatorPublic.getEP(gcovList, answerList)
    nf = calculatorPublic.getNF(gcovList, answerList)
    return 1 / (1 + (ep + nf) / ef)


def jaccardMain(dirPosition):
    resultList = calculatorPublic.getResultList(jaccardList(dirPosition))
    numpy.save(dirPosition + "/numpyDataDir/jaccard.npy", resultList)
