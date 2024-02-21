import json
import cc_classes
import cc_dat_utils

def load_json_data(json_file):
    with open(json_file) as file:
        data = json.load(file)
        return data

def monster_movement(monsters_data):
    monsters = [cc_classes.CCCoordinate(monster["x"], monster["y"])for monster in monsters_data]
    return cc_classes.CCMonsterMovementField(monsters)
def json_to_cc(json_data):
    level_pack = cc_classes.CCLevelPack()
    for level_data in json_data["levels"]:
        level = cc_classes.CCLevel()
        level.level_number = level_data["level_number"]
        level.time = level_data["time"]
        level.num_chips = level_data["num_chips"]
        level.upper_layer = level_data["upper_layer"]
        level.lower_layer = level_data["lower_layer"]

        for field_data in level_data["optional_fields"]:
            field = None
            if field_data["field_type"] == "mapTitle":
                field = cc_classes.CCMapTitleField(field_data["title"])
            elif field_data["field_type"] == "password":
                field = cc_classes.CCEncodedPasswordField(field_data["password"])
            elif field_data["field_type"] == "hint":
                field = cc_classes.CCMapHintField(field_data["hint"])
            elif field_data["field_type"] == "monsters":
                field = monster_movement(field_data["monsters"])
            else:
                print(f"Unknown field type: {field_data['field_type']}")

            if field is not None:
                level.add_field(field)
        level_pack.add_level(level)
    return level_pack

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file
json_file = "data/yihuapu_cc1.json"
json_data = load_json_data(json_file)
cc_level_pack = json_to_cc(json_data)
dat_file = "data/yihuapu_cc1.dat"
cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, dat_file)
