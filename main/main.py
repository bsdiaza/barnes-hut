import os
from common import *
import numpy as np

# Number of bodies (may be smaller according to the distribution chosen).
G1_N = 100
G2_N = 70

# Mass of the N bodies.
G1_max_mass = 50. # Solar masses
G2_max_mass = 50. # Solar masses

# Supermassive Central Black Hole data
G1_BHM = 1.5*1.e6 
G1_BHposition = array([.45, .45, .45]) 
G1_BHmomentum = array([0.,0.,0.]) 

G2_BHM = 1.2*1.e6 
G2_BHposition = array([.85, .85, .85]) 
G2_BHmomentum = array([10000,-300000.,-300000]) 

#Parameters of the galaxy plane orientation 
G1_alpha=.0    #Angle in the plain x,y
G1_beta=.0     #Inclination

G2_beta=.6     #Inclination
G2_alpha=.1    #Angle in the plain x,y

# Initial radius of the distribution
G1_ini_radius = 20 #kpc

G2_ini_radius = 15 #kpc

# Number of time-iterations executed by the program.
n = 8000

# Frequency at which .PNG images are written.
img_step = 25

# Folder to save the images
image_folder = os.getcwd() + '\\images\\'

# Name of the generated video
video_name = 'video.mp4'

# Generate galaxy # 1 & galaxy # 2
galaxy_1 = galaxy_init(G1_N, G1_max_mass, G1_BHM, G1_BHposition, G1_BHmomentum, G1_ini_radius, G1_alpha, G1_beta, 'blue')
galaxy_2 = galaxy_init(G2_N, G2_max_mass, G2_BHM, G2_BHposition, G2_BHmomentum, G2_ini_radius, G2_alpha, G2_beta, 'yellow')

bodies = np.concatenate((galaxy_1, galaxy_2))
print('Total number of bodies: ', len(bodies))

evolve(bodies, n, img_step, image_folder)

create_video(image_folder, video_name)
#create_avi_video(image_folder, 'video.avi')
