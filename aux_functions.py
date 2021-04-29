import json

"""
Load json file in dictionary variable
param filename :    filename with json information
return              json data in a dictionary variable
"""
def load_json(filename):        
    read_lines = openfile(filename)                                                 #read file to extract json
    data = None
    for line in read_lines:
        try:    
            data = json.loads(line)                                                 #json data as a dict
        except ValueError:  
            print('Decoding JSON has failed')       
        except json.decoder.JSONDecodeError:
            print("String could not be converted to JSON")
            
    return data

"""
Remove '[' and ']'
param properties :    str of properties with [ ]   
return prop_aux :     property without "[xx]"
"""
def remove_parent(property):
    prop_aux = property.replace('[', '')                        
    prop_aux = prop_aux.replace(']', '')
    prop_aux = prop_aux.replace('\'', '')
    return prop_aux
    

"""
Open file
param filename :    file name 
return              return dictionary of read lines
"""
def openfile(filename):
    try:
        with open(filename, 'r') as txt_file:                                       #get all information
            lines = txt_file.readlines()
    except:
        print("No " + filename + " was found")
        exit(1)

    return lines

"""
Open file
param filename :    file name 
return              return list of read lines
"""
def openfile_retlist(filename):
    lines = openfile(filename)
    listToStr = ' '.join([str(elem) for elem in lines])                             #convert list to str
    file_list = listToStr.split(',')
    return file_list