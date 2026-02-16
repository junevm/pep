from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self,filename):
        pass

    @abstractmethod
    def write(self,filename,data):
        pass
    
    @abstractmethod
    def get_format():
        pass
    

class TextFileHandler(FileHandler):
    def __init__(self):
        pass
        
    def read(self,filename):
        with open(filename, 'r') as f:
            return f.read()

    def write(self,filename, data):
        with open(filename, 'w') as f:
            f.write(data)

    def get_format(self):
        return "Text"

   

class JSONFileHandler(FileHandler):
    def __init__(self):
        pass
        
    def read(self,filename):
        with open(filename, 'r') as f:
            
            return f.read()

    def write(self,filename, data):
        print (f"{filename} written as JSON")

    def get_format():
        print("JSON")

   

class XMLFileHandler(FileHandler):
    def __init__(self):
        pass
        
    def read(self,filename):
        pass

    def write(self,filename, data):
        pass

    def get_format():
        pass

