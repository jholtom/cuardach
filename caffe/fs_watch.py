import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

def all_files(directory):
    for path, dirs, files in os.walk(directory):
        for f in files:
            yield os.path.join(path, f)

def is_image(f):
    if f.endswith('.JPG'):
	return True
    if f.endswith('.jpg'):
	return True
    if f.endswith('.JPEG'):
	return True
    if f.endswith('.jpeg'):
	return True
    if f.endswith('.png'):
	return True
    if f.endswith('.PNG'):
	return True
    else:
	return False

def find_images():
    image_files = [f for f in all_files(your_directory) if is_image(f)]
    return image_files

def watch_for_changes(path): # This method needs to be daemonized
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
