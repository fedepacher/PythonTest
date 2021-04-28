from extractor import find_element

class Main:
    

    def __init__(self):
        pass
   

    """
    Run function, execute program
    return 1      
    """
    def run(self):
        try:
            element = "Element5"
            value = find_element(element)
            print(element + " : " + str(value))
        except ValueError:
            print("ERROR")
        return 1


       
    

"""
Entry point
"""
main = Main()
main.run()

