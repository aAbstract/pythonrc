import random
import string
import json
import os


conv_json_obj: dict = {}


def print_members(obj):
    members = dir(obj)
    json_str = json.dumps(members, indent=2)
    print(json_str)


def rand_str(str_len: int) -> str:
    str_source = string.ascii_letters + string.digits
    return ''.join([random.choice(str_source) for _ in range(str_len)])


def convs_list(key: str = None, rand: bool = False) -> list[str]:
    if key == None:
        print(list(conv_json_obj.keys()))
        return

    key_parts = key.split('.')
    if len(key_parts) == 1:
        part_1 = key_parts[0]
        part_2_dict: dict = conv_json_obj[part_1]
        part_2_keys = list(part_2_dict.keys())
        print(part_2_keys)

        if rand:
            print('=' * 100)
            print(f"CHOICE: {random.choice(part_2_keys)}")
            print('=' * 100)
        return

    if len(key_parts) == 2:
        part_1, part_2 = key_parts
        vals_list = conv_json_obj[part_1][part_2]
        for q in vals_list:
            print(q)

        if rand:
            print('=' * 100)
            print(f"CHOICE: {random.choice(vals_list)}")
            print('=' * 100)
        return


def gen_convs_graph(top_key: str):
    # TODO: using AI generate knowledge graph from convs.json file
    pass


print(f"Loaded: {os.environ['PYTHONSTARTUP']}")

with open('pythonrc_data/convs.json', 'r') as f:
    conv_json_obj = json.loads(f.read())
    print("Loaded conv.json file")

# print runtime symbols
print(json.dumps([func for func in dir() if callable(globals()[func]) and not func.startswith("__")], indent=2))
