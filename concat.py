import json

districts_file = 'districts.json'
villages_file = 'villages.json'

def get_pairing():
    final_set = []
    with open(districts_file) as dist_stream:
        with open(villages_file) as villages_stream:
            districts = json.load(dist_stream)
            villages = json.load(villages_stream)

            district_id_to_district = {}
            for _dist in districts:
                district_id_to_district[_dist['id']] = _dist

            for village in villages:
                final_set.append({
                    'village': village,
                    'district': district_id_to_district[village['district_id']]
                })

    return final_set

print(get_pairing()[:2])