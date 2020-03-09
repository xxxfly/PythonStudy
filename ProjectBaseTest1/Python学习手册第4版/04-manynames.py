x=11  # Global (module) name/attribute (x,or manyname.x)

def f():
    print(x)  # Access global x

def g():
    x=22  # Local (function) variable (x,hide module x) 
    print(x)  

class C:
    x=33  # Class attribute (C.x)
    def m(self): 
        x=44  # Local variable in method(x)
        self.x=55  # Instance attribute (instance.x)
    
if __name__ == '__main__':
    print(x)
    f()
    g()
    print(x)
    print(C.x)
    obj = C()
    print(obj.x)
    obj.m()
    print(obj.x)
    print(C.x)
