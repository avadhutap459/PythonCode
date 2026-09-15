class CacheResposible :
    _Instance = None
    _Initialize = False
    
    def __new__(cls):
        if cls._Instance is not None:
            cls._Instance = super().__new__(cls)
        
        return cls._Instance
    
    def __init__(self):
        if self._Initialize:
            return
        
        print("Initialize Object")
        
        self._Initialize = True
        
obj1 = CacheResposible()
obj2 = CacheResposible()
obj3 = CacheResposible()