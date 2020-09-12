#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:04:55 2020

@author: prashansahareshdhomane
"""


import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5) ==ord('q'):
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()
