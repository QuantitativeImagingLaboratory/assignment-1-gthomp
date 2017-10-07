class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here

        unknown_intensity = pt1+(unknown*(pt2-pt1))
        return unknown_intensity


    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value NW
        pt2: known point pt2 and f(pt2) or intensity value NE
        pt1: known point pt3 and f(pt3) or intensity value SW
        pt2: known point pt4 and f(pt4) or intensity value SE
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        i1 = self.linear_interpolation(pt1,pt2,unknown[0])
        i2 = self.linear_interpolation(pt3,pt4,unknown[0])
        i3 = self.linear_interpolation(i1,i2,unknown[1])
        return i3

        #or it could be
        """"""


