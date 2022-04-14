from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            for filetype in range(len(file_types)):
                if os.path.splitext(filename)[1] == file_types[filetype]:
                    src = folder_to_track + "/" + filename
                    new_destination = '/home/casper/Downloads/'+ file_loc[filetype] + "/" + filename
                    os.rename(src, new_destination)
        

file_types = ['.pdf', '.zip', '.xlsx' ]
file_loc = ['PDF', 'zip', 'Excel']
folder_to_track = '/home/casper/Downloads/'
event_handler = MyHandler() 
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True: 
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()