# ImageCropper

### Description:
This Python application is designed for the pre-processing stage of preparing machine learning datasets. Its main function is to crop specific regions of interest from images and save them in a designated output directory.

### Environmental Requirements:
* Python 3.9
* Tkinter
* OpenCV
* PIL
* numpy

### How to Use:
  Run the application using Python 3.9

  Load a data directory (root) with the following structure:

    root -> /images/ -> contains color image sources 
            /labels/ -> contains mask images of '/images/' directory
Use the left and right arrow keys to load the previous and next images, respectively.

Select the region of interest (ROI) by clicking and dragging on the preview image.

Save the cropped ROI by right-clicking on the preview image.

The cropped ROI will be saved to the output directory found inside the root, named 'output'.

N.B. The status block will display the working status.

### Action Shortcuts:
* Left and Right arrow keys: Load the previous and next images, respectively.
* Left-click and drag: Select the crop region.
* Single left-click: Clear the previously selected ROI.
* Right-click: Crop and save the selected ROI.

### Troubleshooting:
If the application is not running, ensure that you have installed the required dependencies mentioned in the "Environmental Requirements" section.
