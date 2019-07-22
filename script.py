import json
import os
from os.path import normpath, basename
import re
from html_parser import HtmlParser
from file_helper import FileHelper

class Config:
    def __init__(self, inputDir, outputDir, mergeDir, extension, encoding, publisher, outStacker, discType, label):
        self.inputDir = inputDir
        self.outputDir = outputDir
        self.mergeDir = mergeDir
        self.extension = extension
        self.encoding = encoding
        self.publisher = publisher
        self.outStacker = outStacker
        self.discType = discType
        self.label = label

        print('--- Loaded config ---')
        print('Input: ' + self.inputDir)
        print('Output: ' + self.outputDir)
        print('Merge: ' + self.mergeDir)
        print('Extension: ' + self.extension)
        print('Encoding: ' + self.encoding)
        print('---------------------------')
        print('PUBLISHER: ' + self.publisher)
        print('OUT_STACKER: ' + self.outStacker)
        print('DISC_TYPE: ' + self.discType)
        print('LABEL: ' + self.label)
        print('---------------------------')

def start(config):
    for (dirpath, dirnames, filenames) in os.walk(config.inputDir):
        if '.processed' in filenames:
            continue

        for filename in filenames:
            if filename.endswith('.html'): 
                filePath = os.sep.join([dirpath, filename])
                html_file_content = FileHelper.read_input_file(filePath, config.encoding)
                parsed_html = HtmlParser().parse(html_file_content)
                merge_file_path = os.sep.join([config.mergeDir, 'MERGE_' + basename(normpath(dirpath)) + config.extension])
                FileHelper.create_merge_file(merge_file_path, config.encoding, parsed_html)
                output_file_path = os.sep.join([config.outputDir, 'JOB_' + basename(normpath(dirpath)) + '.inp'])
                FileHelper.create_output_file(output_file_path, config, basename(normpath(dirpath)), dirpath, merge_file_path)
                
                FileHelper.create_processed_file(dirpath)

def load_config():
    with open('config.json') as json_file:  
        data = json.load(json_file)
        config = Config(
            data['INPUT_DIR'], 
            data['OUTPUT_DIR'],
            data['MERGE_DIR'], 
            data['Extension'],
            data['Encoding'],
            data['PUBLISHER'],
            data['OUT_STACKER'],
            data['DISC_TYPE'],
            data['LABEL'])

    return config

def main():
    config = load_config()
    start(config)
 
if __name__ == "__main__":
	main()