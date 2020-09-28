# This is a sample Python script.
import cv2
import numpy
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    img1 = cv2.imread('TestImage1.tif')

    Rate= 0.05;
    downsize = cv2.resize(img1, None, fx=Rate, fy=Rate, interpolation=cv2.INTER_AREA)

# Image Cutting Line Confirm
    Cutline = [ 72 , 198]
    downsize[Cutline[0], :, 0] =255;
    downsize[Cutline[1], :, 0] = 255;

    Realimage = img1[int(Cutline[0]/Rate):int(Cutline[1]/Rate), :, :]
    Realsmall = cv2.resize(Realimage, None, fx=0.25, fy=0.25, interpolation = cv2.INTER_AREA)
    cv2.imshow("Test", Realsmall)
    cv2.waitKey(0)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
