import random
import string
import json
import os


def print_members(obj):
    members = dir(obj)
    json_str = json.dumps(members, indent=2)
    print(json_str)


def rand_str(str_len: int) -> str:
    str_source = string.ascii_letters + string.digits
    return ''.join([random.choice(str_source) for _ in range(str_len)])


print(f"Loaded: {os.environ['PYTHONSTARTUP']}")
