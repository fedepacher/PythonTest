from aux_functions import openfile_retlist
from aux_functions import load_json
from aux_functions import remove_parent

class Element:
    
    def __init__(self, name = None, locator = None):
        self.set_element_name(name)
        self.set_locator(locator)


    def set_element_name(self, name):
        self._element_name = name

    def set_locator(self, locator):
        self._locator = locator

    def get_element_name(self):
        return self._element_name

    def get_locator(self):
        return self._locator



    def position(self):


        return x, y

    def size(self):


        return height, width


    def find_element_near_to(self, elemant_name, locator):
        self.set_element_name(elemant_name) 
        self.set_locator(locator)
        return

    """
    Finde element by it name
    param elemant_name :    element name to be found
    return element object
    """
    def find_element(self, elemant_name):
        self.set_element_name(elemant_name)
        file_list = openfile_retlist('startingFile.txt')
        values = self.find_element_ex(file_list[0])
        return values
        

    """
    Finde element by it name
    param filename :        json file with element info
    return element object
    """
    def find_element_ex(self, filename):
        element_array = []
        files_array = []  
        finder_array = []    
        data = load_json(filename)    
        self.get_value_element(data, element_array, files_array, finder_array, self.get_element_name())     
        if len(element_array) > 0:                                                      #if an element was found element_array > 0
            for k, v in element_array[0].items():                                       #get the first element 
                values = self.get_element(element_array[0])                          
        elif len(files_array) > 0:                                                      #if there is no element in the first file but there is an import files_array > 0
            for file in files_array:
                f_name = remove_parent(str(file)) + '.json'                             #get filename.json
                values = self.find_element_ex(f_name)                                   #call recursively to explore others files in case import label is found
        elif len(finder_array) > 0:                                                     #if a __FINDERS__ label is found finder_array > 0
            for k, v in finder_array[0].items():            
                values = self.get_element(finder_array[0])                               
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
    def get_value_element(self, obj_list, element_array, file_array, finder_array, key):
        if isinstance(obj_list, dict):
            for k, v in obj_list.items():
                if k == 'import':                                                       #checks if import label is as key
                    file_array.append(v)                                                #store value
                elif k == '__FINDERS__':                                                #checks if __FINDERS__ label is as key
                    self.get_value_element(v, element_array, file_array, finder_array, key)          #checks inside __FINDERS__ element
                elif  k == key:                                                         #checks if an element is found            
                    element_array.append(v)                                             #store the element
                elif isinstance(v, (dict)):                                             #checks is value is a dict in case of nested json 
                    self.get_value_element(v, element_array, file_array, finder_array, key)          #checks inside value for element
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
    def get_element(self, locator):
        
        return locator #{"ElementX": {"locator": "_ELEMENT_NAME_X"}}