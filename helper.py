import random
import math

import numpy

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
    new_pieces = []
    for piece in pieces:
        angle = random.choice([0, 90, 180, 270])
        piece = piece.rotate(angle)
        new_pieces.append(piece)

    random.shuffle(new_pieces)

    return new_pieces


def generate_pieces(img):
    pieces = crop(img) # crop and divide the image into 4 pieces
    return rotate_shuffle(pieces) # rotate the pieces and shuffle the order randomly


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
    distance = 0
    for i in range(len(np_pieces)): # for each edge of the chosen piece

        for j in range(len(np_pieces)): # compare it with edges of some other piece

            if n == j:
                continue

            for k in range(len(np_pieces)): # with the edge k of some other piece j
                if len(np_pieces[n].get_edge(i)) != len(np_pieces[j].get_edge(k)):
                    distance = 9999999999
                else:
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

def takeSecond(elem):
    return elem[1]

def solve(piece_objects, all_sorted_distances):
    solution = []
    pieces_used = []
    last_available_edges = []
    index = 0

    while len(solution) < 3 and index < len(all_sorted_distances):
        pair = all_sorted_distances[index]
        index += 1

        if len(solution) == 1 and pair[0] not in pieces_used and pair[2] not in pieces_used:
            long_piece1 = solution[0]

            long_piece1_edge1 = numpy.concatenate((piece_objects[long_piece1[2]].get_edge((long_piece1[3]+3)%4), piece_objects[long_piece1[0]].get_edge((long_piece1[1]+1)%4)))
            long_piece1_edge2 = numpy.concatenate((piece_objects[long_piece1[0]].get_edge((long_piece1[1]+3)%4), piece_objects[long_piece1[2]].get_edge((long_piece1[3]+1)%4)))
            long_piece2 = (pair[0], pair[1], pair[2], pair[3])
            long_piece2_edge1 = numpy.concatenate((piece_objects[long_piece2[2]].get_edge((long_piece2[3]+3)%4), piece_objects[long_piece2[0]].get_edge((long_piece2[1]+1)%4)))
            long_piece2_edge2 = numpy.concatenate((piece_objects[long_piece2[0]].get_edge((long_piece2[1]+3)%4), piece_objects[long_piece2[2]].get_edge((long_piece2[3]+1)%4)))

            sum_case1 = ((long_piece1[0], (long_piece1[1]+1)%4, long_piece2[2], (long_piece2[3]+3)%4), get_distance_between(long_piece1_edge1, long_piece2_edge1))
            sum_case2 = ((long_piece1[0], (long_piece1[1]+1)%4, long_piece2[0], (long_piece2[1]+3)%4), get_distance_between(long_piece1_edge1, long_piece2_edge2))
            sum_case3 = ((long_piece1[2], (long_piece1[3]+1)%4, long_piece2[2], (long_piece2[3]+3)%4), get_distance_between(long_piece1_edge2, long_piece2_edge1))
            sum_case4 = ((long_piece1[2], (long_piece1[3]+1)%4, long_piece2[0], (long_piece2[1]+3)%4), get_distance_between(long_piece1_edge2, long_piece2_edge2))

            sum_list = [sum_case1, sum_case2, sum_case3, sum_case4]
            sum_list.sort(key=takeSecond)
            return (long_piece1, long_piece2, sum_list[0][0])

        if len(solution) > 0 and ((pair[0], pair[1]) not in last_available_edges
                            and (pair[2], pair[3]) not in last_available_edges):
            continue

        if len(solution) > 0 and pair[0] in pieces_used and pair[2] in pieces_used:
            continue

        if len(solution) == 0:
            last_available_edges.append((pair[0],(pair[1]+1) % 4))
            last_available_edges.append((pair[2],(pair[3]+3) % 4))
            last_available_edges.append((pair[2],(pair[3]+1) % 4))
            last_available_edges.append((pair[0],(pair[1]+3) % 4))

        elif len(solution) == 1:
            trigger = False
            if (pair[0], pair[1]) == last_available_edges[0] or (pair[2], pair[3]) == last_available_edges[0]:
                if (pair[0], pair[1]) == last_available_edges[0]:
                    trigger = True
                last_available_edges[:] = [last_available_edges[1]]
            elif (pair[0], pair[1]) == last_available_edges[1] or (pair[2], pair[3]) == last_available_edges[1]:
                if (pair[0], pair[1]) == last_available_edges[1]:
                    trigger = True
                last_available_edges[:] = [last_available_edges[0]]
            elif (pair[0], pair[1]) == last_available_edges[2] or (pair[2], pair[3]) == last_available_edges[2]:
                if (pair[0], pair[1]) == last_available_edges[2]:
                    trigger = True
                last_available_edges[:] = [last_available_edges[3]]
            elif (pair[0], pair[1]) == last_available_edges[3] or (pair[2], pair[3]) == last_available_edges[3]:
                if (pair[0], pair[1]) == last_available_edges[3]:
                    trigger = True
                last_available_edges[:] = [last_available_edges[2]]

            if trigger:
                if piece_objects[pair[0]].is_connected((pair[1]+1) % 4):
                    last_available_edges.append((pair[2], (pair[3]+3) % 4))
                elif piece_objects[pair[0]].is_connected((pair[1]+3) % 4):
                    last_available_edges.append((pair[2], (pair[3]+1) % 4))
            else:
                if piece_objects[pair[2]].is_connected((pair[3]+1) % 4):
                    last_available_edges.append((pair[0], (pair[1]+3) % 4))
                elif piece_objects[pair[2]].is_connected((pair[3]+3) % 4):
                    last_available_edges.append((pair[0], (pair[1]+1) % 4))

        piece_objects[pair[0]].set_connected_true(pair[1])
        piece_objects[pair[2]].set_connected_true(pair[3])
        pieces_used.append(pair[0])
        pieces_used.append(pair[2])

        solution.append((pair[0], pair[1], pair[2], pair[3]))

    return solution


