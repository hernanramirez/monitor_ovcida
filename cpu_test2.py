
try:
  import psutil 
except ImportError:
   print "Cannot import psutil module - this is needed for this application.";
   print "Exiting..."
   sys.exit();
 
# ===================
# Main Python section
# ===================
 
if __name__ == '__main__':
 
   # Current system-wide CPU utilization as a percentage
   # ---------------------------------------------------
   # Server as a whole:
   percs = psutil.cpu_percent(interval=0.5, percpu=False)
   print " CPU ALL: ",percs," %";
 
   # Individual CPUs
   percs = psutil.cpu_percent(interval=0.5, percpu=True)
   for cpu_num, perc in enumerate(percs):
      print " CPU%-2s %5s%% " % (cpu_num, perc);
   # end for
 
 
   # Details on Current system-wide CPU utilziation as a percentage
 
   # --------------------------------------------------------------
   # Server as a whole
   perc = psutil.cpu_times_percent(interval=0.5, percpu=False)
   print " CPU ALL:";
   str1 = "   user:    %5s%%  nice:  %5s%%" % (perc.user, perc.nice);
   str2 = "   system:  %5s%%  idle:  %5s%%  " % (perc.system, perc.idle);
   str3 = "   iowait:  %5s%%  irq:   %5s%% " % (perc.iowait, perc.irq );
   str4 = "   softirq: %5s%%  steal: %5s%% " % (perc.softirq, perc.steal);
   str5 = "   guest:   %5s%% " % (perc.guest);
   print str1
   print str2
   print str3
   print str4
   print str5;
 
   # Individual CPUs
   percs = psutil.cpu_times_percent(interval=0.5, percpu=True)
   for cpu_num, perc in enumerate(percs):
      print " CPU%-2s" % (cpu_num);
      str1 = "   user:    %5s%%  nice:  %5s%%" % (perc.user, perc.nice);
      str2 = "   system:  %5s%%  idle:  %5s%%  " % (perc.system, perc.idle);
      str3 = "   iowait:  %5s%%  irq:   %5s%% " % (perc.iowait, perc.irq );
      str4 = "   softirq: %5s%%  steal: %5s%% " % (perc.softirq, perc.steal);
      str5 = "   guest:   %5s%% " % (perc.guest);
      print str1
      print str2
      print str3
      print str4
      print str5;
   # end for
 
# end if
