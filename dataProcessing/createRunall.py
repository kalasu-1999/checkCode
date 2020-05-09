import os


def getTestNumber(testPosition):
    file = os.listdir(testPosition)
    return file.__len__()


def createRunall(cPosition, testPosition):
    strTemp = cPosition
    cutList = strTemp.split('/')
    cStr = cutList.pop(cutList.__len__() - 1)
    positionStr = ""
    for item in cutList:
        positionStr = positionStr + item + '/'
    open(positionStr + 'runall.sh', 'w')
    for item in range(1, getTestNumber(testPosition) + 1):
        addRunall(cStr, positionStr, cPosition, testPosition, 't' + str(item), positionStr + '/testAnswerDir', item)
    os.system('sh dataProcessing/run.sh ' + positionStr)


def addRunall(cStr, positionStr, cPosition, testPosition, testName, outputsPosition, outputNumber):
    f = open(positionStr + 'runall.sh', 'a')
    f.write('echo ">>>>>>>>running test %s"\n' % (str(outputNumber)))
    val1 = '/'.join(cPosition.split('/')[0:-1]) + "/target.exe"
    val2 = testPosition + "/" + testName
    val4 = outputsPosition + "/t" + str(outputNumber)
    f.write(val1 + " < " + val2 + " > " + val4 + "\n")
    f.write('gcov ' + cStr + '\n')
    f.write('mv ' + cStr + '.gcov ' + outputsPosition + '/t' + str(outputNumber) + '.gcov\n')
    f.write('make remove\n')
    f.close()
