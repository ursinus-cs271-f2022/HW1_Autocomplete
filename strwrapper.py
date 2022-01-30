class StrWrapper:
    def __init__(self, s):
        self.s = s
    
    def hash_code(self):
        return 0 ## TODO: Fill this in

    def __eq__(self, other):
        return self.s == other.s

    def __str__(self):
        return self.s
    
if __name__ == '__main__':
    for s in ["hello", "cs 371", "computers rock"]:
        swrap = StrWrapper(s)
        print(swrap, swrap.hash_code())
