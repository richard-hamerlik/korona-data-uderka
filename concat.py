import json
import csv

districts_file = 'districts.json'
villages_file = 'villages.json'
corona_file = 'pocet_pozitivnych_obce_24_09_2020-07_10_2020.csv'

def get_pairing():
    final_set = []
    with open(districts_file) as dist_stream:
        with open(villages_file) as villages_stream:
            with open(corona_file) as corona_stream:
                districts = json.load(dist_stream)
                villages = json.load(villages_stream)
                corona = csv.reader(corona_stream)

                district_id_to_district = {}
                for _dist in districts:
                    district_id_to_district[_dist['id']] = _dist

                for village in villages:
                    final_set.append({
                        'village': village,
                        'district': district_id_to_district[village['district_id']]
                    })

                return final_set

def dump_set_to_csv(_set, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        for obj in _set:
            writer.writerow([obj['village']['id'], obj['village']['fullname'], obj['district']['id'],obj['district']['name']])


dump_set_to_csv(get_pairing(), "pairs.csv")