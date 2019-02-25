import matplotlib.pyplot as plt
import pymongo
import pandas as pd


url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

newdb1 = mydb["Kampus"]                                
newcol1 = newdb1["Dosen"]
newcol2 = newdb1["Mahasiswa"]

dosen = []
mahasiswa = []

pD = []
pM = []
for data in newcol1.find():                            
    dosen.append(data)

for data in newcol2.find():
    mahasiswa.append(data)

for data in dosen:
    dosen1 = {
        'asal': data['asal'],
        'nama': data['nama'],
        'status': 'dosen',
        'usia': int(data['usia'])
    }
    pD.append(dosen1)

for data in mahasiswa:
    mahasiswa1 = {
        'asal': data['asal'],
        'nama': data['nama'],
        'status': 'mahasiswa',
        'usia': int(data['usia'])
    }
    pM.append(mahasiswa1)

df = pd.DataFrame(pD)
df2 = pd.DataFrame(pM)

plt.bar(df['nama'],df['usia'])
plt.bar(df2['nama'],df2['usia'])
plt.grid(True)
plt.legend(['Dosen','Mahasiswa'])
plt.title('Usia Warga Kampus')
plt.show()