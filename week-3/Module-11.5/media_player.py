
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

# Create Music Object
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
        print("\n")



# Create Video Object 
class Video(Media, Description):
    
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self,description)
    
    def play(self):
        print(f"Playing Video title : {self.title}")
    
    # show details of Video
    def info(self):
        print(f"Title of Video : {self.title}")
        print(f"Duration of Video : {self.duration}")
        print(f"Description of Video : {self.get_description()}")
        print("\n")
        
        
        
# Create AudioBook Object
class AudioBook(Media, Description):
    
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self,description)
    
    def play(self):
        print(f"Playing AudioBook title : {self.title}")
    
    # show details of AudioBook
    def info(self):
        print(f"Title of AudioBook : {self.title}")
        print(f"Duration of AudioBook : {self.duration}")
        print(f"Description of AudioBook : {self.get_description()}")
        print("\n")
    


    
        
music1 = Music("Music1", "3.45 Min", "This is a music and it's duration is 3.45 min")
video1 = Video("Video1", "4.55 Min", "This is a video of some songs")
audiobook1 = AudioBook("Audio Book 1", "10.56 Min", "This is a description of audio book of Atomic Habit")
# music1.play()
# music1.get_description()
music1.info()
video1.info()
audiobook1.info()


