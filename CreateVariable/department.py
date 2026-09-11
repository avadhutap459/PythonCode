class departmentSelf:
    def __init__(self,departName):
        self.departmentName = departName
    
    def displaydepartName(self):
        return "My department name is :" + self.departmentName
    

class departmentCls:
    
    departmentName = "Information Technology"
    
    @classmethod
    def displaydepartName(cls):
        return "My department name is :" + cls.departmentName