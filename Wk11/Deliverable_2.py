class Bus:
    # Constructor to define bus capacity when assigning object to variable
    def __init__(self, passanger_cap):
        self.passenger_limit = passanger_cap
        self.passenger_seats = [] 

    # Function to pick up people and notifying if bus is full
    def person_pickup(self, person):
        if len(self.passenger_seats) >= self.passenger_limit:
            print(f'Bus is full cant pick up {person}')
            return
        
        self.passenger_seats.append(person)
        print(f'Se ha montado {person}')

    # Function to drop people off 
    def person_dropoff(self, person):
        if person in self.passenger_seats:
            self.passenger_seats.remove(person)
            print(f'{person} dropping from the bus')
        
        else:
            print(f'{person} isn\'t on the bus')
            return

class Person():
    # Constructor to name people differently
    def __init__(self, name):
        self.person_name = name
    
    def __str__(self):
        return self.person_name

bus = Bus(3)

person_1 = Person('Larry')
person_2 = Person('Jimmy')
person_3 = Person('Cesar')
person_4 = Person('Don Evelio')

bus.person_pickup(person_1)
bus.person_pickup(person_2)
bus.person_pickup(person_3)
bus.person_pickup(person_4)

bus.person_dropoff(person_1)
bus.person_dropoff(person_4)
print([str(person) for person in bus.passenger_seats])



