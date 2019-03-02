"""
This program provides various functions to correct data or to to process data.

All of these functions have been translated from the 'Data Proccessing' section of the manual. Many values are interpretations and are bound to be incorrrect.
Please read through the manual to modify these functions based on your needs.
"""

from math import pow
from math import exp
import scipy.integrate as integrate
import scipy.special as special

#Returns the dead time corrected photon counting signal
#INPUT: Observed count rate (ocr)
def photon_corrected(ocr):
    td = 260*pow(10,6) #td is the system dead time. Raymetrics uses 260 MHz
    signal = (ocr)/(1-(td*ocr))
    return signal

#Attempts to glue analog and photon counting signals
def gluing(analog,photon):
    if analog>(20*pow(10,6) and photon<(0.5*pow(10,6):
        return analog
    elif photon>(20*pow(10,6) and analog<(0.5*pow(10,6):
        return photon
    else:
        return "TODO" #Need to find the regression coefficient to transfer analog to photon if in the intermediate range

#signal function
def signal(z):
    return None #TODO

#Range corrected LIDAR signal
def rcs(z):
    return signal(z)*z*z

#Range Corrected exponentially attenuated Rayleigh backscattered coefficient
def bcs(beta,a,z):
    exp_part = integrate.quad(lambda: special.a(z))
    exp_part = (-1)*exp_part
    result = beta*z*z*exp(exp_part)
    return result

#Normalized range corrected
def nr(z,beta,a):
    z1 = z[0]
    z2 = z[len(z)-1]
    denominator = 0
    numerator = 0

    for i in z:
        numerator += rcs(i)
        denominator += bcs(beta,a,i)

    numerator = numerator/(z2-z1)
    denominator = denominator/(z2-z1)

    result = numerator/denominator
    result = result*rcs(z)

    return result

