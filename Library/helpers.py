import collections


def to_dict(layer):
    to_ret = layer
    if isinstance(layer, collections.OrderedDict):
        to_ret = dict(layer)

    if isinstance(layer, list):
        to_ret = [dict(i) for i in layer]

    try:
        for key, value in to_ret.items():
            to_ret[key] = to_dict(value)
    except AttributeError:
        pass

    return to_ret
