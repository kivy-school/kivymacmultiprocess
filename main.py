from kivy.clock import Clock
from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.core.window import Window 
from kivy.uix.button import Button

#this is to make the Kivy window always on top
Window.always_on_top = True
#set the window title
Window.set_title('Welcome to Kivy School!')

#kv language setting the main widget to be a button
kvString = '''
CButton:
    text: "Hello world!"
    on_release: self.on_button_press()
'''

def some_background_function(queue):
  import os
  queue.put("data")
  print("os pid", os.getpid(), flush = True)
class CButton(Button):

  def on_button_press(self):
    queue = Queue()
    # Create and start a new process
    process = Process(target=some_background_function, args=(queue,))
    process.start()
    # Use Clock to check for updates from the process
    Clock.schedule_interval(lambda dt: self.check_queue(queue), 1)
    # from functools import partial
    # Clock.schedule_interval(partial (self.check_queue, queue), 0.1)
    # Clock.schedule_interval(partial(self.check_queue, queue), 0.1)
  
  def check_queue(self, queue):
    print("queue data", queue)


if __name__ == "__main__":
  import os
  from multiprocessing import Process, Queue, freeze_support
  freeze_support()
  #run Kivy app
  runTouchApp(Builder.load_string(kvString))

