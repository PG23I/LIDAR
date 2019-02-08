"""Created by Prannav Gupta: 2nd September 2018"""
"""Ver 3.0: 7th September 2018"""
"""Reads the raw ASCII data and exports the X,Y,Z co-ordinates,intensity and the photon count to writefile.txt"""

"""How to use this program: Place the program in a folder along with all the files (ASCII) 
from which the data is to be extracted. An output file will be created (or updated) with the comma separated values"""

import glob
import math
import numpy as np

def polar2cart(r, theta, phi):
    return [
         r * math.sin(theta) * math.cos(phi),
         r * math.sin(theta) * math.sin(phi),
         r * math.cos(theta)
    ]

"""Constants"""
"""Line-of-Sight Resolution (Meters)"""
RES_LOS = 7.5

"""Reference Co-Ordinates"""
ref_x = 0
ref_y = 0
ref_z = 0

"""Creates output file. New data will be appended"""
"""The value of writefileloc can be changed if the output file needs to be called something else"""
writefileloc = "writefile.txt"
writefile = open(writefileloc,'a')

"""Loop through every txt file in the folder"""
for filename in glob.glob('*.txt'):
    
    """Skips if writefile"""
    if not filename==writefileloc:

        """Automated file handling using with"""
        with open(filename,'r') as readfile:

            """Reading the Data in the Ascii Output"""
            data = readfile.readlines()
            
            """Extracting the Zenith and the Azimuth Angles (Converted to Radians) accoring to LIDAR Documentation"""
            sdata = data[1].split()
            zenith = math.radians(float(sdata[8]))  
            azimuth = math.radians(float(sdata[9])) 

            """Computing the base X,Y,Z co-ordinates. All others will be integral multiples of these"""
            """
            base_x = RES_LOS*math.cos(zenith)
            base_y = RES_LOS*math.cos(azimuth)
            base_z = RES_LOS*math.sin(zenith)
            
            base_x = RES_LOS*np.cos(azimuth)*np.sin(zenith)
            base_y = RES_LOS*np.sin(azimuth)*np.sin(zenith)
            base_z = RES_LOS*np.cos(zenith)"""

            base_x, base_y, base_z = polar2cart(RES_LOS, zenith, azimuth)

            """Analog and photon intensity data start on the 8th line"""
            buffer = 7

            """Looping through all the data and writing it to the write file"""
            for i in range(len(data)-buffer):

                """The actual co-ordinates"""
                x = base_x*(i+1) + ref_x
                y = base_y*(i+1) + ref_y
                z = base_z*(i+1) + ref_z

                """Getting the current row"""
                row_data = data[i+buffer].split()

                """Intensity and Photon Count"""
                intensity = row_data[0]
                photon_count = row_data[1]

                #Testing
                #print(x,y,z,intensity,photon_count)
                
                """Formatted output string"""
                output_str = ""
                output_str += str(x) + ',' + str(y) + ',' + str(z) + ',' + str(intensity) + ',' + str(photon_count) + '\n'

                #Testing
                #print(output_str)

                """Writing the values to the file"""
                writefile.write(output_str)

"""Releases the writefile"""
writefile.close()

