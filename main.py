

def some_background_function(queue):
  import os
  import datetime
  queue.put(f'"data", {datetime.datetime.now()}, subprocess PID: { os.getpid()}')

if __name__ == "__main__":
  import os
  from multiprocessing import Process, Queue, freeze_support
  freeze_support()
  #run Kivy app
  # runTouchApp(Builder.load_string(kvString))

  # you need to put as many kivy imports in if name is main guard so your subprocess does not import kivy stuff unnecessarily
  from kivy.lang import Builder
  from kivy.core.window import Window 
  from kivy.uix.button import Button
  from kivy.clock import Clock
  from kivy.app import App

  #this is to make the Kivy window always on top
  Window.always_on_top = True
  #set the window title
  Window.set_title('Welcome to Kivy School!')
  #kv language setting the main widget to be a button
  kvString = '''
#: import os os
CButton:
    text: "Original PID: " + str(os.getpid())
  '''

  class CButton(Button):

    # def on_button_press(self):
    def on_release(self):
      queue = Queue()
      # Create and start a new process
      # do not declare process as global, just refer to process using an OOP way.
      self.process11 = Process(target=some_background_function, args=(queue,))
      self.process11.start()
      # Use Clock to check for updates from the process
      # Clock.schedule_interval(lambda dt: self.check_queue(queue), 1)
      from functools import partial
      Clock.schedule_interval(partial(self.check_queue, queue), 1)
    
    def check_queue(self, queue, *args):
      queuedata = queue.get()
      #need to make sure queue is nonempty for next run else kivy will freeze with no error message
      import datetime, os
      queue.put(f'"data", {datetime.datetime.now()}, subprocess PID:  {os.getpid()}')
      print("queue data", queuedata)
      if queuedata != None:
        self.text = f'{queuedata}'

  class HWM(App):

    def build(self):
      return Builder.load_string(kvString)
    
    def on_request_close(self, *args, **kwargs):
      try:
        print("close the queue here or you will bug out", flush = True)
        app = App.get_running_app().root
        print("a existr?", app)
        # process11.terminate()
      except Exception as e:
        import traceback
        print("err", traceback.format_exc())
  HWM().run()
  HWM().on_request_close()
