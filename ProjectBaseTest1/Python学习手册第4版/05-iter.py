
class Stepper:
    """

    """
    def __getitem__(self, i):
        return self.data[i]

x=Stepper()
x.data='spam'
print(x[1])
for item in x:
    print(item,end=' ')

print('p' in x)
print([item for item in x])
print(list(map(str.upper,x)))
print(list(x),tuple(x),''.join(x))

class Squeres():
    def __init__(self,start,stop):
        self.value = start-1
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
    
for i in Squeres(1,5):
    print(i,end=' ')

x = Squeres(1,5)
it = iter(x)
print(next(it))
print(next(it))
print(next(it))


class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

s1 = 'abcedf'
skipper = SkipObject(s1) 
it = iter(skipper)
print(next(it),next(it),next(it))
for x in skipper:
    for y in skipper:
        print(x+y,end=' ')
print()
for x in s1[::2]:
    for y in s1[::2]:
        print(x+y,end=' ')


