#This demonstrates synchronous threading whereby a thread completes processing before 
#Another one takes over
#Feels like normal sequential processing only that the program doesn't stop and wait

import threading
import time


class myThread(threading.Thread):
	def __init__(self, threadID, name, delay, result):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.delay=delay
		self.result=result
	def run(self):
		print ("\nStarting" +self.name)
		#Now get the lock to synchronize threads
		threadLock.acquire()
		a = print_time(self.name, self.delay, 3, self.result, self.threadID)
		#Free lock to release next thread
		threadLock.release()


def print_time(threadName, delay, counter, result, threadID):

	while counter:
		counter -= 1
		time.sleep(delay)
		print ("%s: %s" %(threadName, time.ctime(time.time())))
	result.append(4) 
        

#The native function?method is replaced here and used in the class that way
#How's that?
threadLock=threading.Lock()

threads=[]
result = []

#Now create new threads
Thread1=myThread(0, "Thread-1", 1, result)
Thread2=myThread(1, "Thread-2", 2, result)

#Start the new threads
Thread1.start()
Thread2.start()

#Add the threads to thread list
threads.append(Thread1)
threads.append(Thread2)

#Wait for all threads to complete
#Failure to do this would make the rest of the program continue to execute
for t in threads:
	t.join()

print(result)


print("Exiting Main Thread")