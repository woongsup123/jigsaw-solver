import numpy
from PIL import Image
from piece import Piece
import helper




#picture = [Piece([3, 8, 9, 10]), Piece([2, 5, 6, 7]), Piece([3, 4, 1, 2]), Piece([8, 7, 11, 12])]
# print (picture[2].get_edge(3))
#def solve(picture):


img = Image.open("pictures/sample_pic.jpg")


pieces = helper.crop(img) # crop and divide the image into 4 pieces
helper.rotate_shuffle(pieces) # rotate the pieces and shuffle the order randomly
np_pieces = []


for index in range(len(pieces)):
    pieces[index].save("pieces/pic_"+str(index)+".jpg") # save each piece as an image file

    width, height = pieces[index].size

    np = numpy.array(pieces[index], dtype='int64')
    np_piece = Piece([np[0,:], np[:,width-1], np[height-1,:], np[:,0]]) # define each piece as a Piece object
    np_pieces.append(np_piece) # add each piece object into the array

for i in range(len(np_pieces)):
    print("for square number " + str(i))
    optimal_pairs = helper.get_optimal_pairs(i, np_pieces)
    print(optimal_pairs)
    print('\n')


'''

image1 = Image.open("pieces/pic_1.jpg")
np_image1 = numpy.array(image1, dtype='int64')
edge1 = np_image1[:,467]

image2 = Image.open("pieces/pic_3.jpg")
np_image2 = numpy.array(image2, dtype='int64')
edge2 = np_image2[0,:]


distance = helper.get_distance_between(edge1, edge2)

print(distance)
'''


#pix = img.load()
#np = numpy.array(img)
#edge1 = np[0,:]
#edge2 = np[:,0]
#print(edge1)
#print(edge2)
#print(np[0,:])
#print(np[:,0])
#print(np[4:10,0])
#print(np[0,0,0])
