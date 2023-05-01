"""
The following code uses VEDO and POLYSCOPE to open and visualize 3D objects, respectively.

Link to VEDO: https://vedo.embl.es/
Link to POLYSCOPE: https://polyscope.run/py/

Tutorials:
    -PART 1 - https://towardsdatascience.com/python-libraries-for-mesh-and-point-cloud-visualization-part-1-daa2af36de30
    -PART 2 - https://towardsdatascience.com/python-libraries-for-mesh-point-cloud-and-data-visualization-part-2-385f16188f0f
"""

import time
from vedo import *      #Using VEDO to open 3D OBJ files
import polyscope as ps  #Using POLYSCOPE to visualize objects
from scipy.spatial.transform import Rotation as R

#My own functions
from shared_functions import decimalToBinary
from shared_functions import combine_rotations_3D

"""Opens Object using VEDO"""
def load_object(filename):
    mesh = Mesh(filename,)
    return mesh

"""Rotates the object, given a mesh and an angle for X, Y and Z"""
def rotation(obj, ax=0, ay=0, az=0, ref=None):
    axis_center = (0,0,0) #Rotation around axis
    obj_center  = np.mean(obj.vertices(), axis = 0) #Rotation around center

    obj.rotate(ax, axis=(1, 0, 0), point=obj_center, rad=False) #Rotate X
    obj.rotate(ay, axis=(0, 1, 0), point=obj_center, rad=False) #Rotate Y
    obj.rotate(az, axis=(0, 0, 1), point=obj_center, rad=False) #Rotate Z

    #Get object information
    faces = obj.faces()
    vertices = obj.vertices()
    
    return faces, vertices

#Parameters POLYSCOPE
ps.set_program_name("3D Viewer") #Set Program Name
ps.set_ground_plane_mode("none") #Disable "Ground"
ps.set_view_projection_mode("orthographic")
ps.set_navigation_style("free")
ps.set_up_dir("y_up")
obj_rotX = 0 #Initial object X angle
obj_rotY = 0 #Initial object Y angle
obj_rotZ = 0 #Initial object Z angle
iteration  = 0 #Counter
rotations, n_rotations = combine_rotations_3D() #Get rotations
output_path = "PlatonicSolidsImages/"
obj_names = ["1_Cilindro", "1_Cone", "1_Dodecaedro", "1_Esfera", "1_Hexaedro", "1_Icosaedro", "1_Octaedro", "1_Tetraedro", "1_Torulo"] #3D Objects
curr_obj = 0 #Current object to process

#Initialize POLYSCOPE
ps.init()

########################################################################################

# Executes every frame
def callback():
    global obj_rotX, obj_rotY, obj_rotZ
    global iteration, rotations, n_rotations
    global curr_obj, obj_names
    take_picture = True
    end_execution = len(obj_names)

    #Se já percorreu todos os objetos da lista, finaliza a execução.
    if curr_obj == end_execution:
        take_picture = False
        exit()

    #Load Object
    obj_name = f"PlatonicSolids3D/{obj_names[curr_obj]}.obj"
    fig_name = obj_name.split("/")[-1][0:-4] #Get name only
    mesh = load_object(obj_name)
    
    #Reset the camera view to the home view (a reasonable default view scaled to the scene).
    ps.reset_camera_to_home_view()

    #Rotaciona o objeto
    if iteration < n_rotations:
        obj_rotX, obj_rotY, obj_rotZ = rotations[iteration]
        iteration += 1
    else:
        iteration = 0
        curr_obj += 1

    #Rotate Object
    faces, vertices = rotation(mesh, obj_rotX, obj_rotY, obj_rotZ, None)

    #Creating the object
    ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces, color=(0.5,0.5,0.5), material="clay")

    # Take a screenshot of the current Scene
    if take_picture:
        output = output_path + f"{fig_name}-x{obj_rotX:.0f}y{obj_rotY:.0f}z{obj_rotZ:.0f}.png"
        ps.set_screenshot_extension(".png")
        ps.screenshot(filename=output, transparent_bg=True)
        
    #Log
    print(f"[Callback][{fig_name}][{iteration}] -> X:{obj_rotX}, Y:{obj_rotY}, Z:{obj_rotZ}")

    #Wait 0.5 seconds before next call
    time.sleep(0.2)

########################################################################################

#Set a function which will be called by polyscope on every UI draw iteration.
ps.set_user_callback(callback)

#Visualization with POLYSCOPE (It is possible using VEDO to visualize as follows: mesh.show())
ps.show()

#Clear the callback function
ps.clear_user_callback()