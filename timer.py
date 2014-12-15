import threading
import time

tLock = threading.Lock()

def timer(name,delay,repeat):
	print "Timer: "+ name + " started!"
	tLock.acquire()
	print 'Lock acquired!'
	while repeat > 0:
		time.sleep(delay)
		print name + ":"+ str(time.ctime(time.time()))
		repeat -= 1
	print 'releasing lock...'
	tLock.release()
	print "Timer: "+ name+ " completed!"


def main():
	t1 = threading.Thread(target=timer,args=("Timer 1",1,5))
	t2 = threading.Thread(target=timer,args=("Timer 2",2,5))

	t1.start()
	t2.start()

	print "Main Complete!"

if __name__ == '__main__':
	main()