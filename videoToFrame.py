import numpy as np
import cv2
import os

try:
    os.mkdir('videoToFrame')
    try:
        os.mkdir('videoToFrame/frames')
        os.mkdir('videoToFrame/videos')
    except:
        print("\tSub-directories already created")
except:
    print("\tDirectory videoToFrame already created")

base_path_videos = 'videoToFrame/videos/'
base_path_frames = 'videoToFrame/frames/'

for (rootDir, dirNames, filenames) in os.walk(base_path_videos):
        # loop over the filenames in the current directory
        if len(filenames) == 0:
            print('[INFO] NO VIDEOS DETECTED IN FOLDER: videoToFrame/videos')
            break
        for filename in filenames:
            filename_folder, _ = filename.split('.')
            print('[INFO] Opennig %s' % filename)
            try:
                os.mkdir(base_path_frames+filename_folder)
                print("\tDirectory %s created" % (base_path_frames + filename_folder))
            except OSError:
                print("\tDirectory %s already created" % (base_path_frames+filename_folder))
            cap = cv2.VideoCapture(base_path_videos+filename)
            frame_count, frame_save = 1, 1
            while(cap.isOpened()):
                ret, frame = cap.read()
                # cv2.imshow('frame',frame)
                if frame_count % 1 == 0:
                    try:
                        cv2.imwrite(base_path_frames+filename_folder+'/'+filename+'-frame_{}.png'.format(frame_save), frame)
                        frame_save += 1
                    except:
                        cap.release()
                frame_count += 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # cv2.destroyAllWindows()