import cv2
import math
class resample:

    def resize(self, image, scalex = None, scaley = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, scalex, scaley)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, scalex, scaley)

    def nearest_neighbor(self, image, scalex, scaley):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        img = cv2.imread(image)
        res = cv2.resize(img, fx=scalex, fy=scaley, interpolation=cv2.INTER_NEAREST)

        return res


    def bilinear_interpolation(self, image, scalex, scaley):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        (ow,oh) = image.shape # stores the old image width and height, BE SURE THAT OW AND OH ARE IN THE CORRECT ORDER!!
        (nw,nh) = (math.floor(scalex*ow),math.floor(scaley*oh)) # new width and height,again check the (ow,oh) order
        new_img = np.zeros(nw,nh) #create matrix populated with zeros,check (ow,oh)
        for(i,j) in new_img:
            ti = i/nw
            tj = j/nh
            old_i = math.floor(ti*ow) #the "old image" i coordinate
            old_j = math.floor(tj*oh)
            tl = image[old_i,old_j] # the top left coordinate
            tr = image[old_i+1, old_j] # top right
            bl = image[old_i, old_j+1] # bottom left coordinate THINK THIS MAY BE [OLD_I+1,OLD_J]
            br = image[old_i+1, old_j+1] # bottom right
            ui = ti*ow-old_i #may be ti*oh-old_j
            uj = tj*oh-old_j #see ui comment
            res = bilinear_interpolation(tl,tr,bl,br,(ui,uj))

        return res

