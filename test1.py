
class shippingContainer:
    next_serial = 1453
    
    def __init__(self,owner_code,contents):
        self.ownercode=owner_code
        self.contents=contents
        self.serial = shippingContainer.next_serial
        shippingContainer.next_serial+=1
        
    

g = shippingContainer(454,453)
print(g.serial)
g2 = shippingContainer(454,453)
print(g2.serial)
        