"""
The following code uses VEDO and POLYSCOPE to open and visualize 3D objects, respectively.

Link to VEDO: https://vedo.embl.es/
Link to POLYSCOPE: https://polyscope.run/py/

Tutorials:
    -PART 1 - https://towardsdatascience.com/python-libraries-for-mesh-and-point-cloud-visualization-part-1-daa2af36de30
    -PART 2 - https://towardsdatascience.com/python-libraries-for-mesh-point-cloud-and-data-visualization-part-2-385f16188f0f
"""

from vedo import *      #Using VEDO to open 3D OBJ files
import polyscope as ps  #Using POLYSCOPE to visualize objects

"""Opens Object using VEDO"""
def load_object(filename):
    mesh = Mesh(filename,)
    return mesh

"""Rotates the object, given a mesh and an angle for X, Y and Z"""
def rotation(obj, ax=0, ay=0, az=0):
    #Rotate object in Z axis
    obj.rotate_x(ax, rad=False)
    obj.rotate_y(ay, rad=False)
    obj.rotate_z(az, rad=False)

    #Get object information
    faces = mesh.faces()
    vertices = mesh.vertices()
    
    return faces, vertices

#Parameters POLYSCOPE
ps.set_program_name("3D Viewer") #Set Program Name
ps.set_ground_plane_mode("none") #Disable "Ground"
ps.set_view_projection_mode("orthographic")

#Initialize POLYSCOPE
ps.init()

#Load Object
mesh = load_object("PlatonicSolids3D/1_Esfera.obj")

#Rotate Object
faces, vertices = rotation(mesh, 0, 0, 0)

#Creating the object
ps_mesh = ps.register_surface_mesh("my mesh", vertices, faces, color=(0.5,0.5,0.5), material="clay")

# Take a screenshot of the current Scene
#ps.set_screenshot_extension(".jpg");
#ps.screenshot(filename=None, transparent_bg=True)

#Visualization with POLYSCOPE (It is possible using VEDO to visualize as follows: mesh.show())
ps.show()