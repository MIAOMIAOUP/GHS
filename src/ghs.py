import os
from typing import (
    List,
    Dict, Tuple)


def ghs(dirs: List[str], tbs: List[str] = []) -> Tuple[Dict[str, int], Dict[str, List[str]]]:
    _types: Dict[str, int] = {}
    _names: Dict[str, List[str]] = {}

    for _dir_path in dirs:
        for root, dirs, files in os.walk(_dir_path):
            for file in files:

                _name = os.path.splitext(file)[0]
                _type = os.path.splitext(file)[1]

                if _type not in tbs:
                    _full_path = root + os.sep + file
                    if _names.__contains__(_name):
                        _names[_name].append(_full_path)
                    else:
                        _names[_name] = [_full_path]
                if _types.__contains__(_type):
                    _types[_type] = _types[_type] + 1
                else:
                    _types[_type] = 1

    return _types, _names
