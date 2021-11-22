from domain import TrainerService
import threading
import time

class FooClass:

    def callback_handler(self, callback_object):
        print(callback_object)

object_input = 'input data'
foo_class = FooClass()

trainer_service = TrainerService()

worker = threading.Thread(name="trainer", target=trainer_service.execute, args=(object_input, foo_class.callback_handler))
worker.setDaemon(True)
worker.start()
worker.join()

#https://ikriv.com/blog/?p=4790