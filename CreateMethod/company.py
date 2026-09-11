class Company:
    @classmethod
    def display_company_name_cls(cls):
        return "This is class method"
    
    @staticmethod
    def display_company_name_static():
        return "This is static method"
    
    def display_company_name_self(self):
        return "This is instance method"