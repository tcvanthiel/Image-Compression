import matplotlib.pyplot as plt
import numpy as np

def decompose_rgb(image):
    """
    Decompose rgb image into its red, green and blue components. Output three arrays
    """
    image_r = image[:,:,0] #Extract the red values from the RGB code
    image_g = image[:,:,1] #Extract the green values from the RGB code
    image_b = image[:,:,2] #Extract the blue values from the RGB code
    
    return(image_r,image_g,image_b)

def matrix_to_image(input_matrix):
    dummy_image = np.ones(input_matrix.shape[0],input_matrix[1],3)/256
    matrix_reshaped = np.asarray(input_matrix[:,:,np.newaxis])   #Reshape the values from a 2D Array to an ndarray
    image = matrix_reshaped*dummy_image 
    return(image)

def rgb_to_gray(image, c = [0.2125,0.7154,0.0721]):
    """
    This function takes an RGB image and converts it into grayscale. 
    The output consists of two parts; (1) a 2D numpy array of the gray values and (2) a reshaped (:,:,3) version suitable for image outputting 
    """
    image_r, image_g, image_b = decompose_rgb(image)

    gray_values = c[0]*image_r+c[1]*image_g+c[2]*image_b #Calculate the 'gray' values 
    gray_image = matrix_to_image(gray_values)
    return(gray_values, gray_image)