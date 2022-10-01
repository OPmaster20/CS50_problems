from pyfiglet import Figlet
import sys
king=['slant','rectangles','alphabet','acrobatic','alphabet','banner']
queen=['-f','--font']
if sys.argv[1] not in queen:
    sys.exit("Invalid usage")
if sys.argv[2] not in king:
    sys.exit("Invalid usage")
figlet = Figlet(font=sys.argv[2])
x=str(input("Input:"))
print("Output:",figlet.renderText(x))