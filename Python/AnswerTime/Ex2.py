#from datetime import time
import requests

sites = ['http://www.google.com', 'http://www.youtube.com', 'http://www.polimi.it']
avgs = []
totreq = 20

for site in sites:
      times = []
      for request in range(totreq):
            r = requests.get(site)
            times.append(r.elapsed.microseconds/1000)
      avgs.append(sum(times)/totreq)
      print (sum(times)/totreq)
print(sites[avgs.index(min(avgs))], " is the better performing site.")
print(sites[avgs.index(max(avgs))], " is the worst performing site.")

