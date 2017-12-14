from collections import Counter
# import matplotlib.pyplot as plt #MAY NEED TO UNCOMMENT THIS
# import numpy as np    MAY NOT NEED TO IMPORT THIS HERE

### ERROR 1: actually needed these < FIXED
import numpy as np
import matplotlib.pyplot as plt
import random


class cell_counting:
    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        ### ADVICE: this function is kind of large, which makes it hard to follow

        # coordinate_array = dict()

        filled = 255
        empty = 0

        (row, col) = image.shape
        ### ERROR 2: needed parenthesis around row,col because it's a shape object < FIXED
        coordinate_array = np.zeros((row, col), dtype=np.uint32)  # make this uint32
        region_dict = {}
        k = 1 #region count
        ### ERROR 5: you check for intensities of 0 and 1, but in 'binary_image' you set max intensity as 255, not 1 < FIXED
        ### ERROR 6: 'binary_image'
        print(row, col)

        def create_region(r,c,k):

            coordinate_array[r,c] = k #array index: use brackets
            region_dict[k] = {(r,c)}  #tuple: use parentheses

        def add_to_north(r,c):

            coordinate_array[r,c] = coordinate_array[r-1, c] #the k value stored in north region
            region_dict[coordinate_array[r-1, c]].add((r,c)) #dict has sets and to add to a set we use .add function

        def add_to_left(r,c):

            coordinate_array[r,c] = coordinate_array[r,c-1] #the k value stored in left region
            region_dict[coordinate_array[r, c-1]].add((r,c))

        def update_coordinate_array(left_k, north_k): #update

            for (r,c) in region_dict[left_k]:
                coordinate_array[r,c] = north_k

        def update_region_dict(left_k, north_k):   #update

            for (r,c) in region_dict[left_k]:
                region_dict[north_k].add((r,c))

            #to remove left region
            del region_dict[left_k]



        for r in range(row):
            for c in range(col):

                current = image[r, c]
                north = None if r == 0 else image[r-1, c]
                left = None if c ==0 else image[r, c-1]

                # current = image[r, c]
                # north   = image[r - 1, c] if r > 0 else None  # setting these to None is necessary since 0 is the default value
                # left    = image[r, c - 1] if c > 0 else None

                ## left and north are black
                if current == filled and left == empty and north == empty:
                    create_region(r,c,k)
                    k += 1

                    # print("#1 ----")
                    # print(r - 1, c, coordinate_array[r - 1, c])
                    # print(r, c - 1, coordinate_array[r, c - 1], " ", r, c, coordinate_array[r, c])

                ## left is black, north is white
                elif current == filled and left == empty and north == filled:  # bottom left in pic
                    add_to_north(r,c)


                    # print("- #2 ---")
                    # print(r - 1, c, coordinate_array[r - 1, c])
                    # print(r, c - 1, coordinate_array[r, c - 1], " ", r, c, coordinate_array[r, c])

                ## left is white, north is black
                elif current == filled and left == filled and north == empty:
                    add_to_left(r,c)

                    # print("--- #3 -")
                    # print(r - 1, c, coordinate_array[r - 1, c])
                    # print(r, c - 1, coordinate_array[r, c - 1], " ", r, c, coordinate_array[r, c])

                ## left and north are white
                elif current == filled and left == filled and north == filled:

                    # print("---- #4-a")
                    # print(r - 1, c, coordinate_array[r - 1, c])
                    # print(r, c - 1, coordinate_array[r, c - 1], " ", r, c, coordinate_array[r, c])

                    add_to_north(r,c)  # R[c] = R[n]

                    # print("---- #4-b")
                    # print(r - 1, c, coordinate_array[r - 1, c])
                    # print(r, c - 1, coordinate_array[r, c - 1], " ", r, c, coordinate_array[r, c])

                    left_k = coordinate_array[r, c - 1]  # gives the k value of left
                    north_k = coordinate_array[r-1, c] #gives the k value of north

                    # print("left k",left_k)
                    # print("north k", north_k)
                    # print()

                    if left_k != north_k:  # if the pixels are black AND the coordinate_array are the same

                        update_coordinate_array(left_k, north_k)
                        update_region_dict(left_k, north_k)

                        # print("---- #4-c")
                        # print(r - 1, c, coordinate_array[r - 1, c])
                        # print(r, c - 1, coordinate_array[r, c - 1], " ", r, c, coordinate_array[r, c])
                        # print()





        for k, pixels in region_dict.items():
            color = random.randint(50, 200)
            for (r, c) in pixels:
                image[r, c] = color


        return region_dict

    def compute_statistics(self, region_dict):
        """Compute cell statistics area and location(centroid)
        takes as input
        region: a list of pixels in a region
        returns: area"""
        min_area = 15
        stats = {}

        ### ERROR 4: 'region_dict' is absolutely empty
        # results in 'stats' being absolutely empty
        print("region_dict: ")
        print(region_dict)

        for k, pixels in region_dict.items():
            area = len(pixels)
            if area < min_area:
                continue
            (ci, cj) = (0, 0)
            for (i, j) in pixels:
                ci += i
                cj += j
            ci /= area
            cj /= area
            stats[k] = {'x': cj, 'y': ci, 'area': area}

        print("stats: ")
        print(stats)

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        plt.clf()
        plt.imshow(image, interpolation='none', cmap=plt.cm.gray)
        ### ERROR 3: expected 'stats' to be an object with data, but 'stats' is actually an integer < FIXED
        # look at line 72 in dip_hw1_region_analysis.py:
        #   stats = cell_count_obj.compute_statistics(regions) <--- compute_statistics
        # look at 'compute_statistics' above:
        #   returns 0, an integer
        for k, region_stats in stats.items():
            (x, y) = (region_stats['x'], region_stats['y'])
            plt.plot(x, y, 'r*')  # plots red asterisk
            plt.text(x, y, '{}:{}'.format(k, region_stats['area']), color='red')
        plt.show()
        plt.savefig('output/cellct/result.png')

        return image
