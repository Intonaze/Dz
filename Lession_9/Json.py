from string import ascii_lowercase
import json
d = {ascii_lowercase[i] : i + 1 for i in range(len(ascii_lowercase))}
json_data = json.dumps(d)
print(json_data)