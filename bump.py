import os
import sys
import json
from typing import List, Dict, Any


def read_file(path: str):
    with open(path, "r") as f:
        return f.read()


def write_file(path: str, data: str):
    with open(path, "w") as f:
        return f.write(data)


def read_json(path: str):
    with open(path) as json_file:
        return json.load(json_file)


def write_json(path: str, data: Dict[str, Any]):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)


def get_list(tk: str, data: Dict[str, Any]):
    if tk in data:
        return [str(k) for k, _ in data[tk].items()]
    return []


IGNORE_LIST: List[str] = [
    "Done",
    "Unknown",
    "Transaction",
    "LedgerEntry",
    "Validation",
    "Metadata",
]

is_release: bool = bool(os.environ.get("RELEASE")) or False
is_debug: bool = bool(os.environ.get("DEBUG")) or False
is_reset: bool = bool(os.environ.get("RESET")) or False


def run(definitions: Dict[str, Any], name: str):
    types: Dict[str, Any] = read_json("./map.json")["types"]
    type_map: Dict[str, Any] = read_json("./map.json")["type_map"]
    new_type_map: Dict[str, Any] = {}
    for tk, tv in definitions["TYPES"].items():
        if tk in IGNORE_LIST:
            continue

        new_type_map[tk] = {}
        try:
            type_map[tk]
        except Exception as e:
            types[tk] = tv
            if is_debug:
                print(f"TYPE ADDED: {e}")

        if tk not in [k for k, _ in type_map.items()]:
            continue

        # definitions to map
        for f in definitions["FIELDS"]:
            type: str = f[0]
            nth: str = f[1]["nth"]

            if tk != f[1]["type"]:
                continue

            new_type_map[tk][str(nth)] = {}

            if str(nth) not in get_list(tk, type_map):
                new_type_map[tk][str(nth)] = f"|{nth}|{type}|{name}|n/a|"
            else:
                old_type = type_map[tk][str(nth)].split("|")[2]
                if old_type != type:
                    print(
                        f"TYPES: Merge conflict for {type}. {old_type} already exists at {nth}."
                    )
                    response = (
                        input(
                            f"Do you want to overwrite `{old_type}`? (yes/no) "
                        ).lower()
                        if not is_release
                        else "no"
                    )
                    if response == "yes":
                        new_type_map[tk][f"{nth}"] = f"|{nth}|{type}|{name}|n/a|"
                    else:
                        raise KeyboardInterrupt(
                            f"Please update `{old_type}` at {nth} and try again."
                        )
                else:
                    new_type_map[tk][str(nth)] = type_map[tk][str(nth)]

        # map to map
        if not is_reset:
            for k, _ in type_map[tk].items():
                if str(k) not in get_list(tk, new_type_map):
                    old_type = type_map[tk][str(k)].split("|")[2]
                    old_amendment = type_map[tk][str(k)].split("|")[3]
                    if is_debug:
                        print(
                            f"MISSING FIELD: {tk} - {old_type} - {k} - {old_amendment}"
                        )
                    new_type_map[tk][str(k)] = type_map[tk][str(k)]

    if not is_reset:
        for k, _ in type_map.items():
            if str(k) not in new_type_map:
                if is_debug:
                    print(f"MISSING TYPE: {k}")
                new_type_map[str(k)] = type_map[str(k)]

    result_map: Dict[str, Any] = read_json("./map.json")["result_map"]
    new_result_map: Dict[str, Any] = {}
    for rk, rv in definitions["TRANSACTION_RESULTS"].items():
        # TRANSACTION_RESULTS
        if str(rv) not in result_map:
            new_result_map[str(rv)] = f"|{rv}|{rk}|{name}|n/a|"
        else:
            old_result = result_map[str(rv)].split("|")[2]
            if old_result != rk:
                print(
                    f"TRANSACTION_RESULTS: Merge conflict for {rk}. {old_result} already exists at {rv}."
                )
                response = (
                    input(
                        f"Do you want to overwrite the `{old_result}` at {rv}? (yes/no) "
                    ).lower()
                    if not is_release
                    else "no"
                )
                if response == "yes":
                    new_result_map[str(rv)] = f"|{rv}|{rk}|{name}|n/a|"
                else:
                    raise KeyboardInterrupt(
                        f"Please update `{old_result}` at {rv} and try again."
                    )
            else:
                new_result_map[str(rv)] = result_map[str(rv)]

    # map to map
    if not is_reset:
        for k, _ in result_map.items():
            if str(k) not in new_result_map:
                old_result = result_map[str(k)].split("|")[2]
                old_amendment = result_map[str(k)].split("|")[3]
                if is_debug:
                    print(
                        f"MISSING TRANSACTION RESULT: {old_result} - {k} - {old_amendment}"
                    )
                new_result_map[str(k)] = result_map[str(k)]

    entry_map: Dict[str, Any] = read_json("./map.json")["entry_map"]
    new_entry_map: Dict[str, Any] = {}
    for lek, lev in definitions["LEDGER_ENTRY_TYPES"].items():
        if str(lev) not in entry_map:
            new_entry_map[str(lev)] = f"|{lev}|{lek}|{name}|n/a|"
        else:
            old_ledger_entry = entry_map[str(lev)].split("|")[2]
            if old_ledger_entry != lek:
                print(
                    f"LEDGER_ENTRY_TYPES: Merge conflict for {lek}. {old_ledger_entry} already exists at {lev}."
                )
                response = (
                    input(
                        f"Do you want to overwrite the `{old_ledger_entry}` at {lev}? (yes/no) "
                    ).lower()
                    if not is_release
                    else "no"
                )
                if response == "yes":
                    new_entry_map[str(lev)] = f"|{lev}|{lek}|{name}|n/a|"
                else:
                    raise KeyboardInterrupt(
                        f"Please update `{old_ledger_entry}` at {lev} and try again."
                    )
            else:
                new_entry_map[str(lev)] = entry_map[str(lev)]

    if not is_reset:
        for k, _ in entry_map.items():
            if str(k) not in new_entry_map:
                if is_debug:
                    print(f"MISSING LEDGER ENTRY: {k}")
                new_entry_map[str(k)] = entry_map[str(k)]

    tt_map: Dict[str, Any] = read_json("./map.json")["tt_map"]
    new_tt_map: Dict[str, Any] = {}
    for lek, lev in definitions["TRANSACTION_TYPES"].items():
        if str(lev) not in tt_map:
            new_tt_map[str(lev)] = f"|{lev}|{lek}|{name}|n/a|"
        else:
            old_tt = tt_map[str(lev)].split("|")[2]
            if old_tt != lek:
                print(
                    f"TRANSACTION_TYPES: Merge conflict for {lek}. {old_tt} already exists at {lev}."
                )
                response = (
                    input(
                        f"Do you want to overwrite the `{old_tt}` at {lev}? (yes/no) "
                    ).lower()
                    if not is_release
                    else "no"
                )
                if response == "yes":
                    new_tt_map[str(lev)] = f"|{lev}|{lek}|{name}|n/a|"
                else:
                    raise KeyboardInterrupt(
                        f"Please update `{old_tt}` at {lev} and try again."
                    )
            else:
                new_tt_map[str(lev)] = tt_map[str(lev)]

    if not is_reset:
        for k, _ in tt_map.items():
            if str(k) not in new_tt_map:
                if is_debug:
                    print(f"MISSING TT: {k}")
                new_tt_map[str(k)] = tt_map[str(k)]

    # return

    output_value: str = """
# SFCode Registry Tables

## How to use

1. If you are working on an Amendment to the XRP Ledger (or a sidechain) and you need additional serialized fields then you should register them here to avoid clobbering others.
2. Register by opening a PR against this repo with your proposed registration as changes to the tables below. Provided the reservations are reasonable these will be accepted.
3. If your code is already in use then enter it into the `used by` column otherwise use the `reserved by` column. Be descriptive but terse in the `reserved by` field. Other developers should understand why this code is being reserved.

## Bump Script

You can use the bump script if you already have the definitions file or a rippled build. The script will merge your definition with this repo.

python3 bump.py | action | name | path

- `python3 bump.py definitions XLS30 ./definitions.json`

If you would like to know what sfields your rippled build is missing then run with:

- `DEBUG=True python3 bump.py XLS30 ./definitions.json`


"""
    for k, v in new_type_map.items():
        if len(v.items()) == 0:
            continue
        type_nth: str = types[k]
        output_value += f"## {k.upper()}"
        output_value += "\n"
        output_value += f"Type {type_nth}"
        output_value += "\n"
        output_value += """
|Field Code|Field Name|Used by|Reserved by|
|-|-|-|-|
"""
        sorted_fields = {
            k: v for k, v in sorted(v.items(), key=lambda item: int(item[0]))
        }
        for _, iv in sorted_fields.items():
            output_value += iv
            output_value += "\n"
            iv = None

        output_value += "\n"
        output_value += "\n"

        new_type_map[k] = sorted_fields

    output_value += f"## TRANSACTION RESULTS" + "\n"
    output_value += "\n"
    output_value += """
|Response Code|Response Name|Used by|Reserved by|
|-|-|-|-|
"""
    sorted_results = {
        k: v for k, v in sorted(new_result_map.items(), key=lambda item: int(item[0]))
    }
    for k, v in sorted_results.items():
        output_value += v
        output_value += "\n"
        v = None

    output_value += "\n"
    output_value += "\n"

    output_value += f"## TRANSACTION TYPES" + "\n"
    output_value += "\n"
    output_value += """
|Type Code|Tx Name|Used by|Reserved by|
|-|-|-|-|
"""
    sorted_tts = {
        k: v for k, v in sorted(new_tt_map.items(), key=lambda item: int(item[0]))
    }
    for k, v in sorted_tts.items():
        output_value += v
        output_value += "\n"
        v = None

    output_value += "\n"
    output_value += "\n"

    output_value += f"## LEDGER ENTRY TYPES" + "\n"
    output_value += "\n"
    output_value += """
|Type Code|Entry Name|Used by|Reserved by|
|-|-|-|-|
"""
    sorted_entries = {
        k: v for k, v in sorted(new_entry_map.items(), key=lambda item: int(item[0]))
    }
    for k, v in sorted_entries.items():
        output_value += v
        output_value += "\n"
        v = None

    output_value += "\n"
    output_value += "\n"

    write_file("./README.md", output_value)
    write_json(
        "./map.json",
        {
            "types": types,
            "type_map": new_type_map,
            "result_map": sorted_results,
            "entry_map": sorted_entries,
            "tt_map": sorted_tts,
        },
    )


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 bump.py <amendment> <path>")
        sys.exit()

    amendment: str = sys.argv[1]
    path: str = sys.argv[2]
    if path[-1] == "/":
        print("Path Usage: app/ripple - no forwardslash")
        sys.exit()

    try:
        definitions: Dict[str, Any] = read_json(path)
        run(definitions, amendment)
    except Exception as e:
        raise e
