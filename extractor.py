import json

"""
Finde element by it name
param elemant_name :    element name to be found
return element object
"""
def find_element(elemant_name):
    file_list = openfile_retlist('startingFile.txt')
    values = find_element_ex(file_list[0], elemant_name)
    return values
    

"""
Finde element by it name
param filename :        json file with element info
param elemant_name :    element name to be found
return element object
"""
def find_element_ex(filename, elemant_name):
    element_array = []
    files_array = []  
    finder_array = []    
    data = load_json(filename)    
    get_value(data, element_array, files_array, finder_array, elemant_name)     
    if len(element_array) > 0:                                                      #if an element was found element_array > 0
        for k, v in element_array[0].items():                                       #get the first element 
            values = get_element(element_array[0])                          
    elif len(files_array) > 0:                                                      #if there is no element in the first file but there is an import files_array > 0
        for file in files_array:
            f_name = remove_parent(str(file)) + '.json'                             #get filename.json
            values = find_element_ex(f_name, elemant_name)                          #call recursively to explore others files in case import label is found
    elif len(finder_array) > 0:                                                     #if a __FINDERS__ label is found finder_array > 0
        for k, v in finder_array[0].items():            
            values = get_element(finder_array[0])                               
    else:
        values = None

    return values


"""
Search values recursively from nested JSON in case exist.
param obj_list :        JSON list
param element_array :   array of found elements
param file_array :      array of found json files
param finder_array :    array of found finders
param key :             value to be searched    
return                  array of found elementets, file and finder or empty arrays 
"""
def get_value(obj_list, element_array, file_array, finder_array, key):
    if isinstance(obj_list, dict):
        for k, v in obj_list.items():
            if k == 'import':                                                       #checks if import label is as key
                file_array.append(v)                                                #store value
            elif k == '__FINDERS__':                                                #checks if __FINDERS__ label is as key
                get_value(v, element_array, file_array, finder_array, key)          #checks inside __FINDERS__ element
            elif  k == key:                                                         #checks if an element is found            
                element_array.append(v)                                             #store the element
            elif isinstance(v, (dict)):                                             #checks is value is a dict in case of nested json 
                get_value(v, element_array, file_array, finder_array, key)          #checks inside value for element
    elif isinstance(obj_list, list):                                                #__FINDERS__ is a list element so explore inside finders
        for item in obj_list:                                                       #checks all items of finders
            for k, v in item.items():                                               #replace value by the element name
                item[k] = key
            finder_array.append(item)                                               #store the new locator 
    return element_array, file_array, finder_array
    

"""
Get element by it locator
param locator :     locator of an specific element
return              object element containing it locator
"""
def get_element(locator):
    
    return locator #{"ElementX": {"locator": "_ELEMENT_NAME_X"}}


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