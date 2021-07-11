import requests
import matplotlib
import matplotlib.pyplot as plt


sites = ['http://www.google.com', 'http://www.youtube.com', 'http://www.polimi.it']

m = 0

for site in sites:
      times = [] # List Results

      for request in range(20):
            r = requests.get(site) # Store in r request data
            times.append(r.elapsed.microseconds / 1000)
      plt.plot(times, label = site)

      print("For ", site, " results are:")
      print("Minimum time: ", min(times), " ms")
      print("Maximun time: ", max(times), " ms")
      print("Average time: ", sum(times)/len(times), " ms", end="\n\n")
      m = max ([m, max(times)])

print("Massimo tra i massimi ", m)

# Plot stuff
plt.xlabel('ID request')
plt.ylabel('Time request (ms)')
plt.title('Multiple server requests')
plt.ylim([0, 1.1*m])
plt.legend(loc = 'upper right', fontsize = 10)
plt.show()