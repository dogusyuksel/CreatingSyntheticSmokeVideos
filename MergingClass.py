import numpy as np
import cv2

class MergingClass():
    def __init__(self, out_vid_x_len = 320, out_vid_y_len = 240, second_vid_resized_ratio = 4, merging_region = 1, second_vid_rotation = 0, out_vid_fps = 25, is_grey_out = 'false'):
        """Either load pretrained from imagenet, or load our saved
        weights from our own training."""

        self.out_vid_x_len            = out_vid_x_len
        self.out_vid_y_len            = out_vid_y_len
        self.second_vid_resized_ratio = second_vid_resized_ratio
        self.merging_region           = merging_region
        self.second_vid_rotation      = second_vid_rotation
        self.out_vid_fps              = out_vid_fps
        self.is_grey_out              = is_grey_out

    def merge(self, inp_image_path, inp_video_path, out_vid_path):

        ###################CONFIG
        DEFINE_X_PIXEL_MULTIPLICATION = 40
        DEFINE_Y_PIXEL_MULTIPLICATION = 30
        
        DEFINE_REGION_1 = 1
        DEFINE_REGION_2 = 2
        DEFINE_REGION_3 = 3
        DEFINE_REGION_4 = 4
        
        DEFINE_NO_ROTATION       = 0
        DEFINE_ROTATION_LEFT     = 1
        DEFONE_ROTATION_LEFTUP   = 2
        DEFINE_ROTATION_RIGHTUP  = 3
        DEFINE_ROTATION_RIGHT    = 4
        ##############END CONFIG

        cap = cv2.VideoCapture(inp_video_path)
        
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(out_vid_path, fourcc, self.out_vid_fps , (self.out_vid_x_len, self.out_vid_y_len))
        
        otherImage = cv2.imread(inp_image_path, cv2.IMREAD_COLOR)
        otherImage = cv2.resize(otherImage,(self.out_vid_x_len, self.out_vid_y_len))
        clone_img = otherImage.copy()
        
        lenMultiplier = 4
        if(self.second_vid_resized_ratio == 1):
            lenMultiplier = 1
        elif(self.second_vid_resized_ratio == 2):
            lenMultiplier = 2
        elif(self.second_vid_resized_ratio == 3):
            lenMultiplier = 3
        elif(self.second_vid_resized_ratio == 4):
            lenMultiplier = 4
        
        smoke_vide_resized_x_len = DEFINE_X_PIXEL_MULTIPLICATION * lenMultiplier
        smoke_vide_resized_y_len = DEFINE_Y_PIXEL_MULTIPLICATION * lenMultiplier
        
        
        myImageWithTransparency = np.zeros([smoke_vide_resized_y_len,smoke_vide_resized_x_len,3],dtype=np.uint8)
        myImageWithTransparency.fill(0) # or img[:] = 255
        
        x_shift = 0
        y_shift = 0
        
        if(self.merging_region == DEFINE_REGION_1):
            #1. region
            y_shift = 0
            x_shift = 0
        elif(self.merging_region == DEFINE_REGION_2):
            #2. region
            y_shift = self.out_vid_x_len - smoke_vide_resized_x_len - 1
            x_shift = 0
        elif(self.merging_region == DEFINE_REGION_3):
            #3. region
            y_shift = 0
            x_shift = self.out_vid_y_len - smoke_vide_resized_y_len - 1
        elif(self.merging_region == DEFINE_REGION_4):
            #4. region
            y_shift = self.out_vid_x_len - smoke_vide_resized_x_len - 1
            x_shift = self.out_vid_y_len - smoke_vide_resized_y_len - 1
        
        
        rotation_contant = DEFINE_NO_ROTATION
        if(self.second_vid_rotation == DEFINE_NO_ROTATION):
            rotation_contant = 0
        elif(self.second_vid_rotation == DEFINE_ROTATION_LEFT):
            rotation_contant = 90
        elif(self.second_vid_rotation == DEFINE_ROTATION_RIGHTUP):
            rotation_contant = -45
        elif(self.second_vid_rotation == DEFONE_ROTATION_LEFTUP):
            rotation_contant = 45
        elif(self.second_vid_rotation == DEFINE_ROTATION_RIGHT):
            rotation_contant = -90
            
        
        
        mask = np.zeros([smoke_vide_resized_y_len,smoke_vide_resized_x_len,3],dtype=np.uint8)
        mask.fill(0) # or img[:] = 255
        
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                #sleep(0.5)
                
                frame = cv2.resize(frame,(smoke_vide_resized_x_len, smoke_vide_resized_y_len))
                
                
                M = cv2.getRotationMatrix2D((smoke_vide_resized_x_len/2, smoke_vide_resized_y_len/2), rotation_contant, 1)
                frame = cv2.warpAffine(frame, M, (smoke_vide_resized_x_len, smoke_vide_resized_y_len))
                
                otherImage = clone_img.copy()
                # manipulate background
                for y in range(0, smoke_vide_resized_x_len):
                    for x in range(0, smoke_vide_resized_y_len):
                        threeColor = frame[x, y]
                        threeColor2 = otherImage[x + x_shift, y + y_shift]
                        if ((threeColor[0] < 127) and (threeColor[1] > 127) and (threeColor[2] < 127)): #it is green
                            threeColor2 = otherImage[x + x_shift, y + y_shift]
                        else:
                            threeColor2 = frame[x, y]
                        
                        if ((threeColor[0] == 0) and (threeColor[1] == 0) and (threeColor[2] == 0)): #it is green
                            threeColor2 = otherImage[x + x_shift, y + y_shift]
                            
                        otherImage[x + x_shift, y + y_shift] = threeColor2
                
                        
                if(self.is_grey_out   == 'true'):
                    otherImage = cv2.cvtColor(otherImage, cv2.COLOR_BGR2GRAY);
                    
        
                # write the flipped frame
                out.write(otherImage)
        
                cv2.imshow('frame',otherImage)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        
        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()