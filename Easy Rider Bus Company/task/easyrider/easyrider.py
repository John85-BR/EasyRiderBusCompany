import json

enter = input()
temp = json.loads(enter)
pattern_streets = r'([A-Z][a-z]+ )+(Street|Boulevard|Avenue|Road)$'
cont_dict = {
    "Start stops": [],
    "Transfer stops": [],
    "On demand": [],
    "Finish stops": []
}

lines_names_id = []
for item in temp:
    dict_temp = dict(item)
    for key, value in dict_temp.items():

        lines_names_id.append((dict_temp['stop_name'], dict_temp['bus_id']))
        if key == "stop_type":
            if value in ["S", "O", "F"]:
                if value == "S":
                    cont_dict["Start stops"].append(dict_temp['stop_name'])
                elif value == "F":
                    cont_dict["Finish stops"].append(dict_temp['stop_name'])
                elif value == "O":
                    cont_dict["On demand"].append(dict_temp['stop_name'])


list_names_set = set(lines_names_id)
for name, line in list_names_set:
    total_count = sum(string.count(name) for string in list_names_set)
    if total_count > 1:
        if name not in cont_dict["Transfer stops"]:
            cont_dict["Transfer stops"].append(name)

result = list(set(cont_dict["On demand"]) & (set(cont_dict["Transfer stops"]) | set(cont_dict["Start stops"]) | set(cont_dict["Finish stops"])))

if result:
    print(f"Wrong stop type: {sorted(result)}")
else:
    print("OK")
