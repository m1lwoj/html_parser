import os
from annotations import *
import uuid

class FileHelper():
    @staticmethod
    @safe_run
    def create_output_file(outputFilePath, config, processingDir, processingFilePath, mergeFilePath):
        print('--- Saving output file ---')
        print(outputFilePath)

        if not os.path.exists(os.path.dirname(config.mergeDir)):
            try:
                os.makedirs(os.path.dirname(config.mergeDir))
            except OSError as exc: 
                if exc.errno != errno.EEXIST:
                    raise
                
        model = dict()
        model['JOB_ID'] = processingDir + str(uuid.uuid4())
        model['PUBLISHER'] = config.publisher
        model['COPIES'] = str(1)
        model['OUT_STACKER'] = config.outStacker
        model['DISC_TYPE'] = config.discType
        model['DATA'] = processingFilePath
        model['VOLUME_LABEL'] =  processingDir + str(uuid.uuid4())
        model['LABEL'] = config.label
        model['REPLACE_FIELD'] = mergeFilePath

        with open(outputFilePath, 'w', encoding=config.encoding) as f:
            for key, value in model.items():
                f.write(key + '=' + value + '\n')
        
        print('--- End ---\n')

    @staticmethod
    @safe_run
    def create_merge_file(path, encoding, model):
        print('--- Saving merge file ---')
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
    def create_processed_file(path):
        print('--- Saving processed file ---')
        print(os.sep.join([path, '.processed']))

        open(os.sep.join([path, '.processed']), 'w').close()
        
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

    @staticmethod
    def gothroughdirectory(some_dir, level=1):
        some_dir = some_dir.rstrip(os.path.sep)
        assert os.path.isdir(some_dir)
        num_sep = some_dir.count(os.path.sep)
        for root, dirs, files in os.walk(some_dir):
            yield root, dirs, files
            num_sep_this = root.count(os.path.sep)
            if num_sep + level <= num_sep_this:
                del dirs[:]