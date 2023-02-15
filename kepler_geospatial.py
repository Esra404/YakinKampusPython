from keplergl import KeplerGl
map_1 =KeplerGl(heigh=900)
with open ('earthquake.csv ','r') as f:
    csvData=f.read()
map_1.add_data(data=csvData,name='data_1')
print(map_1)