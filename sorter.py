from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler  
 
import os 
import json  
import time   

class myfilehandler(FileSystemEventHandler):   
    def on_modified(self,event):   
        for filename in os.listdir(mother_folder):
            src = mother_folder + "/" + filename  
            new_sorted= folder_dest + "/" + filename  
            os.rename(src , new_sorted)  

# mother_folder -> folder under observation  
# folder_dest -> Folder to which files will be copied
mother_folder = "/home/pimple/Documents/COding/python_file_sorter"     
folder_dest = "/home/pimple/Documents/COding/read"  
event_handler = myfilehandler()   
observer = Observer()   
observer.schedule(event_handler , mother_folder,recursive = True)  
observer.start()  

try:  
    while True:  
        time.sleep(10)   
except KeyboardInterrupt:  
    observer.stop()  
observer.join()
