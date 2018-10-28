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

