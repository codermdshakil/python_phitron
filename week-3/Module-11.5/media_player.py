
from abc import ABC, abstractmethod

class Description:
    
    def __init__(self):
        self.__description
        

class Media(ABC):
    
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        super().__init__()
        
        
    @abstractmethod
    def play(self):
        pass


class Mesic(Media, Description):
    
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(description)
        