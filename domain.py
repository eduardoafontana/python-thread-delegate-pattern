import time
import sys

class TrainerService:

    def execute(self, input_value, callback_method):
        print('Executing code of TrainerService.')
        print(input_value)

        for i in range(100):
            data = 'callback data i: ' + str(i)
            callback_method(data)

            time.sleep(0.4)


