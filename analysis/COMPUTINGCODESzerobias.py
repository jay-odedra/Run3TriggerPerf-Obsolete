from fileinput import close
import numpy as np
for i in range(1,9):
    directory = "/afs/cern.ch/user/j/jodedra/CMSSW_12_3_0_pre5/src/week113032022/Run3TriggerPerf-1/analysis/fulldatanames/fulldatafilenames" + str(i)+".txt"
    List = open(directory).readlines()
    mystring = str('root://cms-xrd-global.cern.ch/')
    List = [mystring + x for x in List ]



    f = open("/afs/cern.ch/user/j/jodedra/CMSSW_12_3_0_pre5/src/week113032022/Run3TriggerPerf-1/analysis/fullfilenamedatasetroot" + str(i)+".txt","w")
    for c in List:
        f.write(c)
    f.close()

#with open(r"C:\Users\odedr\filaaaanmes.txt","r") as file:
#    input = file.read()
#input.replace("\n", "")
#print(input)
