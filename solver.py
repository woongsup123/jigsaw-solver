import numpy
from PIL import Image
from piece import Piece
import helper

img = Image.open("pictures/sample_pic_2.jpg")

n = 0

while n != 1 and n != 2 :
    print("1. Generate pieces, then load pieces")
    print("2. Load pieces that are already generated (Recommended for quick look-through)")
    n = int(input("Enter option: "))
    print("\n")
if n == 1:
    helper.generate_pieces(img) # crops and shuffles the pieces randomly

pieces = helper.load_pieces()

piece_objects = []

for index in range(len(pieces)):

    width, height = pieces[index].size

    np_piece = numpy.array(pieces[index], dtype='int64')
    # define each piece as a Piece object2
    # Piece object consists of four edges
    edge1 = np_piece[0,:]
    edge2 = np_piece[:,height-1]
    edge3 = np_piece[width-1,:]
    edge4 = np_piece[:,0]
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(type(edge1))
    print(edge1)
    print(type(edge2))
    print(edge2)
    print(type(edge3))
    print(edge3)
    print(type(edge4))
    print(edge4)
    edges = [edge1, edge2, numpy.fliplr(edge3), edge4[::-1]]
    piece = Piece(edges)

    piece_objects.append(piece) # add each piece object into the array

all_sorted_distances = helper.get_all_sorted_distances(piece_objects)
solution = helper.solve(piece_objects, all_sorted_distances)

print("LIST OF ALL SORTED DISTANCES (Square #, Edge #, Square #, Edge #, Distance Value) : ")
print(all_sorted_distances)
print("\n")
print("Total number of edges compared: ")
print(len(all_sorted_distances))
print("\n")
print("Final Solution: ")
print(solution)
print("\n")
print("(S1, E1, S2, E2) Edge E1 of Square S1 is connected with Edge E2 of Square S2")
print("Edge(0, 1, 2, 3) => Edge(North, East, South, West)")
print("\n")
helper.combine(pieces, solution)

