class cat :
    def __init__(self,name="",hieght=0,weight=0):
            self.name = name
            self.hieght = hieght
            self.weight = weight

    def run(self): 
        print("{}the cat runs".format(self.name))

    

    def mew(self):
        print("{}the cat mews".format(self.name)) 

def main(): 

    pussy=cat("pussy", 10, 13)

    pussy=run()

    pussy=mew()

main()