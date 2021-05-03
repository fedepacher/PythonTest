from manage_element import ManageElement
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
            #exersice 1
            element_name_example1 = "Element2"       
            e1 = ManageElement()
            value1 = e1.find_element(element_name_example1)
            i = 0
            print('------------------------Excersice 1 ---------------------------------')
            for v in value1:
                print('Element ' + str(i) + ': ' + '[X=' + str(v.get_X()) + ', Y=' + str(v.get_Y()) + ', H=' + str(v.get_Height()) + ', W=' + str(v.get_Width()) + ']')
                i = i + 1
            print('')
            print('')


            #exercise 2
            elementA = Element()
            locator = 'locator'
            near_element = e1.find_element_near_to(elementA, locator)
            print('------------------------Excersice 2 ---------------------------------')
            
            if near_element == None:
                print('None element with ' + locator + ' was found')
            else:
                print('ElementA X= ' + str(elementA.get_X()) + ', Y= ' + str(elementA.get_Y()) + ' is near to element with X= ' + str(near_element.get_X()) + ', Y= ' + str(near_element.get_Y()))
            print('')
            print('')
        except ValueError:
            print("ERROR")
        return 1


"""
Entry point
"""
main = Main()
main.run()

