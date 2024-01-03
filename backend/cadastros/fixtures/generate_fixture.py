import json

MODEL_NAME = "cadastros.cidade"

with open('/home/carletto/Projetos/projeto_intranet_rest/backend/cadastros/fixtures/brazil-cities-states-en.json') as data_file:
	data = json.load(data_file)
	fixtures = []
	city_pk = 0

	for state_object in data['states']:
		state = state_object['uf']
		for city in state_object['cities']:
			city_pk = city_pk + 1
			fixture_object = {
				 "model": MODEL_NAME,
				 "pk":city_pk,
				 "fields":{	
					 "nome": city,
					 "estado": state
				 }
			}

			fixtures.append(fixture_object)

	fixture_data = json.dumps(fixtures)
	fixtures_file = open("city.json", "w")
	fixtures_file.write(fixture_data)
	fixtures_file.close()