from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler  
 
import os 
import json  


class myfilehandler(FileSystemEventHandler):    
    def on_modified(self,event):    
        onlyfiles = [f for f in os.listdir(mother_folder) ]    
        listOfFiles=[]     
        for file in onlyfiles: 
            if len(file.split("."))>1:
                historicalSize = -1
                while (historicalSize != os.path.getsize(mother_folder + "/" + file)):
                    historicalSize = os.path.getsize((mother_folder + "/" + file))
                    print(".....loading......",historicalSize)
                    time.sleep(1)
                listOfFiles.append(file) 

        for filename in listOfFiles:
            src = mother_folder + "/" + filename    
            new_sorted= folder_dest + "/" + filename  
            os.rename(src , new_sorted)  

# mother_folder -> folder under observation  , path to the folder
# folder_dest -> Folder to which files will be copied
mother_folder = "/home/pimple/Documents/sorter"     
folder_dest = "/home/pimple/Documents/read"  
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
