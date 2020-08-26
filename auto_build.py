import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent
from watchdog.observers import Observer
from pathlib import PurePath
import subprocess
import signal


class KotlinFileSystemEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        src_path = event.src_path
        pp = PurePath(src_path)
        if pp.suffix == '.kt':
            subprocess.run(['./gradlew', 'assemble'])

exit_flag = False

def handle_exit(sig, frame):
    global exit_flag
    exit_flag = True


signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

event_handler = KotlinFileSystemEventHandler()
observer = Observer()
observer.schedule(event_handler, './', recursive=True)
observer.start()
while exit_flag == False:
    time.sleep(1)

observer.stop()
observer.join()
