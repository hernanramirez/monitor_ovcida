


for p in psutil.process_iter():
    if p.name.startswith('condor_'):
        print p, p.username

