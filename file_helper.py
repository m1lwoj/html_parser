import os
from annotations import *
import uuid

class FileHelper():
    @staticmethod
    @safe_run
    def  create_output_file(outputFilePath, config, processingDir, processingFilePath, mergeFilePath):
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
    def read_input_file(path, encoding):
        print('--- Reading file ---')
        print(path)
        with open(path, 'r', encoding=encoding) as file:  
            fileContent = file.read()

        print('--- End ---\n')
        return fileContent

