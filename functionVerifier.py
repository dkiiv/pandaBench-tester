# todo: make this file automatically compare results data vs feed data when ran and spit out a pass / fail for the module
# convert only the messages we manipulate into binary, parse that data to verify ocelot did what we want
# make sure the other normal message's made it through the ocelot filter

import csv

GRA_Neu = 0x38A
mACC_GRA_Anziege = 0x56a
mACC_System = 0x368

with open('benchtestResults.csv', 'r') as resultData:
    reader = csv.reader(resultData)
    for row in reader:
        try:
            addr = hex(int(row[0]))
            dat = bin(int(row[1], 16)).ljust(66, '0')
            if addr == hex(GRA_Neu):
                #do some binary ops here to ensure proper ocelot function
                GRA_Kodierinfo = bin((int(dat, 2) >> 48) & 0b0000000000000001)
                GRA_Sender = bin((int(dat, 2) >> 44) & 0b00000000000000000011).ljust(4, '0')
                print("GRA_Kodierinfo: " + GRA_Kodierinfo)
                print("GRA_Sender: " + GRA_Sender)
            if addr == hex(mACC_GRA_Anziege):
                #do some binary ops here to ensure proper ocelot function
                pass
            if addr == hex(mACC_System):
                #do some binary ops here to ensure proper ocelot function
                pass
        except Exception as e:
            print("an exception occured" + str(e))