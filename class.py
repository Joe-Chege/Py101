class Vehicles:
    def kenyan_vehicles(self):

        print("This are the types of vehicles on the kenyan Roads")
class Saloon(Vehicles):
    def __init__(self, station, wagon, hatchback):

        self.station=station
        self.wagon=wagon
        self.hatchback=hatchback

    def saloon_types(self):

        print("The type of sallon car include,", self.station, self.wagon, self.hatchback )


class Heavy_Cars(Vehicles):
    def __init__(self, transist, truck, trailer, bus):

        self.transist=transist
        self.truck=truck
        self.bus=bus

    def heavy_vehicles(self):

        print("The following are the major types of heavy commercial vehicles", 
        self.bus, self.transist,
         self.truck, "This are just but an example.")

heavy1=Heavy_Cars("Actros", "FH", "Man", "Scania")


print(heavy1.truck)
print(heavy1.bus)



car1=Saloon("Filder", "GT4", "vitz")
car2=Saloon("macX", "Crown", "AltoS")

car1.saloon_types()
car2.saloon_types()

heavy1.heavy_vehicles()

car1.kenyan_vehicles()