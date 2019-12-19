from sugeno import *
from report import *
import webbrowser
import pandas as pd

path = input("Masukkan nama file: ")
df = pd.read_csv(path)
destination = str(input("Masukkan IP Server: "))
df = df[df['Protocol'].isin(['ICMP', 'IPv4'])]
df = df[df['Source'] != destination]
df = df[df['Destination'] == destination]
df.Time = df.Time.astype(int)
report_dict = {
    'interval(second)' : [],
    'attacker_count' : [],
    'attacker_ip' : [],
    'average_length' : [],
    'packet_sent' : [],
    'class' : []
}
Z = []
for i in range(len(df.Time.unique())):
    report_dict['interval(second)'].append(i)
    time_group = df.groupby(['Time'])
    jml_source = len(time_group.Source.get_group(i).unique())
    report_dict['attacker_count'].append(jml_source)
    u_source = derajat_source(jml_source)
    source = time_group.Source.get_group(i).unique()
    report_dict['attacker_ip'].append(source)
    packet_length = 0
    source_group = df.groupby(['Time', 'Source'])
    for j in source:
        packet_length += source_group.get_group((i, j)).Length.sum()
    avg_length = packet_length / len(source)
    report_dict['average_length'].append(int(avg_length))
    # print(avg_length)
    u_length = derajat_length(avg_length)
    # print(u_length.pendek, u_length.normal, u_length.panjang)
    jml_data = time_group['No.'].get_group(i).count()
    report_dict['packet_sent'].append(jml_data)
    # print(jml_data)
    u_jmldata = derajat_jmldata(jml_data)
    # print(u_jmldata.sedikit, u_jmldata.banyak)
    alfa = []
    z = []
    alfa, z = inferensi(u_length, u_source, u_jmldata)
    # print(''.join(str(alfa)))
    # print(''.join(str(z)))
    defuzzy = defuzzyikasi(alfa, z)
    if defuzzy < 0.5:
        report_dict['class'].append("NOT_POD")
    else:
        report_dict['class'].append("POD")
    Z.append(defuzzy)
# print(Z)
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

report = pd.DataFrame(report_dict)
output = path.split('.')[0] + '-report.html'
to_html_pretty(report, output, path, destination, klasifikasi)
webbrowser.open(output, new=2)