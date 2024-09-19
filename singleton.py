import threading

my_lock = threading.Lock()

class SingleTon:
    obj = None

    def __new__(cls):
        if cls.obj is None:
            with my_lock:
                if cls.obj is None:
                    cls.obj = super().__new__(cls)
                    return cls.obj
        
        return cls.obj
    

obj1 = SingleTon()
obj2 = SingleTon()

print(id(obj1) == id(obj2))

    
    
