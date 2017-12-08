class Node:
    def __init__(self):
        self.north = -1
        self.east = -1
        self.south = -1
        self.west = -1
        self.angle = 0

    def print_node(self):
        print("angle: " + str(self.angle))
        print("north: " + str(self.north))
        print("east: " + str(self.east))
        print("south: " + str(self.south))
        print("west: " + str(self.west))

    def get_north(self):
        return self.north

    def get_east(self):
        return self.east

    def get_south(self):
        return self.south

    def get_west(self):
        return self.west

    def get_angle(self):
        return self.angle

    def get_num_of_connected_edges(self):
        sum = 0
        if self.get_north() != -1:
            sum += 1

    def set_north(self,north):
        self.north = north

    def set_east(self,east):
        self.east = east

    def set_south(self,south):
        self.south = south

    def set_west(self,west):
        self.west = west

    def set_angle(self, angle):
        self.angle = angle

    def add_angle(self, angle):
        self.angle += angle

    def set_connection(self, direction, piece):
        if direction == 0:
            self.set_north(piece)
        elif direction == 1:
            self.set_east(piece)
        elif direction == 2:
            self.set_south(piece)
        else:
            self.set_west(piece)
