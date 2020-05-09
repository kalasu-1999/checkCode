# -*- coding: UTF-8 -*-
import numpy
import xlwt


def matome(dirPosition, tempList):
    if len(tempList) != 0:
        book = xlwt.Workbook(encoding='UTF-8')
        for item in tempList:
            if item == '1':
                sheet1 = book.add_sheet('Tarantula')
                answerList = numpy.load(dirPosition + "/numpyDataDir/tarantula.npy")
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        str1 = str(answerList[i][0] + 1)
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                str1 = str1 + str(answerList[i][j] + 1) + ","
                            else:
                                str1 = str1 + str(answerList[i][j] + 1)
                    sheet1.write(i, 0, str1)
            if item == '2':
                sheet1 = book.add_sheet('Ochiai')
                answerList = numpy.load(dirPosition + "/numpyDataDir/ochiai.npy")
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        str1 = str(answerList[i][0] + 1)
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                str1 = str1 + str(answerList[i][j] + 1) + ","
                            else:
                                str1 = str1 + str(answerList[i][j] + 1)
                    sheet1.write(i, 0, str1)
            if item == '3':
                sheet1 = book.add_sheet('Jaccard')
                answerList = numpy.load(dirPosition + "/numpyDataDir/jaccard.npy")
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        str1 = str(answerList[i][0] + 1)
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                str1 = str1 + str(answerList[i][j] + 1) + ","
                            else:
                                str1 = str1 + str(answerList[i][j] + 1)
                    sheet1.write(i, 0, str1)
            if item == '4':
                sheet1 = book.add_sheet('次数矩阵')
                answerList = numpy.load(dirPosition + "/numpyDataDir/FLSF.npy")
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        str1 = str(answerList[i][0] + 1)
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                str1 = str1 + str(answerList[i][j] + 1) + ","
                            else:
                                str1 = str1 + str(answerList[i][j] + 1)
                    sheet1.write(i, 0, str1)
            if item == '5':
                sheet1 = book.add_sheet('神经网络（0,1矩阵）')
                answerList = numpy.load(dirPosition + "/numpyDataDir/networks1.npy")
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        str1 = str(answerList[i][0] + 1)
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                str1 = str1 + str(answerList[i][j] + 1) + ","
                            else:
                                str1 = str1 + str(answerList[i][j] + 1)
                    sheet1.write(i, 0, str1)
            if item == '6':
                sheet1 = book.add_sheet('神经网络（次数矩阵）')
                answerList = numpy.load(dirPosition + "/numpyDataDir/networks2.npy")
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        str1 = str(answerList[i][0] + 1)
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                str1 = str1 + str(answerList[i][j] + 1) + ","
                            else:
                                str1 = str1 + str(answerList[i][j] + 1)
                    sheet1.write(i, 0, str1)
            if item == '7':
                sheet1 = book.add_sheet('遗传算法')
                answerList = numpy.load(dirPosition + "/numpyDataDir/population.npy")
                temp = []
                i = 0
                for line in answerList:
                    j = 0
                    while j < len(line):
                        if line[j] in temp:
                            line.remove(line[j])
                        else:
                            j = j + 1
                    if len(line) > 0:
                        str1 = ""
                        if len(line) == 1:
                            str1 = str(line[0] + 1)
                            temp.append(line[0])
                        else:
                            for j in range(len(line)):
                                if j != len(line) - 1:
                                    str1 = str1 + str(line[j] + 1) + ","
                                    temp.append(line[j])
                                else:
                                    str1 = str1 + str(line[j] + 1)
                                    temp.append(line[j])
                        sheet1.write(i, 0, str1)
                        i = i + 1
                    if temp.__len__() > 20:
                        break
        book.save(dirPosition + '/answerExl.xls')