def merge_pieces(final_pieces):
    width, height = final_pieces[0].size
    final_image = Image.new('RGB', (width*2, height*2))
    final_image.paste(final_pieces[0],(width, 0))
    final_image.paste(final_pieces[1], (width, height))
    final_image.paste(final_pieces[2], (0, height))
    final_image.paste(final_pieces[3])
    return final_image



def locate_top_piece_at(piece, index):
        sum = 0
        pos = 0
        if index == 0:
            pos = 1
        elif index == 3:
            pos = 3
        # rotate piece until
        while not (piece.get_direction_at(0) == -1 and piece.get_direction_at(pos) == -1):
            piece.rotate_once()
            sum += 1
        piece.add_rotate_sum(sum)


def locateSouth(piece):
        sum = 0
        while piece.get_direction_at(0) == -1:
            piece.rotate_once()
            sum += 1
        piece.add_rotate_sum(sum)


def locateTop(piece, top_piece_indices):
    for i in range(len(piece.get_directions())):
        if piece.get_direction_at(i) in top_piece_indices:
            if piece.get_direction_at((i+3)%4) != -1:
                locate_top_piece_at(piece, 0)
                piece.set_location(0)
            elif piece.get_direction_at((i+1)%4) != -1:
                locate_top_piece_at(piece, 3)
                piece.set_location(3)
            break


def locateBottom(piece, bottom_piece_indices, top_piece_indices, piece1, piece2):
    for i in range(len(piece.get_directions())):
        if piece.get_direction_at(i) == top_piece_indices[0]:
            if piece1.is_NE():
                locateSouth(piece)
                piece.set_location(1) # 1 refers to SE
            else:
                locateSouth(piece)
                piece.set_location(2) # 2 refers to SW
        elif piece.get_direction_at(i) == top_piece_indices[1]:
            if piece2.is_NE():
                locateSouth(piece)
                piece.set_location(1) # 1 refers to SE
            else:
                locateSouth(piece)
                piece.set_location(2) # 2 refers to SW


def combine(pieces, solution):

    linked_list = list()

    for i in range(4):
        linked_list.append(Node(i))

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

    # finally, put the pieces together
    pieces_in_order = [None] * 4
    pieces_in_order[piece1.get_location_index()] = pieces[top_piece_indices[0]].rotate(270*piece1.get_rotate_sum())
    pieces_in_order[piece2.get_location_index()] = pieces[top_piece_indices[1]].rotate(270*piece2.get_rotate_sum())
    pieces_in_order[piece3.get_location_index()] = pieces[bottom_piece_indices[0]].rotate(270*piece3.get_rotate_sum())
    pieces_in_order[piece4.get_location_index()] = pieces[bottom_piece_indices[1]].rotate(270*piece4.get_rotate_sum())

    return merge_pieces(pieces_in_order)

    # merge_pieces function will be called in the end
