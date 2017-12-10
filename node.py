class Node:
    def __init__(self, node_number):
        self.rotate_sum = 0
        self.directions = [-1, -1, -1, -1]
        self.location = [False, False, False, False] # NE, SE, SW, NW
        self.node_number = node_number

    def print_node(self):
        print(self.directions)
        print(self.rotate_sum)
        print(self.location)

    def get_direction_at(self, num):
        return self.directions[num]

    def get_rotate_sum(self):
        return self.rotate_sum

    def get_directions(self):
        return self.directions

    def get_num_of_connected_edges(self):
        sum = 0
        for direction in self.directions:
            if direction != -1:
                sum += 1
        return sum

    def get_location_index(self):
        i = 0
        while not self.location[i]:
            i += 1
        return i

    def get_node_number(self):
        return self.node_number


    def is_NE(self):
        return self.location[0]

    def is_NW(self):
        return self.location[3]


    def set_north(self, north):
        self.directions[0] = north

    def set_east(self,east):
        self.directions[1] = east

    def set_south(self,south):
        self.directions[2] = south

    def set_west(self,west):
        self.directions[3] = west

    def set_location(self, index):
        self.location[index] = True

    def add_rotate_sum(self, num):
        self.rotate_sum += num

    def rotate_once(self):
        self.directions = self.directions[-1:] + self.directions[:-1]

    def set_connection(self, direction, piece):
        if direction == 0:
            self.set_north(piece)
        elif direction == 1:
            self.set_east(piece)
        elif direction == 2:
            self.set_south(piece)
        else:
            self.set_west(piece)
