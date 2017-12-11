import numpy
from PIL import Image
from piece import Piece
import helper

filenames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for file in filenames:
    img = Image.open("pictures/"+file+".jpg")

    helper.generate_pieces(img, file) # crops and shuffles the pieces randomly

    pieces = helper.load_pieces(file)

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
        edges = [edge1, edge2, edge3[::-1], edge4[::-1]]
        piece = Piece(edges)

        piece_objects.append(piece) # add each piece object into the array

    all_sorted_distances = helper.get_all_sorted_distances(piece_objects)
    solution = helper.solve(piece_objects, all_sorted_distances)
    helper.combine(pieces, solution, file)

