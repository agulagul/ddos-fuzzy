from sugeno import *
import pandas as pd

path = input("Masukkan nama file: ")
df = pd.read_csv(path)
destination = str(input("Masukkan IP Server: "))
df = df[df['Protocol'].isin(['ICMP' , 'IPv4'])]
df = df[df['Source'] != destination]
df = df[df['Destination'] == destination]
df.Time = df.Time.astype(int)
Z = []
for i in range(len(df.Time.unique())):
    time_group = df.groupby(['Time'])
    jml_source = len(time_group.Source.get_group(i).unique())
    u_source = derajat_source(jml_source)
    source = time_group.Source.get_group(i).unique()
    packet_length = 0
    source_group = df.groupby(['Time','Source'])
    for j in source:
        packet_length += source_group.get_group((i,j)).Length.sum()
    avg_length = packet_length / len(source)
    print(avg_length)
    u_length = derajat_length(avg_length)
    print(u_length.pendek, u_length.normal, u_length.panjang)
    jml_data = time_group['No.'].get_group(i).count()
    print(jml_data)
    u_jmldata = derajat_jmldata(jml_data)
    print(u_jmldata.sedikit, u_jmldata.banyak)
    alfa = []
    z = []
    alfa, z = inferensi(u_length, u_source, u_jmldata)
    print(''.join(str(alfa)))
    print(''.join(str(z)))
    Z.append(defuzzyikasi(alfa, z))

print(Z)
Z_class = []
for z in Z:
    if z < 0.5:
        Z_class.append("NOT_POD")
    else:
        Z_class.append("POD")

klasifikasi = ''
if Z_class.count('POD') < Z_class.count('NOT_POD'):
    klasifikasi = 'NOT_POD'
elif Z_class.count('POD') > Z_class.count('NOT_POD'):
    klasifikasi = 'POD'
else:
    klasifikasi = 'NOT_POD'