import os

class SheetCalculator:
    """A command line utility to calculate sheet number for images"""

    def __init__(self):
        self.filename = None
        self.directory = None
        self.name = None
        self.extension = None

    def filebrowser(self):
        self.filename = input("Enter the path of the image file: ")
        if not os.path.isfile(self.filename):
            print("Error: Invalid file path.")
            return False

        self.directory = os.path.dirname(os.path.realpath(self.filename))
        self.name, self.extension = os.path.splitext(os.path.basename(self.filename))
        os.chdir(self.directory)
        print("File details:")
        print("File name:", self.name)
        print("File extension:", self.extension)
        print("Directory:", self.directory)
        return True

    def tfwmaker(self):
        try:
            sf = float(input("Enter the Scale factor (eg: 1200): "))
            dpi = float(input("Enter the Scanning Resolution (eg: 300): "))
        except ValueError:
            print("Error: Invalid input. Scale factor and Scanning Resolution must be numbers.")
            return

        cellsize = 0.0254 * sf / dpi
        print("Cell Size:", cellsize)

        # Create a new tfw file and write it
        tfw_filename = self.name + ".tfw"
        with open(tfw_filename, "w") as outfile:
            outfile.write(str(cellsize) + "\n")
            outfile.write("0\n")
            outfile.write("0\n")
            outfile.write(str(-cellsize) + "\n")
            outfile.write("500000\n")
            outfile.write("3100000\n")

        print(f"TFW file '{tfw_filename}' created successfully.")

def main():
    print("Sheet Calculator by Ganesh")
    calculator = SheetCalculator()

    if not calculator.filebrowser():
        return

    calculator.tfwmaker()

if __name__ == "__main__":
    main()
