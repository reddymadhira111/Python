
import requests


response = requests.get('http://services.groupkt.com/state/get/USA/all')
data = response.json()
#print(data)

res = data['RestResponse']['result']
state = []

for i in res:
	state.append(i['name'])
	state.append(i['abbr'])

#print(state)

l = 'largest_city'
def out():
	for i in res:
			
		if i['name'] == s or i['abbr'] == s:
			if l in i.keys():
				print(i['largest_city'], i['capital'])
			else:
				print('largest city not exist in the state')

while True:
	s = input("Enter the state name:")
	if s in state:
		out()
	else:
		print('state is not in the data')

