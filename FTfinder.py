#-------------------------------------------------------------------------------
# Name:        Failed Test Finder
# Purpose:
#
# Author:      Liang-Huan chin
#
# Created:     09/23/2013
# Copyright:   (c) Leo Chin 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from time import gmtime, strftime
import socket as SOCKET
import platform as PF

def readPRF(prfFile):
    """
    this function read the _prf.txt and return the failed test number

    Input:
        fileName: _prf.txt includes full path

    Output:
        failed test name list

    Examples
    --------
      >>> fileNmae = "c:/gpqa/test_prf.txt"
      >>> key_value = ['TEST1', 'TEST4',...]
    """
    f = open(prfFile, 'r')
    testName = []
    for line in f:
        if line.find('TEST') > -1:
            token = line.split(' ')
            token2 = token[1].split('	')
            if str(token2).find("fail") > -1:
                testName.append(token2[0])
    return testName

def readModelPRF(prfFile):
    f = open(prfFile, 'r')
    testName = []
    for line in f:
        if line.find('TEST') > -1:
            token = line.split(' ')
            token2 = token[2].split('	')
            if str(token2).find("fail") > -1:
                testName.append(token2[0])
            print testName
    return testName

def writeResult(prfFile, tool=0):
    """
    this function search log.txt by the failed test name number
    Then write the $MSG log in to a summary text file

    Input:
        testPath: _prf.txt includes full path

    Output:
        Using report_file.write() to write the result directly to txt file
        Including the tool name, test number, and message log

    Examples
    --------
      >>> writeResult("c:/gpqa/test_prf.txt")
      >>> "FTs.txt"
    """
    if tool == 3:
        FT = readModelPRF(prfFile)
    else:
        FT = readPRF(prfFile)
    print FT
    if len(FT)==0:
        print "ALL PASS"
        report_file.write("ALL PASS\n")
    else:
        msg = ""
        logFile = prfFile.replace("prf", "log")
        f = open(logFile, 'r')
        for line in f:
            for test in FT:
                if line.find(test+":")>-1:
                    msg = line
                    for i in xrange(50):
                        check = f.next()
                        if check.find("$") != -1:
                            msg = msg + check
                        else:
                            break
                    print test
                    report_file.write(test+"\n")
                    print msg
                    report_file.write(msg)
    return 0

# specify the main path for new and old _prf.txt file and the sub path
mainPath = 'C:/gpqa/pytest/core/stat'
oldPath = 'C:/gpqa/pytest/core/stat'
subPath = ['analyzing_patterns',
           'mapping_clusters',
           'measuring_geographic_distributions',
           'model',
           'modeling_spatial_relationships',
           'rendering',
           'utilities']

# 7 tools
ap = ['generalg', 'globalmorani', 'incrementalsa', 'kfunction', 'nearestneighbor']
mc = ['cluster', 'gi', 'optimizedgi', 'partitional','similarity']
mgd = ['centralfeature', 'linear', 'meancenter', 'mediancenter', 'standarddistance', 'standardellipse']
model = ['statModelsTest1', 'statModelsTest2', 'statModelsTest3', 'statModelsTest4', 'statModelsTest5', 'statModelsTest6']
msr = ['exploratoryregression', 'explorecorrelations', 'generateswm', 'geographicallyweightedregression', 'networkswm', 'ols']
render = ['clusterrendered', 'collecteventsrendered', 'countrenderer', 'girendered', 'zrenderer']
util = ['calculatearea', 'calculatedistanceband', 'collectevents', 'exportxyv', 'swm2table']

# create a new text file named "FTs.txt" for the result
report_file = open('FTs.txt', 'w')
# record time, system name and platform info
report_file.write("File Generated : "+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
report_file.write("System Name : "+ SOCKET.gethostname()+"\n")
report_file.write("Platform Name : "+ PF.platform()+"\n\n\n")


# Search for the failed test in prf.txt and extract msg log from log.txt
for i in xrange(7):
    if i == 0:
        for tool in ap:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            writeResult(testPath)
            print tool
            report_file.write("--"*20+"\n")
    elif i == 1:
        for tool in mc:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            writeResult(testPath)
            print tool
            report_file.write("--"*20+"\n")
    elif i == 2:
        for tool in mgd:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            print tool
            writeResult(testPath)
            report_file.write("--"*20+"\n")
    elif i == 3:
        for tool in model:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            writeResult(testPath,3)
            print tool
            report_file.write("--"*20+"\n")
    elif i == 4:
        for tool in msr:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            writeResult(testPath)
            print tool
            report_file.write("--"*20+"\n")
    elif i == 5:
        for tool in render:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            writeResult(testPath)
            print tool
            report_file.write("--"*20+"\n")
    else:
        for tool in util:
            testPath = mainPath + '/'+subPath[i] + '/' + tool+ '/' + tool + '_prf.txt'
            report_file.write(tool+"\n")
            writeResult(testPath)
            print tool
            report_file.write("--"*20+"\n")

# close the result txt file
report_file.close()

