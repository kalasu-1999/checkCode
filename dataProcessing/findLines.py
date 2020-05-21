import numpy


# cPosition传入错误文件所在位置,如:/home/target.c
# dirPosition:/home
def findLines(cPosition, dirPosition):
    file = open(cPosition)
    lines = file.readlines()
    countList = []
    for i in range(lines.__len__()):
        if not (lines[i].startswith('#') or lines[i].startswith('//') or lines[i] == '' or lines[i] == '\n'):
            if not ('{' in lines[i] or '}' in lines[i]):
                countList.append(i)
    numpy.save(dirPosition + "/numpyDataDir/findLines.npy", countList)


if __name__ == '__main__':
    findLines("/home/kalasu/PycharmProjects/tot_info/target.c",
              "/home/kalasu/PycharmProjects/tot_info")
