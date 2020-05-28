# -*- coding: UTF-8 -*-
import numpy
import xlwt


def lineFilter(dirPosition, answerList):
    gcovMap = numpy.load(dirPosition + "/numpyDataDir/gcov1.npy")
    answer = numpy.load(dirPosition + "/numpyDataDir/answerNumpy.npy")
    for i in range(answerList.__len__()):
        for j in range(answerList[i].__len__()):
            flag = 0
            for k in range(gcovMap.__len__()):
                if answer[k] == 0 and gcovMap[k][answerList[i][j]] == 1:
                    flag = 1
                    break
            if flag == 0:
                answerList[i][j] = -1
    resultList = []
    for i in range(answerList.__len__()):
        temp = []
        for j in range(answerList[i].__len__()):
            if answerList[i][j] != -1:
                temp.append(answerList[i][j])
        if temp.__len__() != 0:
            resultList.append(temp)
    return resultList


def matome(dirPosition, tempList):
    findLines = numpy.load(dirPosition + "/numpyDataDir/findLines.npy")
    if len(tempList) != 0:
        book = xlwt.Workbook(encoding='UTF-8')
        for item in tempList:
            if item == '1':
                sheet1 = book.add_sheet('Tarantula')
                answerList = numpy.load(dirPosition + "/numpyDataDir/tarantula.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
            elif item == '2':
                sheet1 = book.add_sheet('Ochiai')
                answerList = numpy.load(dirPosition + "/numpyDataDir/ochiai.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
            elif item == '3':
                sheet1 = book.add_sheet('Jaccard')
                answerList = numpy.load(dirPosition + "/numpyDataDir/jaccard.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
            elif item == '4':
                sheet1 = book.add_sheet('次数矩阵')
                answerList = numpy.load(dirPosition + "/numpyDataDir/FLSF.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
            elif item == '5':
                sheet1 = book.add_sheet('神经网络（0,1矩阵）')
                answerList = numpy.load(dirPosition + "/numpyDataDir/networks1.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
            elif item == '6':
                sheet1 = book.add_sheet('神经网络（次数矩阵）')
                answerList = numpy.load(dirPosition + "/numpyDataDir/networks2.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
            elif item == '7':
                sheet1 = book.add_sheet('遗传算法')
                answerList = numpy.load(dirPosition + "/numpyDataDir/population.npy")
                answerList = lineFilter(dirPosition, answerList)
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
                            try:
                                str1 = str(findLines[line[0]] + 1)
                                temp.append(line[0])
                            except IndexError:
                                print("IndexError")
                        else:
                            for j in range(len(line)):
                                if j != len(line) - 1:
                                    try:
                                        str1 = str1 + str(findLines[line[j]] + 1) + ","
                                        temp.append(line[j])
                                    except IndexError:
                                        print("IndexError")
                                else:
                                    try:
                                        str1 = str1 + str(findLines[line[j]] + 1)
                                        temp.append(line[j])
                                    except IndexError:
                                        print("IndexError")
                        if str1 != "":
                            sheet1.write(i, 0, str1)
                        i = i + 1
                    if temp.__len__() > 20:
                        break
            elif item == '8':
                sheet1 = book.add_sheet('Clustering')
                answerList = numpy.load(dirPosition + "/numpyDataDir/clustering.npy")
                answerList = lineFilter(dirPosition, answerList)
                for i in range(0, len(answerList)):
                    str1 = ""
                    if len(answerList[i]) == 1:
                        try:
                            str1 = str(findLines[answerList[i][0]] + 1)
                        except IndexError:
                            print("IndexError")
                    else:
                        for j in range(0, len(answerList[i])):
                            if j != len(answerList[i]) - 1:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1) + ","
                                except IndexError:
                                    print("IndexError")
                            else:
                                try:
                                    str1 = str1 + str(findLines[answerList[i][j]] + 1)
                                except IndexError:
                                    print("IndexError")
                    if str1 != "":
                        sheet1.write(i, 0, str1)
        book.save(dirPosition + '/answerExl.xls')
