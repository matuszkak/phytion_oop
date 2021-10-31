class Spaceship:

    # constructior
    def __init__(self, fuel, passengers, shields, speedometer):
        self.fuel = fuel
        self.passengers = passengers
        self.shields = shields
        self.speedometer = speedometer
        print('Spaceship created!')

    def list_passengers(self):
        for i in range(0, len(self.passengers)):
            print(f'Passenger: {self.passengers[i]}')
        return

    def add_passenger(self, new_passenger):
        self.passengers.append(new_passenger)
        print(f'{new_passenger} added to the ship')
        return

    def travel(self, distance):
        print(f'Trying to travel: {distance}')
        newDistance = 0

        # ha nincs már üzemenyag...
        if (self.fuel == 0):
            print(f'Cannot go further, tank is empty')

        # ha még van üzemanyag...
        else:
            self.fuel = self.fuel - (distance / 2)

            # ha negatívba ment akkor nem tudja a teljes távot megtenni
            if (self.fuel < 0):
                # megtehető távolság számítása és tank ürítése
                newDistance = distance + 2 * self.fuel
                print(f'Can only travel: {int(newDistance)}')
                self.fuel = 0
                # ha nem ment negatívba akkor a teljes távot meg tudja tenni + benga is marad még
            else:
                newDistance = int(distance)

            # kilométeróra átállítása + pajzs inaktiválás maradék üzemanyag függvényében
            self.speedometer = self.speedometer + newDistance

            if (self.fuel < 30 and self.shields):
                self.shields = False
                print(f'Fuel is low, turning off shields...')

            # megtett távolság és megmaradó üzemanyag a képernyőre
            print(f'Spaceship is at: {int(self.speedometer)}')
            print(f'Spaceship has: {int(self.fuel)} fuel')


mySpaceship = Spaceship(400, ["John", "Steve", "Sam", "Danielle"], True, 0)

mySpaceship.list_passengers()
mySpaceship.add_passenger('Lindsay')
mySpaceship.list_passengers()
mySpaceship.travel(750)
mySpaceship.travel(200)
mySpaceship.travel(100)
