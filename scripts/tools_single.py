#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  10 2018

@authors: MBac Team

Set of tools that will allow the image recognition in the experiments

"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def detect_container(img):
    """ detects the inner boundary of the petridish in an image
    input
        img: grayscale image as numpy array
    ouput: 
        cnt: an opencv contour object representing the inner border 
              of the petridish
    """
    # edge detection
    edges = cv.Canny(img,18,32)
    
    # dilate edges
    # to close small openings
    kernel = np.ones((2,2),np.uint8)
    edges = cv.dilate(edges,kernel,iterations = 2)
    
    #find contours
    im2, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, 
                                               cv.CHAIN_APPROX_NONE)
    
    #detect the biggest contour
    outer_cntIndex = np.argmax([cv.contourArea(cnt) for cnt in contours])
    outer_cnt = contours[outer_cntIndex]
    
    #filter contours that have area > 0.6*Area of max contour
    filt_cnts = [cnt for cnt in contours if cv.contourArea(cnt)>0.6*cv.contourArea(outer_cnt)]
    
    #get the minimun contour of the filterd ones
    inner_cntIndex = np.argmin([cv.contourArea(cnt) for cnt in filt_cnts])
    inner_cnt= filt_cnts[inner_cntIndex]
    
    # get the minimin enclosing circle for the inner contour
    # to get a perfect circular shape
    # (x,y),radius = cv.minEnclosingCircle(inner_cnt)
    # center = (int(x),int(y))
    # radius = int(radius)
    # cv.circle(img,center,radius,(255,0,255),1)
    
    return inner_cnt

def create_ROI(img, cnt):
    """ creates a mask displaying only the region inside cnt in the image 
    input
        img: grayscale image as numpy array
        cnt: opencv contour object representing the inner border 
              of the petridish
    output
        ROI: a binary mask (black/white), numpy array, representing the area inside 
             the petridish
    """
    
    pass

def calc_brightRange(img, ROI):
    """ calculates mimimum and maximum grayscale value inside the petridish empty area
    input
        img: grayscale image as numpy array
        ROI: a binary mask (black/white), numpy array, representing the are inside 
             the petridish
    output
        (minValue,maxValue): grayscale values (0-255) that apears in the empy area
                             of a petridish
    """
    pass

def detect_bacteria(img, ROI, minValue, maxValue):
    """ finds the bacteria region
    input
        img: grayscale image as numpy array
        ROI: a binary mask (black/white), numpy array, representing the are inside 
             the petridish
        (minValue,maxValue): grayscale values (0-255) that apears in the empy area
                             of a petridish
    output
        bac_cnts: a list of openCV contour objects representing the bacteria's region'
    """
    pass

def calc_area(cnts):
    """ calculate the total area inside all the contours
    input
        cnts: a list of openCV contour objects representing the bacteria's region
    output
        total_area: a float number that indicates the total number of pixels inside
                    all the contours 
    """
    pass
