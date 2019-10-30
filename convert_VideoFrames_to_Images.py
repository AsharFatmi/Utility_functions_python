import cv2
import os

def main(video_path):

    save_dir = '/home/kingashar/Downloads/test'
    camera = cv2.VideoCapture(video_path)
    i = 0

    while True:
        return_value,image = camera.read()

        cv2.imshow('image',image)

        cv2.imwrite(os.path.join(save_dir,'{}.jpg'.format(i)),image)
        
        print(i)
        i += 1

        if cv2.waitKey(1)& 0xFF == ord('q'):
            break


    camera.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":

    import sys
    main(sys.argv[1])