class ClsDefaultConstructor :
    def __init__(self):
        self.message = "Default Constructor"

class ClsParameterConstructor :
    def __init__(self, message ):
        self._message = message
        

class ClsCopyConstructor :
    def __init__(self,message):
        self._message = message
    
    def __copy__(self):
        return ClsCopyConstructor(self._message)
    

class ClsOverloadingConstructor :
    def __init__(self , message = None):
        if message is None :
            self._message = "Default Constructor Overloading"
        else :
            self._message = message
            

class ClsDestructor :
    def __init__(self, message):
        self._message = message
    
    def __del__(self):
        print(f"Destructore called : {self._message}")