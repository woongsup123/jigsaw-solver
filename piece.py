class Piece(object):

    def __init__(self, edges):
        self.edges = edges
        self.connected = [False, False, False, False]

    def get_edge(self, index): #index range from 0 to 3
        if len(self.edges) >= index + 1:
            return self.edges[index]
        else:
            print("[Error] index out of range")

    def is_connected(self, index):
        return self.connected[index]

    def set_connected_true(self, index):
        self.connected[index] = True