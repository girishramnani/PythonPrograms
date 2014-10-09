import random


class housie():
    def __init__(self):
        self.nlist=[x for x in range(1,91)]
    def random(self):
        self.left_list=list()
        random_no=random.choice(self.nlist)
        self.left_list.append(random_no)
        return random_no
    def show_left(self):
        for x in self.left_list:
            self.nlist.remove(x)
        return self.nlist
            


x=housie()

    
        
        
        
