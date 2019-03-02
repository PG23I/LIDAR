"""
This program provides various functions to correct data or to to process data
"""

from math import pow

#Returns the dead time corrected photon counting signal
#INPUT: Observed count rate (ocr)
def photon_corrected(ocr):
    td = 260*pow(10,6) #td is the system dead time. Raymetrics uses 260 MHz
    signal = (ocr)/(1-(td*ocr))
    return signal
