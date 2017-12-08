import random
import math
from node import Node
from operator import itemgetter
from PIL import Image


def crop(img):
    width, height = img.size

    img1 = img.crop((0, 0, width/2, height/2))
    img2 = img.crop((width/2, 0, width, height/2))
    img3 = img.crop((0, height/2, width/2, height))
    img4 = img.crop((width/2, height/2, width, height))

    return [img1, img2, img3, img4]


def rotate_shuffle(pieces):
    #rotate randomly
    for index in range(len(pieces)):
        angle = random.choice([0, 90, 180, 270])
        pieces[index] = pieces[index].rotate(angle)
        random.shuffle(pieces)


def generate_pieces(img):
    pieces = crop(img) # crop and divide the image into 4 pieces
    rotate_shuffle(pieces) # rotate the pieces and shuffle the order randomly

    for index in range(len(pieces)):
        pieces[index].save("pieces/piece_"+str(index)+".jpg") # save each piece as an image file


def load_pieces():
    pieces = []
    for index in range(0, 4):
        pieces.append(Image.open("pieces/piece_"+str(index)+".jpg"))
    return pieces


def get_distance_between (edge1, edge2):

    if len(edge1) != len(edge2):
        print("[Error] lengths of the edges are not equal")
    distance = 0

    length = len(edge1)
    for index in range(length):
        distance += math.sqrt( (edge1[index][0] - edge2[length-index-1][0]) ** 2 +
                               (edge1[index][1] - edge2[length-index-1][1]) ** 2 +
                               (edge1[index][2] - edge2[length-index-1][2]) ** 2 )

    return round(distance,2)


def get_distances(n, np_pieces): # for the chosen piece
    collection_of_distances = []
    for i in range(len(np_pieces)): # for each edge of the chosen piece

        for j in range(len(np_pieces)): # compare it with edges of some other piece

            if n == j:
                continue

            for k in range(len(np_pieces)): # with the edge k of some other piece j
                distance = get_distance_between(np_pieces[n].get_edge(i), np_pieces[j].get_edge(k))
                collection_of_distances.append((n, i, j, k, distance)) # piece j, edge k, distance value

    return collection_of_distances


def get_all_sorted_distances(np_pieces):

    distances_all = []
    for i in range(len(np_pieces)):
        distances = get_distances(i, np_pieces) # for piece i
        # distances_all.append(distances)
        for distance in distances:
            if (distance[2], distance[3], distance[0], distance[1], distance[4]) not in distances_all:
                distances_all.append(distance)

    distances_all = sorted(distances_all, key=itemgetter(4))

    return distances_all


def solve(piece_objects, all_sorted_distances):
    solution = []
    pieces_used = []
    index = 0
    found_first_two = False
    while len(solution) < 3 and index < len(all_sorted_distances):
        pair = all_sorted_distances[index]
        index += 1

        piece1 = piece_objects[pair[0]]
        piece2 = piece_objects[pair[2]]
        if piece1.is_connected(pair[1]) or piece1.is_connected((pair[1]+4)%4) or piece2.is_connected(pair[3]) or piece2.is_connected((pair[3]+4)%4):
            continue

        if not found_first_two or (pair[0] in pieces_used) is (pair[2] not in pieces_used):
            piece_objects[pair[0]].set_connected_true(pair[1])
            piece_objects[pair[2]].set_connected_true(pair[3])
            pieces_used.append(pair[0])
            pieces_used.append(pair[2])
            solution.append((pair[0], pair[1], pair[2], pair[3]))
            found_first_two = True
    return solution


def merge_pieces(final_pieces):
    width, height = final_pieces[0].size
    final_image = Image.new('RGB', (width*2, height*2))
    final_image.paste(final_pieces[0],(0, 0))
    final_image.paste(final_pieces[1], (width, 0))
    final_image.paste(final_pieces[2], (0, height))
    final_image.paste(final_pieces[3], (width, height))
    final_image.save("results/final_img.jpg")


def locateNE(piece):
        sum = 0
        while piece.get_direction_at(0) != -1 and piece.get_direction_at(1) != -1:
            piece.rotate_once()
            sum += 1
        piece.set_rotate_sum(sum)

def locateNW(piece):
        sum = 0
        while piece.get_direction_at(1) != -1 and piece.get_direction_at(2) != -1:
            piece.rotate_once()
            sum += 1
        piece.set_rotate_sum(sum)

def locateSouth(piece):
        sum = 0
        while piece.get_direction_at(0) != -1:
            piece.rotate_once()
            sum += 1
        piece.set_rotate_sum(sum)


def locateTop(piece, top_piece_indices):
    for i in range(len(piece.get_directions())):
        if piece.get_direction_at(i) == top_piece_indices[1]:
            if piece.get_direction_at((i+3)%4) != -1:
                locateNE(piece)
                piece.set_NE_True()
            else:
                locateNW(piece)
                piece.set_NW_True()
            break
        elif piece.get_direction_at(i) == top_piece_indices[0]:
            if piece.get_direction_at((i+3)%4) != -1:
                locateNE(piece)
                piece.set_NE_True()
            else:
                locateNW(piece)
                piece.set_NW_True()
            break

def locateBottom(piece, bottom_piece_indices, top_piece_indices, piece1, piece2):
    for i in range(len(piece.get_directions())):
        if piece.get_direction_at(i) == top_piece_indices[0]:
            if piece1.is_NE():
                locateSouth(piece)
                piece.set_SE_True()
            else:
                locateSouth(piece)
                piece.set_SW_True()
        elif piece.get_direction_at(i) == top_piece_indices[1]:
            if piece2.is_NE():
                locateSouth(piece)
                piece.set_SE_True()
            else:
                locateSouth(piece)
                piece.set_SW_True()

def combine(pieces, solution):

    linked_list = list()

    for i in range(4):
        linked_list.append(Node())

    for pair in solution:
        linked_list[pair[0]].set_connection(pair[1], pair[2])
        linked_list[pair[2]].set_connection(pair[3], pair[0])

    top_piece_indices = []
    bottom_piece_indices = []

    for i in range(4):
        if linked_list[i].get_num_of_connected_edges() == 2:
            top_piece_indices.append(i)
        else:
            bottom_piece_indices.append(i)

    piece1 = linked_list[top_piece_indices[0]]
    piece2 = linked_list[top_piece_indices[1]]

    locateTop(piece1, top_piece_indices)
    locateTop(piece2, top_piece_indices)

    piece3 = linked_list[bottom_piece_indices[0]]
    piece4 = linked_list[bottom_piece_indices[1]]

    locateBottom(piece3, bottom_piece_indices, top_piece_indices, piece1, piece2)
    locateBottom(piece4, bottom_piece_indices, top_piece_indices, piece1, piece2)

    print("============================================================")
    print("Linked List Nodes to be implemented")
    print("============================================================")
    piece1.print_node()
    piece2.print_node()
    piece3.print_node()
    piece4.print_node()

    # merge_pieces function will be called in the end
