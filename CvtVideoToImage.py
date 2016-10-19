"""
function:The code can transfer videos to many pictures using ffmpeg and subprocess
"""
"""
author:zhipengliu
data:2016-7-18
convert video to image
"""

import time
import os, sys
from GetSubfileName import *
import subprocess
import time

#-------------------------setting parameter--------------------------
pathRGBVideo = '/media/zhipengliu/backupNHCI/zhipengliu/dataset/convertContinousToIsoGestrueTrain'
pathImageJpg = '/home/zhipengliu/dataset/RGBVideoToImageJPG'
# pathRGBVideo = '/media/zhipengliu/backupNHCI/zhipengliu/dataset/CvtDepthVideoToFrontVideo'
# pathVideToImage = '/media/zhipengliu/backupNHCI/zhipengliu/dataset/VideoToImage'
# pathRGBoutput = '/home/zhipengliu/kerasWork/ConGCompetetion/CNN_LSTM/C3DFeature/DepthFront_cliplength16'
nlabel = 6
# inputfilename = 'ConGesture_input_list_frontdepthvideo_nlabel249.txt'
# outputfilename = 'ConGesture_list_frontdepthvideo_prefixlabel249.txt'
#----------------------------end-------------------------------------

if __name__ == "__main__":
    timestart = time.time()
    subRGB = GetSubfileName(pathRGBVideo)
    featureCount = 0
    for i in range(nlabel):
        subfileName = subRGB[i]
        print "---------------" + subfileName + "----------------"
        subRGBfilePath = pathRGBVideo + "/" + subfileName

        oneLabelImagePath = pathImageJpg + "/" + subfileName
        if os.path.exists(oneLabelImagePath) ==False:
            os.mkdir(oneLabelImagePath)
        DTlRGBfileName = GetSubfileName(subRGBfilePath)
        labelVideoSize = len(DTlRGBfileName)
        count = 1
        for j in range(1, labelVideoSize + 1, 2):
            videostr = DTlRGBfileName[j]
            print "nvideo = " + videostr
            oneVideoPath = subRGBfilePath + "/" + videostr
            tmp = "%03d" % count
            count = count + 1
            finaloutput = oneLabelImagePath + "/" + tmp
            if os.path.exists(finaloutput) == False:
                os.mkdir(finaloutput)
            else:
                continue
            strcmd = "ffmpeg -i " + oneVideoPath + " -r 10 -f image2 " + finaloutput + "/%06d.jpg"
            subprocess.call(strcmd, shell=True)
        timeend = time.time()
        print "time = " + str(timeend - timestart)


#subprocess.call("ffmpeg -i /home/zhipengliu/competetion/C3D-master/examples/c3d_feature_extraction/0001.M.avi -r 10 -f image2 /home/zhipengliu/kerasWork/ConGCompetetion/CNN_LSTM/image/%06d.jpg", shell=True)
