from element import Element
from aux_functions import load_json
import random
import math

class ManageElement:
    

    def __init__(self):
        pass

    """
    Finde element by it name
    param elemant_name :    element name to be found
    param locator :         locator 
    return object element 
    """
    def find_element(self, elemant_name, locator = 'locator'):
        try:
            read_list = load_json()
            ret_value = False
            finders = '__FINDERS__'
            locator_name = locator
            locator_value = None
            for value in read_list:
                if elemant_name in value:
                    locator_value = value[elemant_name][locator_name]                       #get locator value
                    ret_value = True
                    break
            if not ret_value:                                                               #search finders
                for value in read_list:     
                    if finders in value:                        
                        for val in value[finders]:
                            val[locator_name] = val[locator_name].replace("..._ELEMENT_NAME_...", elemant_name)     #replace locator by element name
                            locator_value = val[locator_name]                               #get locator value 
            if locator_value is None:
                return None
            new_list = self.get_element(locator_value)
        except ValueError:
            return None
        except Exception:
            return None
        return new_list
        
    """
    Get element by it locator
    param locator :     locator of an specific element
    return              object element list
    """
    def get_element(self, locator):
        element_list = list()
        amount_of_element = random.randint(1, 5)
        for i in range(0, amount_of_element):
            e = Element()
            element_list.append(e)
        return element_list 

    """
    Find element near to element
    param element :     element object
    param locator :     locator of an specific element
    return              nearest element 
    """
    def find_element_near_to(self, element, locator):

        element_list = self.find_element('element', locator)
        x, y = element.position()
        h, w = element.size() 
        
        if element_list is None:
            return None

        elem = self.near_element(x, y, element_list)        
        return elem

    """
    Get element near to element
    param x :               x coordinate
    param y :               y coordinate 
    param element_list :    element list to be compare
    return              nearest element 
    """
    def near_element(self, x, y, element_list):
        aux_elem = None

        for elem in element_list:
            e_x, e_y = elem.position()
            hip = math.sqrt(((x - e_x) ** 2 + (y - e_y) ** 2))
            if aux_elem is None:
                aux_elem = elem
                hip_aux = hip
            elif hip < hip_aux:
                hip_aux = hip
                aux_elem = elem

        return aux_elem