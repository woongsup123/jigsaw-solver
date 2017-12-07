import numpy
from PIL import Image
from piece import Piece
import helper

img = Image.open("pictures/sample_pic.jpg")

#helper.generate_pieces(img) # crops and shuffles the pieces randomly
pieces = helper.load_pieces()
piece_objects = []
for index in range(len(pieces)):

    width, height = pieces[index].size

    np_piece = numpy.array(pieces[index], dtype='int64')
    # define each piece as a Piece object
    # Piece object consists of four edges
    piece = Piece([np_piece[0,:], np_piece[:,width-1], np_piece[height-1,:], np_piece[:,0]])
    piece_objects.append(piece) # add each piece object into the array

for i in range(len(piece_objects)):
    print("for square number " + str(i))
    optimal_pairs = helper.get_optimal_pairs(i, piece_objects)
    for j in range(len(optimal_pairs)):
        print(optimal_pairs[j])
    print('\n')
