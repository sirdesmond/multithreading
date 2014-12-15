import threading
import time
import math

class AsyncWrite(threading.Thread):
	def __init__(self,text,output):
		threading.Thread.__init__(self)
		self.text = text
		self.output = output


	def run(self):
		with open(self.output, "a") as f:
			f.write(self.text + "\n")
			time.sleep(5)
			print 'Done storing string in file '+ self.output

def main():
	message = raw_input("Enter a string to store: ")

	background = AsyncWrite(message,'output.txt')

	background.start()

	print 'Program execution can continue...'

	print math.ceil(13/4)

	background.join()

	print "I waited for background task to finish running"

if __name__ == '__main__':
	main()