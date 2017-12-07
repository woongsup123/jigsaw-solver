class Piece(object):

    def __init__(self, edges):
        self.edges = edges

    def get_edge(self, index): #index range from 0 to 3
        if len(self.edges) >= index + 1:
            return self.edges[index]
        else:
            print("[Error] index out of range")