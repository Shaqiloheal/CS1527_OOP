data_dict = {
    'data': [{'a': 'b'}, {'b', 'c'}, {'c', 'd'}],
    'texts': ['a', 'b', 'c']
}

for key, value in data_dict.iteritems():
    if key == 'data':
        for data_item in value:
            # Do you know what you are iterating now?
            for data_key, data_value in data_item.iteritems():
                print(data_key, data_value)
