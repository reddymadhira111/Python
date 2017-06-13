import yaml

with open('manifest-dev.yml', 'r') as yml_file:
	data = yaml.load(yml_file)
print(data)

l = data['applications']

for i in l:
	for key in i:
		if key == 'env':
			d = i['env']
			d['uaa_service_name'] = 'cups-apm-uaa'

with open('manifest-dev.yml', 'w') as yml_file:
	yaml.dump(data, yml_file)

print(data)
