
from abc import ABC, abstractmethod

class Description:
    
    def __init__(self, description):
        self.__description = description
        
    def get_description(self):
        return self.__description
        

class Media(ABC):
    
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
        
    @abstractmethod
    def play(self):
        pass


class Music(Media, Description):
    
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self,description)
    
    def play(self):
        print(f"Playing Music title : {self.title}")
    
    # show details of music
    def info(self):
        print(f"Title of music : {self.title}")
        print(f"Duration of music : {self.duration}")
        print(f"Description of music : {self.get_description()}")
    
        
        
music1 = Music("Music1", "3.45", "This is a music and it's duration is 3.45 min")
# music1.play()
# music1.get_description()
music1.info()

