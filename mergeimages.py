from MergingClass import MergingClass
import os

# REGIONS
#---------------------
#|  1    |    2     | 
#--------------------
#|  3    |    4    | 
#-------------------


# Do not touch this part
DEFINE_REGION_1 = 1
DEFINE_REGION_2 = 2
DEFINE_REGION_3 = 3
DEFINE_REGION_4 = 4

DEFINE_NO_ROTATION       = 0
DEFINE_ROTATION_RIGHTUP  = 1
DEFONE_ROTATION_LEFTUP   = 2
DEFINE_ROTATION_LEFT     = 3
DEFINE_ROTATION_RIGHT    = 4

DEFINE_X_PIXEL_MULTIPLICATION = 40
DEFINE_Y_PIXEL_MULTIPLICATION = 30

DEFINE_BACKROUND_IMAGE_FOLDER = "SmokeRelated/SmokeStaticImages/"
DEFIE_SMOKE_VIDEO_FOLDER = "SmokeRelated/SmokeVideos/"
DEFINE_OUTPUT_VIDEO_FOLDER = "SmokeRelated/SmokeDataSet/"
# End of do not touch

DEFINE_RESIZED_VIDEO_X_LEN                          = 320
DEFINE_RESIZED_VIDEO_Y_LEN                          = 240
DEFINE_SMOKE_VIDE_RESIZE_RATIO_WRT_RESIZED_VIDEO    = 4  #between 1 to 4
DEFINE_SMOKE_VIDEO_MERGE_REGION_SELECTION = DEFINE_REGION_2
DEFINE_ROTATION_DEGREE = DEFINE_NO_ROTATION
DEFINE_OUTPUT_VIDEO_FPS = 25.0

DEFINE_SMOKE_VIDEO_FILENAME = "vid15.avi"
DEFINE_STATIC_IMAGE_FILENAME = "nonfire.390.jpg"
DEFINE_OUTPUT_VIDEO_FILENAME = "Edited_" + str(DEFINE_STATIC_IMAGE_FILENAME) + "_resizeRatio_" + str(DEFINE_SMOKE_VIDE_RESIZE_RATIO_WRT_RESIZED_VIDEO) + "_region_" + str(DEFINE_SMOKE_VIDEO_MERGE_REGION_SELECTION) + "_rotationDegree_" + str(DEFINE_ROTATION_DEGREE) + ".avi"

DEFINE_IS_OUTPUT_GREYSCALE = 'false'


def findfiles(directory):
    objects = os.listdir(directory)  # find all objects in a dir

    files = []
    for i in objects:  # check if very object in the folder ...
        if isFile(directory + i):  # ... is a file.
            files.append(i)  # if yes, append it.
    return files

def isFile(object):
    try:
        os.listdir(object)  # tries to get the objects inside of this object
        return False  # if it worked, it's a folder
    except Exception:  # if not, it's a file
        return True



# get all video names here
the_list_video = findfiles("SmokeRelated/SmokeVideos")

# get all static images here
the_list_image = findfiles("SmokeRelated/SmokeStaticImages")


img_rotat = 0
img_res = 0
img_reg = 0
grey_cnt = 0
video_cnt = 0

for i in the_list_video:
    for j in the_list_image:
        DEFINE_SMOKE_VIDEO_FILENAME = str(i)
        DEFINE_STATIC_IMAGE_FILENAME = str(j)
        for img_rotat in range(0, 5):
            DEFINE_ROTATION_DEGREE = img_rotat
            for img_res in range(1, 5):
                DEFINE_SMOKE_VIDE_RESIZE_RATIO_WRT_RESIZED_VIDEO = img_res
                for img_reg in range(1, 5):
                    DEFINE_SMOKE_VIDEO_MERGE_REGION_SELECTION = img_reg
                    DEFINE_IS_OUTPUT_GREYSCALE = 'false'
                    
                    # stars main code here
                    video_cnt = video_cnt + 1
                    DEFINE_OUTPUT_VIDEO_FILENAME = "Edited_" + str(DEFINE_SMOKE_VIDEO_FILENAME) + "_" + str(DEFINE_STATIC_IMAGE_FILENAME) + "_resizeRatio_" + str(DEFINE_SMOKE_VIDE_RESIZE_RATIO_WRT_RESIZED_VIDEO) + "_region_" + str(DEFINE_SMOKE_VIDEO_MERGE_REGION_SELECTION) + "_rotationDegree_" + str(DEFINE_ROTATION_DEGREE) + "_" + str(DEFINE_IS_OUTPUT_GREYSCALE) + ".avi"
                    mergeInstance = MergingClass(DEFINE_RESIZED_VIDEO_X_LEN, DEFINE_RESIZED_VIDEO_Y_LEN, DEFINE_SMOKE_VIDE_RESIZE_RATIO_WRT_RESIZED_VIDEO, DEFINE_SMOKE_VIDEO_MERGE_REGION_SELECTION, DEFINE_ROTATION_DEGREE, DEFINE_OUTPUT_VIDEO_FPS, DEFINE_IS_OUTPUT_GREYSCALE)
                    mergeInstance.merge(DEFINE_BACKROUND_IMAGE_FOLDER + DEFINE_STATIC_IMAGE_FILENAME, DEFIE_SMOKE_VIDEO_FOLDER + DEFINE_SMOKE_VIDEO_FILENAME, DEFINE_OUTPUT_VIDEO_FOLDER+DEFINE_OUTPUT_VIDEO_FILENAME)
                    print("Finished " + str(video_cnt) + ". video!")
                

print("End of This Process!")




















