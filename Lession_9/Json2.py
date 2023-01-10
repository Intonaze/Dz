import json
from pprint import pprint
with open('manager_sales.json', 'r') as f:
    data = json.load(f)
pprint(data)
sales = [0] * 10
for i in range(len(data)):
    for j in range(len(data[i]['cars'])):
        sales[i] += data[i]['cars'][j]['price']
name = sales.index(max(sales))
print(data[name]['manager'])
print(max(sales))