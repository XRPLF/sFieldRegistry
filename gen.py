import sys
import re
import json


capitalization_exceptions = {
    "NFTOKEN": "NFToken",
    "UNL": "UNL",
    "XCHAIN": "XChain",
    "ID": "ID",
    "AMM": "AMM",
}


def translate(inp):
    try:
        if re.search(r'^UINT', inp):
            if re.search(r'256|160|128', inp):
                return re.sub(r'UINT', 'Hash', inp)
            else:
                return re.sub(r'UINT', 'UInt', inp)
        if inp == 'OBJECT' or inp == 'ARRAY':
            return 'ST' + inp[0].upper() + inp[1:].lower()
        if inp == 'AMM':
            return inp
        if inp == 'ACCOUNT':
            return 'AccountID'
        if inp == 'LEDGERENTRY':
            return 'LedgerEntry'
        if inp == 'NOTPRESENT':
            return 'NotPresent'
        if inp == 'PATHSET':
            return 'PathSet'
        if inp == 'VL':
            return 'Blob'
        if inp == 'DIR_NODE':
            return 'DirectoryNode'
        if inp == 'PAYCHAN':
            return 'PayChannel'

        if re.split(r'_', inp):
            parts = re.split(r'_', inp)
            inp = ''
            for x in parts:
                if x in capitalization_exceptions:
                    inp += capitalization_exceptions[x]
                else:
                    inp += x[0].upper() + x[1:].lower()
            return inp
        return inp[0].upper() + inp[1:].lower()
    except Exception as e:
        raise e


def ttranslate(inp):
    try:
        if inp == 'REGULAR_KEY_SET':
            inp = 'SET_REGULAR_KEY'

        if inp == 'NICKNAME_SET':
            inp = 'NICK_NAME_SET'

        if inp == 'AMENDMENT':
            inp = 'ENABLE_AMENDMENT'

        if inp == 'FEE':
            inp = 'SET_FEE'

        if inp == 'SPINAL_TAP':
            inp = 'TICKET_CANCEL'

        if inp == 'HOOK_SET':
            inp = 'SET_HOOK'

        inp = re.sub(r'PAYCHAN', 'PAYMENT_CHANNEL', inp)

        if re.split(r'_', inp):
            parts = re.split(r'_', inp)
            inp = ''
            for x in parts:
                if x in capitalization_exceptions:
                    inp += capitalization_exceptions[x]
                else:
                    inp += x[0].upper() + x[1:].lower()
            return inp
        return inp[0].upper() + inp[1:].lower()
    except Exception as e:
        raise e


def unhex(x):
    x = x.strip()
    if x[0:2] == '0x':
        return int(x, 16)
    if x[0] == "'" and len(x) == 3:
        return ord(x[1])
    return x


def isVLEncoded(t):
    if t == 'VL' or t == 'ACCOUNT' or t == 'VECTOR256':
        return True
    return False


def isSerialized(t):
    if t == 'LEDGERENTRY' or t == 'TRANSACTION' or t == 'VALIDATION':
        return False
    return True


def isOne(t, v):
    if t == 'LEDGERENTRY' or t == 'TRANSACTION' or t == 'VALIDATION' or t == 'METADATA':
        return 1
    return v


def isSigningField(t):
    if t == 'notSigning':
        return False
    return True

