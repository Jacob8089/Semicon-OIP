import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d
import glob
from scipy import optimize
import warnings
warnings.filterwarnings('ignore')
import csv
import numpy.linalg as la
import scipy.optimize as sopt
from mpl_toolkits.mplot3d import axes3d
import random as ran
import matplotlib
from sympy import *
from pyswarm import pso
from tabulate import tabulate
from flet import *

def load_image(img_url):
    img = mpimg.imread(img_url)
    img = img.astype(np.uint8)
    return img
 
def crop_image(img, x):
    img_crop = img[0:x, :]
    return img_crop
 
def hist256(imgint8):
    hist = np.zeros(256)
    for cnt in range(256):
    hist[cnt] = np.sum(imgint8 == cnt)
    return (hist)

def threshold(imgINT, ath):
    imgTH = np.zeros(imgINT.shape)
    imgTH[imgINT >= ath] = 255
    imgTH[imgINT <= ath] = 0
     return imgTH.astype(np.uint8)
 
def contrast(imgInt, a):
    imgInt_contrast = crop_level(imgInt.astype(np.float64) * a)
     return imgInt_contrast.astype(np.uint8)
 
def crop_level(imgInt):
    imgInt[imgInt <= 0] = 0
    imgInt[imgInt >= 255] = 255
    return imgInt.astype(np.uint8)

def filter_image(I,H): 
    # Convolution-based filtering: 
    Filtered = conv2(np.double(I),np.double(H)); 
    # Reducing to original size and converting back to uint8: 
    # and CUT to the range between 0 and 255.
    return (crop_levels(Filtered)).astype(np.uint8)

def conv2(x, y, mode='same'):
    # mimic matlab's conv2 function: 
    return np.rot90(convolve2d(np.rot90(x, 2), np.rot90(y, 2), mode=mode), 2)
    
def median_filter(imgINT, radius):
    padded = np.pad(imgINT, ((radius, radius), (radius, radius)), 'reflect').astype(np.floa
    N, M = imgINT.shape
    filtered = np.zeros(imgINT.shape)
    for cntN in range(N):
    for cntM in range(M):
    pidN = cntN+radius
    pidM = cntM+radius
    filtered[cntN,cntM] = np.floor(np.median(padded[pidN-radius:pidN+radius+1, pidM
    return filtered.astype(np.uint8)


