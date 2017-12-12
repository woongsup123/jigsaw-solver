import numpy
from PIL import Image
from piece import Piece
import helper

filenames = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(len(filenames)):
    img = Image.open("pictures/"+filenames[i]+".jpg")

    generated_pieces = helper.generate_pieces(img) # crops and shuffles the pieces randomly

    for index in range(len(generated_pieces)):
        generated_pieces[index].save("pieces/"+filenames[i]+"/piece_"+str(index)+".jpg") # save each piece as an image file

    pieces = []
    for index in range(len(generated_pieces)):
        pieces.append(Image.open("pieces/"+filenames[i]+"/piece_"+str(index)+".jpg"))

    piece_objects = []

    for index in range(len(pieces)):

        width, height = pieces[index].size

        np_piece = numpy.array(pieces[index], dtype='int64')
        # define each piece as a Piece object2
        # Piece object consists of four edges
        edge1 = np_piece[0,:]
        edge2 = np_piece[:,width-1]
        edge3 = np_piece[height-1,:]
        edge4 = np_piece[:,0]
        edges = [edge1, edge2, edge3[::-1], edge4[::-1]]
        piece = Piece(edges)

        piece_objects.append(piece) # add each piece object into the array

    all_sorted_distances = helper.get_all_sorted_distances(piece_objects)
    solution = helper.solve(piece_objects, all_sorted_distances)
    final_image = helper.combine(pieces, solution, filenames[i])
    final_image.save("results/final_img_"+filenames[i]+".jpg")
    print(filenames[i] + " Complete")
