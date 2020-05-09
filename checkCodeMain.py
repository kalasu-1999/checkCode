# -*- coding: UTF-8 -*-
from dataProcessing import createMakeFile
from dataProcessing import createRunall
from dataProcessing import getData
from dataProcessing import matome
from calculator import tarantula
from calculator import ochiai
from calculator import jaccard
from calculator import FLSF
from calculator import networks
from calculator.inherited import resetPopulation
from calculator.inherited import InializeMain


# 根据输入进行算法计算
# cDirPosition:.c文件所在路径(例:/home)
# tempList:算法存放列表
def calculator(cDirPosition, tempList):
    tempStr = ""
    for item in tempList:
        tempStr = tempStr + str(item)
        if item == 1:
            tarantula.tarantulaMain(cDirPosition)
        if item == 2:
            ochiai.ochiaiMain(cDirPosition)
        if item == 3:
            jaccard.jaccardMain(cDirPosition)
        if item == 4:
            FLSF.FLSFMain(cDirPosition)
        if item == 5:
            networks.networksMain(cDirPosition, 1)
        if item == 6:
            networks.networksMain(cDirPosition, 2)
        if item == 7:
            InializeMain.Inialize(cDirPosition)
            resetPopulation.resetMain(cDirPosition)
    matome.matome(cDirPosition, tempStr)


# main函数，调用其他函数
# cPosition:.c文件(例：/home/asd.c)
# cDirPosition:.c文件所在路径(例:/home)
# testDirPosition:测试用例所在路径(例：/home/test)
# answerDirPosition:测试答案存放路径(例：/home/answer)
# tempList:算法存放列表
def checkMain(cPosition, cDirPosition, testDirPosition, answerDirPosition, tempList):
    createMakeFile.createMakeFile(cPosition)
    createRunall.createRunall(cPosition, testDirPosition)
    getData.getDataMain(cDirPosition, answerDirPosition)
    calculator(cDirPosition, tempList)
    print('finish')


if __name__ == '__main__':
    checkMain('/home/kalasu/PycharmProjects/tot_info/target.c',
              '/home/kalasu/PycharmProjects/tot_info',
              '/home/kalasu/PycharmProjects/tot_info/test',
              '/home/kalasu/PycharmProjects/tot_info/answer',
              [1, 2, 3, 4, 5, 6, 7])
