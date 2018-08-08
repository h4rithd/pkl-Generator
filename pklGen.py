from pygame import surfarray, image, display
import pygame
import pickle
import sys

print"-----------------------------------------------------------------------"
print"   _____ _                 __  __                       _      _    "
print"  / ____| |               |  \/  |                     (_)    | |   "
print" | (___ | |__   __ _ _ __ | \  / | __ _ _ __   __ _ ___ _  ___| | __"
print"  \___ \| '_ \ / _` | '_ \| |\/| |/ _` | '_ \ / _` / __| |/ __| |/ /"
print"  ____) | | | | (_| | |_) | |  | | (_| | | | | (_| \__ \ | (__|   < "
print" |_____/|_| |_|\__,_| .__/|_|  |_|\__,_|_| |_|\__,_|___/_|\___|_|\_\/"
print"                    | |                                             "
print"                    |_|   .pkl Generator "
print""
print"-----------------------------------------------------------------------"
print"------------------      Coded By ShapManasick         -----------------"
print"-------------------------   HarithDilshan   ---------------------------"
print""

var = len(sys.argv) 
if var != 3 :
	print " [!] No argument supplied"
	print " pklGen 1.0 ( https://www.facebook.com/shap.manasick )"
	print " Usage: pklGen [SourceImage] [Output.pkl]"
	print "	EXAMPLES:"
	print "   python pklGen.py abc.png data.pkl"  
	exit()

image = image.load(sys.argv[1])
print "Image Load successfully"
surfarray.use_arraytype("numpy") 
screenpix = surfarray.pixels3d(image) 
file = open(sys.argv[2], "wb")
pickle.dump(screenpix, file)
file.close()
print "Mission completed !!"
print sys.argv[2] + " genarated successfully!"
exit()


