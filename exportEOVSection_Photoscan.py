#RÉPÁS Zoltán
#2023.

#### Init section ####################################################
import readModulEOV as EOV
import PhotoScan
doc = PhotoScan.app.document
chunk = doc.activeChunk
#### End of init ######################################################

#### SETTINGS ########################################################
#   Edit before use:
type = "tif"                            #file type of the exported picture
folder = "C:/python/HelloAgiSoft/"      #path of export directory need to be exist
d_x = d_y = 0.5                         #Resolution of the ortho mosaic in [m]:

proj = PhotoScan.CoordinateSystem()     #Coordinate System Datum:
proj.init("EPSG::23700")
#EOV:"EPSG::23700"
#WGS84:"EPSG::4326"

#######################################################################
def exportSection(sectionEOV):
    global folder
    global path
    global type
    global proj
    global d_x
    global d_y
    coords = EOV.readEOV(sectionEOV)        #Calc the coordinates (at readmodulEOV.py file)
    print ('Starting export:')
    path = folder + sectionEOV + "." + type
    print (path)
    # Define an export instruction for AgiSoft Photoscan
    chunk.exportOrthophoto(path, type, "mosaic", projection = proj, region = coords, dx = d_x, dy = d_y, write_kml=False, write_world=False)
    print (" ")

exportSection('75-313432')
