import os
from annotations import *

class FileHelper():
    @staticmethod
    @safe_run
    def create_output_file(path, encoding, model):
        print('--- Saving to file ---')
        print(path)

        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
                
        with open(path, 'w', encoding=encoding) as f:
            for key, value in model.items():
                f.write(key + '=' + value + '\n')
        
        print('--- End ---\n')

    @staticmethod
    @safe_run
    def read_input_file(path, encoding):
        print('--- Reading file ---')
        print(path)
        with open(path, 'r', encoding=encoding) as file:  
            fileContent = file.read()

        print('--- End ---\n')
        return fileContent

