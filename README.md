
# TFW Maker Command Line Utility

**TFW Maker** is a command line utility designed to calculate sheet numbers for images and generate ".tfw" files that contain transformation information. This utility can be useful for georeferencing images to specific coordinate systems or map projections.

## Usage

1. Make sure you have Python installed on your system.
2. Download the "TFW_Maker_CUI.py" script and save it to a directory.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script by typing the following command and hitting Enter:

   ```
   python TFW_Maker_CUI.py
   ```

5. The utility will prompt you to enter the path of the image file you want to process.
6. If the file path is valid, the utility will extract the file details (name, extension, and directory).
7. You will then be asked to enter the scale factor and scanning resolution for the image.
8. The utility will calculate the cell size and create a new ".tfw" file in the same directory as the image file.
9. The ".tfw" file will contain the necessary transformation parameters for the image.

**Note:** Make sure to enter valid numeric values for the scale factor and scanning resolution. Invalid inputs will result in an error.

## Example

Let's say you have an image file named "sample_image.jpg" located in the "/path/to/images" directory. Running the "TFW Maker" utility with this file will generate a "sample_image.tfw" file containing the transformation parameters.

## Credits

This "TFW Maker" utility was originally created by Ganesh.
