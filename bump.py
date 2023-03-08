
import sys
import json
from typing import List, Dict, Any


def read_file(path: str):
    with open(path, 'r') as f:
        return f.read()


def write_file(path: str, data: str):
    with open(path, 'w') as f:
        return f.write(data)


def read_json(path: str):
    with open(path) as json_file:
        return json.load(json_file)


def write_json(path: str, data: Dict[str, Any]):
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def get_list(tk: str, type_map: Dict[str, Any]):
    if tk in type_map:
        return [str(k) for k, _ in type_map[tk].items()]
    return []


IGNORE_LIST: List[str] = [
    'Done',
    'Unknown',
    'Transaction',
    'LedgerEntry',
    'Validation',
    'Metadata'
]


def run(definitions: Dict[str, Any], name: str):
    type_map: Dict[str, Any] = read_json('./map.json')
    new_type_map: Dict[str, Any] = {}
    for tk, tv in definitions['TYPES'].items():
        if tk in IGNORE_LIST:
            continue
        new_type_map[tk] = {}
        if tk not in [k for k, _ in type_map.items()]:
            continue
        for f in definitions['FIELDS']:
            type: str = f[0]
            nth: str = f[1]['nth']
            if tk != f[1]['type']:
                continue

            # PATCH FOR END OF OBJECT/ARRAY
            if tk == 'STObject':
                new_type_map[tk]["1"] = "|1|<EndOfObject>|Objects|n/a|"
            if tk == 'STArray':
                new_type_map[tk]["1"] = "|1|<EndOfArray>|Arrays|n/a|"

            new_type_map[tk][str(nth)] = {}

            # FIELDS
            if str(nth) not in get_list(tk, type_map):
                new_type_map[tk][str(nth)] = f'|{nth}|{type}|{name}|n/a|'
            else:
                new_type_map[tk][str(nth)] = type_map[tk][str(nth)]

    output_value: str = ''
    output_value: str = """
# SFCode Registry Tables

## How to use

1. If you are working on an Amendment to the XRP Ledger (or a sidechain) and you need additional serialized fields then you should register them here to avoid clobbering others.
2. Register by opening a PR against this repo with your proposed registration as changes to the tables below. Provided the reservations are reasonable these will be accepted.

## Quick Bump

You can use the quick bump if you already have the definitions file or a rippled build

python3 bump.py | action | name | path

`python3 bump.py definitions Hooks ./definitions.json`
`python3 bump.py rippled Hooks ./rippled`

This will update the `README.md` and the `map.json` file.

3. If your code is already in use then enter it into the `used by` column otherwise use the `reserved by` column. Be descriptive but terse in the `reserved by` field. Other developers should understand why this code is being reserved.

"""
    for k, v in new_type_map.items():
        type_nth: str = definitions['TYPES'][k]
        output_value += f'## {k.upper()}'
        output_value += '\n'
        output_value += f'Type {type_nth}'
        output_value += '\n'
        output_value += """
|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
"""
        sorted_fields = {k: v for k, v in sorted(v.items(), key=lambda item: int(item[0]))}
        for _, iv in sorted_fields.items():
            output_value += iv
            output_value += '\n'
            iv = None

        output_value += '\n'
        output_value += '\n'

        new_type_map[k] = sorted_fields

    write_file('./README.md', output_value)
    write_json('./map.json', new_type_map)


