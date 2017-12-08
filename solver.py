import numpy
from PIL import Image
from piece import Piece
import helper

img = Image.open("pictures/sample_pic.jpg")

n = 0

while n != 1 and n != 2 :
    print("1. Generate pieces, then load pieces")
    print("2. Load pieces that are already generated")
    n = int(input())

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

    edges = [edge1, edge2, numpy.fliplr(edge3), edge4[::-1]]
    piece = Piece(edges)

    piece_objects.append(piece) # add each piece object into the array

all_sorted_distances = helper.get_all_sorted_distances(piece_objects)
solution = helper.solve(piece_objects, all_sorted_distances)

print(all_sorted_distances)
print(len(all_sorted_distances))
print(solution)

helper.combine(pieces, solution)