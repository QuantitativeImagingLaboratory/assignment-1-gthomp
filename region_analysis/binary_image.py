import numpy as np

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        (row, col) = image.shape
        hist = [0]*256 # I think this line and the following loops is calculating the frequency of pixels

        for i in range(row):
            for j in range(col):
                hist[image[i, j]] += 1


        return hist


    def expected_value(self, pdf, offset, total):
        exp = 0
        for i, val in enumerate(pdf):
            exp += (i+offset)*val/total
        return exp




    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = int(len(hist)/2)
        num_pixels = sum(hist) #width*height
        (uprev,vprev) = (0,0)
        u = expected_value(hist[:threshold],0,num_pixels)
        v = expected_value(hist[t:],threshold,num_pixels)
        threshold = int((u+v)/2)
        (du,dv) = (u-uprev,v-vprev)
        while du != 0 and dv != 0:
            (uprev, vprev) = (u, v)
            u = expected_value(hist[:threshold], 0, num_pixels)
            v = expected_value(hist[t:], threshold, num_pixels)
            threshold = int((u + v) / 2)
            (du, dv) = (u - uprev, v - vprev)

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        hist = compute_histogram(image)
        t = find_optimal_threshold(hist)
        for i in range(row):
            for j in range(col):
                if image[i,j] <= t:
                    bin_img[i,j] = 0
                else:
                    bin_img[i,j] = 255


        return bin_img


