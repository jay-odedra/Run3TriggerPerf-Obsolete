import os 
import numpy as np
processedevents = int(os.environ["processedEvents"])
producedevents = int(os.environ["producedEvents"])
threads = float(os.environ["threads"])
totaljobtime = float(os.environ["totalJobTime"])
totaljobcpu = float(os.environ["totalJobCPU"])
totalsize = float(os.environ["totalSize"])
eventthroughput = float(os.environ["eventThroughput"])
avgeventtime = float(os.environ["avgEventTime"])
cpuefficiency= (totaljobcpu*100)/(threads*totaljobtime)
sizeperevent=(totalsize*1024/producedevents)
timeperevent=1/(eventthroughput)
filterefficiency=(producedevents)/(processedevents)

matchingefficiency=1

print("CPU EFFICIENCY : ", cpuefficiency,"%")
print("SIZE PER EVENT : ", sizeperevent,"KB")
print("TIME PER EVENT : ", timeperevent,"s")
print("FILTER EFFICIENCY : ", filterefficiency)

print("EVENTS PER LUMI SEC : ",8*3600*filterefficiency*matchingefficiency/timeperevent)