def type_v_lookup(v: str):
    if v == 'UINT8':
        return 'UInt8'
    if v == 'UINT16':
        return 'UInt16'
    if v == 'UINT32':
        return 'UInt32'
    if v == 'UINT64':
        return 'UInt64'
    if v == 'UINT128':
        return 'Hash128'
    if v == 'UINT160':
        return 'Hash160'
    if v == 'UINT256':
        return 'Hash256'
    if v == 'AMOUNT':
        return 'Amount'
    if v == 'VL':
        return 'Blob'
    if v == 'ACCOUNT':
        return 'AccountID'
    if v == 'VECTOR256':
        return 'Vector256'
    if v == 'PATHSET':
        return 'PathSet'
    if v == 'OBJECT':
        return 'STObject'
    if v == 'ARRAY':
        return 'STArray'
    if v == 'LEDGERENTRY':
        return 'LedgerEntry'
    if v == 'TRANSACTION':
        return 'Transaction'
    if v == 'VALIDATION':
        return 'Validation'
    if v == 'METADATA':
        return 'Metadata'


def num_v_lookup(v: str):
    if v == 'UINT8':
        return 16
    if v == 'UINT16':
        return 1
    if v == 'UINT32':
        return 2
    if v == 'UINT64':
        return 3
    if v == 'UINT128':
        return 4
    if v == 'UINT160':
        return 17
    if v == 'UINT256':
        return 5
    if v == 'AMOUNT':
        return 6
    if v == 'VL':
        return 7
    if v == 'ACCOUNT':
        return 8
    if v == 'VECTOR256':
        return 19
    if v == 'PATHSET':
        return 18
    if v == 'OBJECT':
        return 14
    if v == 'ARRAY':
        return 15
    if v == 'LEDGERENTRY':
        return 10002
    if v == 'TRANSACTION':
        return 10001
    if v == 'VALIDATION':
        return 10003
    if v == 'METADATA':
        return 10004


def run_rippled(path: str, amendment: str):
    # create an empty dictionary
    definitions = {}
    definitions["TYPES"] = {}
    definitions["FIELDS"] = {}

    # open the cpp file
    with open(path) as f:
        # loop over each line
        fields: List[Dict[str, Any]] = []
        for line in f.readlines():
            line = line.strip()
            line = line.replace('"', '')
            line = line.replace("'", '')
            line = line.replace(");", '')
            if line.startswith("CONSTRUCT_UNTYPED_SFIELD"):
                line = line.replace("CONSTRUCT_UNTYPED_SFIELD(", '')
                line_parts = line.split(",")
                sf_type: str = line_parts[1].strip()
                name: str = type_v_lookup(line_parts[2].strip())
                value: str = line_parts[3].strip()
                def_arr = [sf_type, {"nth": int(value), "type": name}]
                fields.append(def_arr)
                if name not in definitions["TYPES"]:
                    definitions["TYPES"][f"{name}"] = num_v_lookup(
                        line_parts[2].strip())
            elif line.startswith("CONSTRUCT_TYPED_SFIELD"):
                line = line.replace("CONSTRUCT_TYPED_SFIELD(", '')
                line_parts = line.split(",")
                sf_type: str = line_parts[1].strip()
                name: str = type_v_lookup(line_parts[2].strip())
                value: str = line_parts[3].strip()
                def_arr = [sf_type, {"nth": int(value), "type": name}]
                fields.append(def_arr)
                if name not in definitions["TYPES"]:
                    definitions["TYPES"][f"{name}"] = num_v_lookup(
                        line_parts[2].strip())

        definitions["FIELDS"] = fields

    run(definitions, amendment)


action_list: List[str] = ['definitions', 'rippled']
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python3 bump.py <action> <amendment> <path>"
        )
        sys.exit()

    action: str = sys.argv[1]
    if action not in action_list:
        print(f"Usage: action must be {[f' {i}' for i in action_list]}")
        sys.exit()

    amendment: str = sys.argv[2]
    path: str = sys.argv[3]
    if path[-1] == "/":
        print("Path Usage: app/ripple - no forwardslash")
        sys.exit()

    try:
        if action == 'definitions':
            definitions: Dict[str, Any] = read_json(path)
            run(definitions, amendment)
        if action == 'rippled':
            r_path: str = path + '/src/ripple/protocol/impl/SField.cpp'
            run_rippled(r_path, amendment)
    except Exception as e:
        print(e)
