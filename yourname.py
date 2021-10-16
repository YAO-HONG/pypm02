from random import sample

class Yourname:

    # digits: digit number of a game
    def __init__(self, digits=4):
        self.digits = digits
        self.renew()
    
    # guess next 4 digits in list, ex: [1, 2, 3, 4]
    # last means the last guessing result in tuple, ex: (1, 2) means 1A 2B
    # last would be None whne guess be called first time of a game
    def guess(self, last=None):
        return sample(range(10), k=self.digits)
    
    # would be called for a new game, you may do necessary setting here 
    def renew(self):
        pass
