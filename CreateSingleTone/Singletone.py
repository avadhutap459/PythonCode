class MasterDataLoad:
    
    _instance = None
    _initilize = False
    
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
        return cls._instance
    
    def __init__(self):
        if self._initilize:
            return
        
        print("Initilze object")
        
        self._initilize = True

obj1 = MasterDataLoad()
obj2 = MasterDataLoad()
obj3 = MasterDataLoad()