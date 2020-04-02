import json

with open('timeseries.json') as json_file:
    json_data = json.load(json_file)

csv = "Country"

for i in json_data['Burma']:
    csv += "," + i['date']
csv += "\n"
for i in json_data:
    sub_data = i
    print(i)
    for l in json_data[i]:
        print(l['confirmed'])
        sub_data += ","+str(l['confirmed'])
    csv += sub_data+"\n"

print(csv)
f = open("corona_day_date.csv", 'w')
f.write(csv)
f.close()
