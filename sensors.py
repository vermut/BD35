mapping = {
    8590175: ('A', None),
    13583386: ('B', None),
    13579673: ('C', 'D'),
    8589832: ('E', None),
    8584595: ('G', 'F'),
    13579798: ('H', 'I'),
    8589724: ('J', 'K'),
    8584654: ('M', 'L'),
    8589405: ('N', 'O'),
    8588919: ('Q', 'P'),
    8590509: ('R', 'S'),
    13642720: ('T', None),
}


def map_gate(content):
    if content['id'] in mapping:
        if content['distance'] > 0:
            return mapping[content['id']][0]
        elif content['distance2'] > 0:
            return mapping[content['id']][1]

    return None
