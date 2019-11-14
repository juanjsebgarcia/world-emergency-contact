import json

def load_data():
    json_file = open('emergency-contacts.json', 'r').read()
    return json.loads(json_file)


def save_data(countries_dict):
    with open('emergency-contacts.json', 'w') as outfile:
        json.dump(countries_dict, outfile, indent=4, sort_keys=True)

    with open('dist/emergency-contacts.min.json', 'w') as outfile:
        json.dump(countries_dict, outfile, separators=(',', ':'), sort_keys=True)
