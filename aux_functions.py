import json

"""
Open file
param filename :    file name 
return              return list of read data
"""
def load_json():
    FILENAME = 'File1.json'
    read_list = list()
    flag_read = True
    while(flag_read):
        with open(FILENAME) as json_file:
            data = (json.load(json_file))           #dict
        read_list.append(data)
        if 'import' in data:
            FILENAME = data['import'][0] + '.json'
        else:
            flag_read = False

    return read_list


