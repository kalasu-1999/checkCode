# -*- coding: UTF-8 -*-
import os


# 创建Makefile文件到指定路径，cName为c文件文件名，不包含后缀名，cPosition为目标路径
def createMakeFile(cPosition):
    cutList = cPosition.split('/')
    cName = cutList.pop(cutList.__len__() - 1)
    cName = cName[0:cName.__len__() - 2]
    positionStr = ""
    for item in cutList:
        positionStr = positionStr + item + '/'
    MakeFile = open(positionStr + "Makefile", "w")
    MakeFile.write("GCOV_FLAGS=-fprofile-arcs -ftest-coverage -lm\n")
    MakeFile.write("CFLAGS+=$(GCOV_FLAGS)\n")
    MakeFile.write("LDFLAGS+=-lpthread $(GCOV_FLAGS)\n")
    MakeFile.write("target=target.exe\n")
    MakeFile.write("target.exe:" + cName + ".o\n")
    MakeFile.write("\t$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)\n")
    MakeFile.write("%.o:%.c\n")
    MakeFile.write("\t$(CC) -g -c $^ -o $@  $(CFLAGS) $(DEFINES)\n")
    MakeFile.write("remove:\n")
    MakeFile.write("\trm -rf *.gcda\n")
    MakeFile.write(".PHONY : clean\n")
    MakeFile.write("clean:\n")
    MakeFile.write("\trm -rf *.o\n")
    MakeFile.write("\trm -rf $(target)\n")
    MakeFile.write("\trm -rf  *.gcov *.gcda *.gcno\n")
    os.system('sh dataProcessing/startMake.sh ' + positionStr)
