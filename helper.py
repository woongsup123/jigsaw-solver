import random
import math
from operator import itemgetter

def crop(img):
    width, height = img.size

    img1 = img.crop((0, 0, width/2, height/2))
    img2 = img.crop((width/2, 0, width, height/2))
    img3 = img.crop((0, height/2, width/2, height))
    img4 = img.crop((width/2, height/2, width, height))

    return [img1, img2, img3, img4]

    #img1.save("1.jpg")
    #img2.save("2.jpg")
    #img3.save("3.jpg")
    #img4.save("4.jpg")


def rotate_shuffle(pieces):
    #rotate randomly
    for index in range(len(pieces)):
        angle = random.choice([0, 90, 180, 270])
        pieces[index] = pieces[index].rotate(angle)
        random.shuffle(pieces)


def get_distance_between (edge1, edge2):
    if len(edge1) != len(edge2):
        print("[Error] lengths of the edges are not equal")
    distance = 0
    for index in range(len(edge1)):
        distance += math.sqrt( (edge1[index][0] - edge2[index][0]) ** 2 +
                               (edge1[index][1] - edge2[index][1]) ** 2 +
                               (edge1[index][2] - edge2[index][2]) ** 2 )

    return distance


def get_optimal_pairs(n, np_pieces): # for the chosen piece
    collection_of_sorted_distances = []
    for i in range(len(np_pieces)): # for each edge of the chosen piece
        collection_of_distances = []
        for j in range(len(np_pieces)): # compare it with edges of some other piece
            if n == j:
                continue
            for k in range(len(np_pieces)): #with the edge k of some other piece j
                distance = get_distance_between(np_pieces[n].get_edge(i), np_pieces[j].get_edge(k))
                collection_of_distances.append((j, k, distance)) # piece j, edge k, distance value
        sorted_distances = sorted(collection_of_distances, key=itemgetter(2))
        collection_of_sorted_distances.append(sorted_distances) # sort the pairs in accordance with the distance and add it to the list

    return collection_of_sorted_distances
