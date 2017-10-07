from collections import Counter
#import matplotlib.pyplot as plt #MAY NEED TO UNCOMMENT THIS
#import numpy as np    MAY NOT NEED TO IMPORT THIS HERE
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        #regions = dict()
        (row,col) = image.shape
        regions = np.zeros(row,col,dtype = np.uint32) #make this uint32
        region_dict = {}
        k = 1
        for i in range(row):
            for j in range(col):
                if image[i,j] == 1 and image[i,j-1] == 0 and image[i-1,j] == 0:
                    regions[i,j] = k
                    region_dict[k] = set([i,j]) # NEW   may not need to be [] around i,j
                    k += 1
                elif image[i,j] == 1 and image[i,j-1] == 0 and image[i-1,j] == 1: #bottom left in pic
                    regions[i,j] = regions[i-1,j] #R[c] = R[n]
                    region_dict[regions[i,j]].add(i,j) # for the k value in regions matrix(key) add the coordinate tuple to the list of values associated with the key
                elif image[i,j] == 1 and image[i,j-1] == 1 and image[i-1,j] == 0:
                    regions[i,j] = regions[i,j-1]
                    region_dict[regions[i,j]].add(i,j) #top right in pic
                elif image[i,j] == 1 and image[i,j-1] == 1 and image[i-1,j] == 1:
                    regions[i, j] = regions[i - 1, j]  # R[c] = R[n]
                    if regions[i-1,j] == regions[i,j-1]: # if the pixels are black AND the regions are the same
                        region_dict[regions[i,j]].add(i,j)
                        continue
                    for r in region_dict[regions[i,j-1]]:
                        regions[r[0],r[1]] = regions[i,j] #LOOK AGAIN
                    union = region_dict[regions[[i-1,j]]] or region_dict[regions[i,j-1]]
                    union.add(i,j)
                    region_dict[regions[i,j-1]].clear() #SHOULD THIS BE DEL INSTEAD OF CLEAR??
                    region_dict[regions[i,j]] = union
                if regions[i,j-1] != regions[i-1,j]: # if pixels (left and top) are black and regions are different, make regions the same
                    regions[i,j-1] = regions[i-1,j]



        return region_dict

    def compute_statistics(self, region_dict):
        """Compute cell statistics area and location(centroid)
        takes as input
        region: a list of pixels in a region
        returns: area"""
        min_area = 15
        stats = {}
        for k,pixels in region_dict.items():
            area = len(pixels)
            if area < min_area:
                continue
            (ci,cj) = (0,0)
            for (i,j) in pixels:
                ci += i
                cj += j
            ci /= area
            cj /= area
            stats[k] = {'x':cj,'y':ci, 'area':area}

        print(stats)



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        plt.clf()
        plt.imshow(image,interpolation='none',cmap=plt.cm.gray)
        for k,region_stats in stats.items():
            (x,y) = (region_stats['x'],region_stats['y'])
            plt.plot(x,y,'r*') # plots red asterisk
            plt.plot(x,y,"{}:{}".format(k,region_stats['area']))
        plt.show()
        plt.savefig('output/cellct/result.png')

        return image

