import multiprocessing
import time

manager = multiprocessing.Manager()
final_list = manager.list()


def add():
	import tkinter
	top= tkinter.Tk()
	def cbp():
		print("caught a close click")
		final_list.clear()
		final_list.append(1)
	def obp():
		print("caught an open click")
		final_list.clear()
		final_list.append(2)
	c=tkinter.Button(top,text="Close graph",command=cbp)
	c.pack()
	o=tkinter.Button(top,text="open graph",command=obp)
	o.pack()
	top.mainloop()

def sud():
	import random
    from time import sleep
    from oscilloscope import Osc
    
    # adjust window_sec and intensity to improve visibility
    osc = Osc(fps=1)
    @osc.signal
    def increasing_signal(state):
        delta = 1
        while True:
            state.draw(random.randint(-delta, delta))
            delta += 5
            sleep(0.01)
	flag=0
	while(True):
		if(len(final_list)>0):
			if(final_list[-1]==1):
				osc.stop()
				flag=0
				final_list.clear()
			if(flag==0 and len(final_list)>0):
				if(final_list[-1]==2):
					osc.start()
					flag=1
					final_list.clear()

if __name__ =='__main__':
	p1 = multiprocessing.Process(name='p1',target=add)
	p2 = multiprocessing.Process(name='p1',target=sud)
	p1.start()
	p2.start()
	p1.join()
	p2.join()