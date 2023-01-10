import csv
from pprint import pprint

suspicious_agent = {
    "ip": '',            # самый частовстречаемый ip в логах
    'fraction': 0,     # процент запросов с таким ip от общего кол-ва запросов
    'count': 0,         # число запросов с таким IP
    'last': {               # вложенный словарь с 2-мя полями
        'agent': '',     # последний user-agent для этого ip
        'timestamp': '', # последний timestap для этого ip
    }
}

with open('log_full.csv') as csvfile:
    ip = {}
    for i in csv.reader(csvfile):
        ip[i[1]] = ip.get(i[1], 0) + 1

most_often_ip = ''
cnt = 0
for key, value in ip.items():
    if cnt < value:
        most_often_ip = key
        cnt = value

suspicious_agent['ip'] = most_often_ip
suspicious_agent['count'] = ip[most_often_ip]
suspicious_agent['fraction'] = ip[most_often_ip] / sum(ip.values()) * 100

with open('log_full.csv') as csvfile:
    for i in csv.reader(csvfile):
        if i[1] == suspicious_agent['ip']:
            suspicious_agent['last']['agent'] = i[2]
            suspicious_agent['last']['timestamp'] = i[0]

pprint(suspicious_agent)