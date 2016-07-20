#!/usr/bin/python

try:
 import os 
except ImportError:
 print "Cannot import os module - this is needed for this code.";
 print "Exiting..."
 sys.exit();

try:
 import time 
except ImportError:
 print "Cannot import time module - this is needed for this code.";
 print "Exiting..."
 sys.exit();

# ===================
# Main Python section
# ===================

if __name__ == '__main__':
 
 load_avg = os.getloadavg()
 print "load average: %.2f, %.2f, %.2f" % (load_avg[0], load_avg[1],
 load_avg[2]);
 
# end main
