import json
import os
from os.path import normpath, basename
import re
from html_parser import HtmlParser
from file_helper import FileHelper

class Config:
    def __init__(self, inputDir, outputDir, extension, encoding):
        self.inputDir = inputDir
        self.outputDir = outputDir
        self.extension = extension
        self.encoding = encoding
        print('--- Loaded config ---')
        print('Input: ' + self.inputDir)
        print('Output: ' + self.outputDir)
        print('Extension: ' + self.extension)
        print('Encoding: ' + self.encoding)

def start(config):
    for (dirpath, dirnames, filenames) in os.walk(config.inputDir):
        for filename in filenames:
            if filename.endswith('.html'): 
                filePath = os.sep.join([dirpath, filename])
                html_file_content = FileHelper.read_input_file(filePath, config.encoding)
                parsed_html = HtmlParser().parse(html_file_content)
                output_file_path = os.sep.join([config.outputDir, basename(normpath(dirpath)), os.path.splitext(filename)[0] + config.extension])
                FileHelper.create_output_file(output_file_path, config.encoding, parsed_html)

def load_config():
    with open('config.json') as json_file:  
        data = json.load(json_file)
        config = Config(data['INPUT_DIR'], data['OUTPUT_DIR'], data['Extension'], data['Encoding'])

    return config

def main():
    config = load_config()
    start(config)
 
if __name__ == "__main__":
	main()