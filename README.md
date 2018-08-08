# pkl-Generator
This script will generate image to .pkl file 


  _____ _                 __  __                       _      _    "
  / ____| |               |  \/  |                     (_)    | |   "
 | (___ | |__   __ _ _ __ | \  / | __ _ _ __   __ _ ___ _  ___| | __"
  \___ \| '_ \ / _` | '_ \| |\/| |/ _` | '_ \ / _` / __| |/ __| |/ /"
**  ____) | | | | (_| | |_) | |  | | (_| | | | | (_| \__ \ | (__|   < "
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
