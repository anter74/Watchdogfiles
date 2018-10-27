import sys
import time
import logging
import watchdog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler,PatternMatchingEventHandler  ,FileDeletedEvent
class FileDeletedEvent(FileDeletedEvent):
    def dispatch(self, event):
        a = event.event_type
        print(a)
        if a == 'deleted':
            return(print("rip file"))
        if a == 'created':
            return(print("WOW! new files birth"))
        if a == 'modified':
            return(print("Hmmm,something changed ,ah"))

        
    def on_deleted(self,event):
        print(event.event_type)
        



       
        
        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileDeletedEvent(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

'''

class ScanFolder:
    'Class defining a scan folder'

    def __init__(self, path):
        self.path = path
        self.documents = dict() # key = document label   value = Document reference

        self.event_handler = watchdog.events.PatternMatchingEventHandler(patterns=["*.py", "*.xml", "*.html", "*.out", "*.js"],
                                    ignore_patterns=[],
                                    ignore_directories=True)
        self.event_handler.on_any_event = self.on_any_event
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=False)
        self.observer.start()

    def on_any_event(self, event):
        print(event.src_path, event.event_type)
        print("Complete ScanFolder() access")
        print("oh no programming is illegal in your country!!")

    def stop(self):
        self.observer.stop()
        self.observer.join()


path = 'testfolder/'

scan_folder = ScanFolder(path)

if __name__ == "__main__":

   try:
       while True:
          time.sleep(1)
        """Here, I'll act on my scan_folder object that lists the discovered files"""
   except KeyboardInterrupt:
       log.warning("Ouch !!! Keyboard interrupt received.")
       scan_folder.stop()
'''
       
        












