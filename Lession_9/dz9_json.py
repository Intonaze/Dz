import json

with open('log_100.json', 'r') as f:
    data = json.load(f)

visits = {}
for i in data:
    visits[i['ip']] = visits.get(i['ip'], 0) + 1

print('Общий вклад топ-3 всех IP по количеству посещений: ', sum(sorted(visits.values())[-3:]) / sum(visits.values()) * 100, '%', sep='')
print('Уникальных IP, с которых на сайт заходили только 1 раз:', list(visits.values()).count(1))