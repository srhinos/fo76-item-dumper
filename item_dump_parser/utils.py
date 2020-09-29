import json
import re
from datetime import datetime, timezone
from operator import attrgetter


def load_json(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return json.loads(f.read())

    except IOError as e:
        print("Error loading", filename, e)
        return []


def load_file(filename):
    try:
        with open(filename) as f:
            results = []
            for line in f:
                line = line.strip()
                if line:
                    results.append(line)

            return results

    except IOError as e:
        print("Error loading", filename, e)
        return []


def write_file(filename, contents):
    with open(filename, "w") as f:
        for item in contents:
            f.write(str(item))
            f.write("\n")


def write_json(filename, contents):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(contents, indent=2))


def datetime_to_utc_ts(dt):
    return dt.replace(tzinfo=timezone.utc).timestamp()


def find(predicate, seq):
    for element in seq:
        if predicate(element):
            return element
    return None


def get(iterable, **attrs):

    # global -> local
    _all = all
    attrget = attrgetter

    # Special case the single element call
    if len(attrs) == 1:
        k, v = attrs.popitem()
        pred = attrget(k.replace("__", "."))
        for elem in iterable:
            if pred(elem) == v:
                return elem
        return None

    converted = [
        (attrget(attr.replace("__", ".")), value) for attr, value in attrs.items()
    ]

    for elem in iterable:
        if _all(pred(elem) == value for pred, value in converted):
            return elem
    return None


def _unique(iterable):
    seen = set()
    adder = seen.add
    return [x for x in iterable if not (x in seen or adder(x))]
