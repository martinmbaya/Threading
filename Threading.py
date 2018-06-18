import threading
import time

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
		print ("\nStarting" + self.name)
		print_time(self.name, self.counter, 5)
		print ("Exiting" + self.name)

def print_time(threadName, delay, counter):
	while counter:
		#I wonder why they put this below here?
		#There's no effect of not putting this here
		if exitFlag:
			thread.exit()
		time.sleep(delay)
		print ("%s: %s" %(threadName, time.ctime(time.time())))
		counter -=1

#Create new threads here by invoking the class myThread and passing the parameters required
thread1=myThread(1, "Thread-1", 1)
thread2=myThread(2, "Thread-2", 2)

#Start the new threads. the start method invokes the run method in the class
thread1.start()
thread2.start()

print ("\nExiting Main Thread")