mapping = {
    8590175: ('A', None),
    8590509: ('B', None),
    13583386: ('C', None),
    8589832: ('C', 'D'),
    13642720: ('D', None)
}


def map_gate(content):
    if content['id'] in mapping:
        if content['distance'] > 0:
            return mapping[content['id']][0]
        elif content['distance2'] > 0:
            return mapping[content['id']][1]

    return None
