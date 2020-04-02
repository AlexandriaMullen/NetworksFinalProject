from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.figure(figsize=(30,15))
m = Basemap(projection='cyl',
            llcrnrlat = -90,
            llcrnrlon = -180,
            urcrnrlat = 90,
            urcrnrlon = 180,
            resolution='l')

m.drawcoastlines()
m.drawcountries(linewidth=2)
plt.title('Routing Cities')
m.bluemarble()

latDict = {}
lonDict={}

with open("latarray.txt") as f:
    for line in f:
        (key, val) = line.split(" : ")
        line = line.strip('\n')
        latDict[key] = float(val)
with open("longarray.txt") as f:
    for line in f:
        (key, val) = line.split(" : ")
        line = line.strip('\n')
        lonDict[key] = float(val)
        
def route(a,b):
    m.drawgreatcircle(lonDict.get(a),latDict.get(a),lonDict.get(b),latDict.get(b),linewidth=4,color='b')
    
route('French Polynesia','Mexico')
route('Algeria','Australia')
route('South Korea','France')

plt.show()
