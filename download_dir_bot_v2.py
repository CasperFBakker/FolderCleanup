import os
import json
import time

def run():
    for filename in os.listdir(folder_to_track):
        for filetype, loc in zip(file_types, file_loc):
            if os.path.splitext(filename)[1] == filetype:
                src = os.path.join(folder_to_track, filename)
                if loc == 'PowerPoint' or loc =='Word':
                    os.system(f"unoconv --format=pdf -o {os.path.join(folder_to_track, loc, 'pdf', filename)} {src}")
                new_destination = os.path.join(folder_to_track, loc ,filename)
                os.rename(src, new_destination)

        
file_types = ['.pdf', '.zip', '.xlsx', '.pptm', '.docx' ]
file_loc = ['PDF', 'zip', 'Excel', 'PowerPoint', 'Word']
folder_to_track = '/home/casper/Downloads/'

run()