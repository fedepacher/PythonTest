from extractor import find_element
from element import Element

class Main:
    

    def __init__(self):
        pass
   

    """
    Run function, execute program
    return 1      
    """
    def run(self):
        try:
            element_name_example = "Element5"
            #value = find_element(element)
            e = Element()
            value = e.find_element(element_name_example)
            print(e.get_element_name() + " : " + str(value))
        except ValueError:
            print("ERROR")
        return 1


       
    

"""
Entry point
"""
main = Main()
main.run()

