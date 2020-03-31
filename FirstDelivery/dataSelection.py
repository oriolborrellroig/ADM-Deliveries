import os
import ndjson
import random as rand

PATH = './data/10000_each/'
NUMBER_OF_ROWS = 1000

data = []
filelist = os.listdir(PATH)
print(filelist)
if ("output.ndjson" in filelist): filelist.remove("output.ndjson")
print(filelist)
desti = open("./data/10000_each/output.ndjson", "w")

for file in filelist:
    with open(PATH + file) as f:
        # number_of_lines = len(f.readlines())
        acceptance = NUMBER_OF_ROWS/100000
        for line in f:
            l = ndjson.loads(line)
            # print('j')
            if (l[0]["recognized"]):
                randNumber = rand.random()
                # print(str(randNumber) + str(acceptance))
                if(randNumber <= acceptance):
                    data = data + l
                    desti.write(str(l[0]))
                    desti.write('\n')
        f.close()

print(len(data))