class Node:
    def __init__(self):
        self.rotate_sum = 0
        self.directions = [-1, -1, -1, -1]
        self.NE = False
        self.NW = False
        self.SE = False
        self.SW = False

    def print_node(self):
        print(self.directions)
        print(self.rotate_sum)
        print(self.NE)
        print(self.NW)
        print(self.SE)
        print(self.SW)

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

    def get_NE(self):
        return self.NE

    def get_NW(self):
        return self.NW

    def is_NE(self):
        if self.NE:
            return True
        else:
            return False

    def is_NW(self):
        if self.NW:
            return True
        else:
            return False

    def set_north(self, north):
        self.directions[0] = north

    def set_east(self,east):
        self.directions[1] = east

    def set_south(self,south):
        self.directions[2] = south

    def set_west(self,west):
        self.directions[3] = west

    def set_NE_True(self):
        self.NE = True

    def set_NW_True(self):
        self.NW = True

    def set_SE_True(self):
        self.SE = True

    def set_SW_True(self):
        self.SW = True

    def set_rotate_sum(self, num):
        self.rotate_sum = num

    def rotate_once(self):
        size = len(self.directions)
        temp = self.directions[size-1]
        for i in reversed(range(size-1)):
            self.directions[i] = self.directions[i-1]
        self.directions[0] = temp

    def set_connection(self, direction, piece):
        if direction == 0:
            self.set_north(piece)
        elif direction == 1:
            self.set_east(piece)
        elif direction == 2:
            self.set_south(piece)
        else:
            self.set_west(piece)
