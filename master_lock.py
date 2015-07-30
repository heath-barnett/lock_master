__author__ = 'heath'
import pandas as pd

master = pd.read_csv('All_Rooms.csv',names=['Room','Desk','ID','Combo'],header=0)
master['Combo'] = master['Combo'].str.replace('\'','')
#print(master)

Chem1003A=[3,18,33,48,63,78,91,108,123,138,153,168]
Chem1003B=[9,24,39,54,69,84,99,114,129,144,159,174]
Chem1009A=[5,17,35,47,65,77,95,107,125,137,155,167]
Chem1009B=[8,20,38,50,68,80,98,110,128,140,158,170]
# orphans ?? 15,30,45,60,75,90,105,120,135,150,165,180
Chem1010A=[1,10,19,28,32,40,49,58,61,70,79,88,91,100,109,118,121,130,139,148,151,160,169,178]
Chem1010B=[2,7,16,25,34,43,52,59,62,67,76,85,94,103,112,119,124,133,142,149,154,163,172,179]
Chem1010C=[4,13,22,29,32,37,46,55,64,73,82,89,92,97,106,115,122,127,136,145,152,157,166,175]

room = master[master['Desk'].isin(Chem1010A) & (master['Room']==232)]
room = room[['Desk','ID','Combo']]
print(room.to_string(index=False))
