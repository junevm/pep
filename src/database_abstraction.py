from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect():
        pass

    @abstractmethod
    def disconnect():
        pass


    @abstractmethod
    def execute_query():
        pass

    @abstractmethod
    def fetch_data():
        pass


class MongoDatabase(Database):
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.connect = False
    
    def connect(self):
        self.connect = True    
        return 'connected'

    def disconnect(self):
        self.connect = False
        return 'disconnected'

    def execute_query(self):
        if not self.connect:
            return "Error not connected"
        
        return 'query executed'

    def fetch_data(self):
        if not self.connect:
            return "Error not connected"
        
        return [1,2]