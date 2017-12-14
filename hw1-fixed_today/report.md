1 resampling) interpolation.py-- I wrote the linear_interpolation method
following the algorithm described in the class slides.
The bilinear_interpolation method utilizes the linear interpolation
method by passing the first two bilinear arguments (pt1,pt2) to the first 
call to linear_interpolation along with the first value of the unknown location tuple which returns intensity 1.
The second two arguments (pt3,pt4) and first value of the unknown location tuple are passed to the second call 
of linear_interpolation which returns intensity 2.
To find the value lying between the intensities returned by the first two calls to linear_interpolation
I passed the intensity1,intensity2, and the second value of the unknown location tuple to linear_interpolation
which returns the desired intensity.  

resample.py-- This bilinear_interpolation method first assigns a tuple
to hold the dimensions of the image that is passed as an argument.
Next I assign a tuple that holds the dimensions of the new interpolated
image. I also created a normalized scale that allows me to associate
pixels from the old image to pixels of the interpolated image.!!!


2 region counting) binary_image.py-- compute histogram returns the number
of occurrences of intensities in the image. 

expected_value and find_optimal_threshold compute the optimal threshold
value by averaging the expected values on either side of the current threshold

binarize sets intensity values less than the threshold to black, and values
greater than the threshold to white.

 cell_counting.py-- blob coloring is done by checking the current black 
pixel and its adjacent pixels for membership in a region(blob)

compute_statistics takes the dictionary returned by the blob_coloring function
and ignores areas less than 15 pixels and returns the remaining key value pairs