def get_definitions(path: str):
    sfield_h_fn = path + '/protocol/SField.h'
    sfield_cpp_fn = path + '/protocol/impl/SField.cpp'
    ledgerformats_h_fn = path + '/protocol/LedgerFormats.h'
    ter_h_fn = path + '/protocol/TER.h'
    txformats_h_fn = path + '/protocol/TxFormats.h'

    sfield_h = open(sfield_h_fn).read()
    sfield_cpp = open(sfield_cpp_fn).read()
    ledgerformats_h = open(ledgerformats_h_fn).read()
    ter_h = open(ter_h_fn).read()
    txformats_h = open(txformats_h_fn).read()

    definitions = {}
    definitions['TYPES'] = {}
    definitions['TYPES']['Done'] = -1

    hits = re.findall(
        r'^ *STI_([^ ]*?) *= *([0-9-]+) *,?$', sfield_h, re.MULTILINE)
    for x in range(len(hits)):
        definitions['TYPES'][translate(hits[x][0])] = int(hits[x][1])

    definitions['LEDGER_ENTRY_TYPES'] = {}
    definitions['LEDGER_ENTRY_TYPES']['Invalid'] = -1

    hits = re.findall(r' *lt([A-Z_]+)[^\n=]*= *([^,]+),?$',
                      ledgerformats_h, re.MULTILINE)
    for x in range(len(hits)):
        if hits[x][0] == 'ANY':
            definitions['LEDGER_ENTRY_TYPES'][translate(hits[x][0])] = -3
        elif hits[x][0] == 'CHILD':
            definitions['LEDGER_ENTRY_TYPES'][translate(hits[x][0])] = -2
        else:
            definitions['LEDGER_ENTRY_TYPES'][translate(
                hits[x][0])] = unhex(hits[x][1])

    definitions['FIELDS'] = []
    definitions['FIELDS'] = [
        [
            "Generic",
            {
                "nth": 0,
                "isVLEncoded": False,
                "isSerialized": False,
                "isSigningField": False,
                "type": "Unknown"
            }
        ],
        [
            "Invalid",
            {
                "nth": -1,
                "isVLEncoded": False,
                "isSerialized": False,
                "isSigningField": False,
                "type": "Unknown"
            }
        ],
        [
            "ObjectEndMarker",
            {
                "nth": 1,
                "isVLEncoded": False,
                "isSerialized": True,
                "isSigningField": True,
                "type": "STObject"
            }
        ],
        [
            "ArrayEndMarker",
            {
                "nth": 1,
                "isVLEncoded": False,
                "isSerialized": True,
                "isSigningField": True,
                "type": "STArray"
            }
        ],
        [
            "hash",
            {
                "nth": 257,
                "isVLEncoded": False,
                "isSerialized": False,
                "isSigningField": False,
                "type": "Hash256"
            }
        ],
        [
            "index",
            {
                "nth": 258,
                "isVLEncoded": False,
                "isSerialized": False,
                "isSigningField": False,
                "type": "Hash256"
            }
        ],
        [
            "taker_gets_funded",
            {
                "nth": 258,
                "isVLEncoded": False,
                "isSerialized": False,
                "isSigningField": False,
                "type": "Amount"
            }
        ],
        [
            "taker_pays_funded",
            {
                "nth": 259,
                "isVLEncoded": False,
                "isSerialized": False,
                "isSigningField": False,
                "type": "Amount"
            }
        ]
    ]

    hits = re.findall(
        r'^ *CONSTRUCT_[^\_]+_SFIELD *\( *[^,\n]*,[ \n]*\"([^\"\n ]+)\"[ \n]*,[ \n]*([^, \n]+)[ \n]*,[ \n]*([0-9]+)(,.*?(notSigning))?', sfield_cpp, re.MULTILINE)
    for x in range(len(hits)):
        definitions['FIELDS'].append([
            hits[x][0],
            {
                "nth": int(isOne(hits[x][1], hits[x][2])),
                "isVLEncoded": isVLEncoded(hits[x][1]),
                "isSerialized": isSerialized(hits[x][1]),
                "isSigningField": isSigningField(hits[x][4]),
                "type": translate(hits[x][1]),
            }
        ])

    definitions['TRANSACTION_RESULTS'] = {}
    ter_h = re.sub(r'\[\[maybe_unused\]\]', '', ter_h)
    hits = re.findall(
        r'^ *((tel|tem|tef|ter|tes|tec)[A-Z_]+)( *= *([0-9-]+))? *,? *(\/\/[^\n]*)?$', ter_h, re.MULTILINE)
    upto = -1
    last = ""
    for x in range(len(hits)):
        if hits[x][3] != '':
            upto = int(hits[x][3])

        current = hits[x][1]
        if current != last and last != "":
            pass
        last = current

        definitions['TRANSACTION_RESULTS'][str(hits[x][0])] = upto
        upto += 1

    definitions['TRANSACTION_TYPES'] = {}

    hits = re.findall(
        r'^ *tt([A-Z_]+) *(\[\[[^\]]+\]\])? *= *([0-9]+) *,?.*$', txformats_h, re.MULTILINE)
    for x in range(len(hits)):
        definitions['TRANSACTION_TYPES'][ttranslate(
            hits[x][0])] = int(hits[x][2])

    return definitions
