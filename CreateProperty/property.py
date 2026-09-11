class publicProperty:
    def __init__(self,CName,CAddress,CMobileNo,Message):
        self.companyName = CName
        self.companyAddress = CAddress
        self.companyMobileNumber = CMobileNo
        self.message = Message


class protectedProperty:
    def __init__(self,message):
        self._message = message

class superClsprotectedProperty(protectedProperty) :
    def returnval(self):
        return self._message

class privateProperty:
    def __init__(self, message):
        self.__message = message
    
    def returnPrivatePro(self):
        return self.__message


class PropertyAttribute:
    def __init__(self,message):
        self.__message = message
    
    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self,value):
        if value is None or value == "":
            raise ValueError("This can not empty")
        self.__message = value
               