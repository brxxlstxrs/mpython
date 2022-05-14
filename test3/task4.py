class DwarvesCastle:
    def __init__(self, area, gnome_capacity, location):
        self.area = area
        self.gnome_capacity = gnome_capacity
        self.location = location

    def __lt__(self, other):
        if self.gnome_capacity < other.gnome_capacity:
            return True
        elif self.area < other.area:
            return True
        elif self.location.lower() > other.location.lower():
            return True
        
        return False

    def __le__(self, other):
        if self.gnome_capacity <= other.gnome_capacity:
            return True
        elif self.area <= other.area:
            return True
        elif self.location.lower() >= other.location.lower():
            return True
        
        return False

    def __eq__(self, other):
        if (self.gnome_capacity == other.gnome_capacity and
                self.area == other.area and
                self.location.lower() == other.location.lower()):
            return True
        
        return False

    def __ne__(self, other):
        if self.gnome_capacity != other.gnome_capacity:
            return True
        elif self.area != other.area:
            return True
        elif self.location.lower() != other.location.lower():
            return True
        
        return False

    def __gt__(self, other):
        if self.gnome_capacity > other.gnome_capacity:
            return True
        elif self.area > other.area:
            return True
        elif self.location < other.location:
            return True
        
        return False

    def __ge__(self, other):
        if self.gnome_capacity >= other.gnome_capacity:
            return True
        elif self.area >= other.area:
            return True
        elif self.location <= other.location:
            return True
        
        return False

    def __mul__(self, other):
        area = max(self.area, other.area)
        gnome_capacity = int((self.gnome_capacity + other.gnome_capacity) / 2)
        location = min(self.location, other.location)
        return DwarvesCastle(area, gnome_capacity, location)

    def __isub__(self, number):
        self.area -= number // 2
        self.gnome_capacity -= number
        if self.gnome_capacity < 1:
            self.gnome_capacity = 1

    def __truediv__(self, number):
        lst = []
        area = self.area // number
        self.area = self.area % number
        for i in range(number):
            lst.append(DwarvesCastle(area, 1, self.location))
        return lst

    def __call__(self):
        return self.area * len(self.location) // self.gnome_capacity

    def expand(self, number):
        self.area += number

    def __str__(self):
        return (f'Dwarf Castle location {self.location} accommodates '
                f'{self.gnome_capacity} dwarves in an area of {self.area}.')

    def __repr__(self):
        return f'DwarvesCastle({self.area}, {self.gnome_capacity}, \'{self.location}\')'


