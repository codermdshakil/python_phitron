
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
    

# Create Library
class Library():
    
    def __init__(self, library_name):
        self.library_name = library_name
        self.__media_items = []
        self.__media_by_genre = []
        
    
    # get media items
    def get_media_items(self):
        return self.__media_items
    
    # get media by genre
    def get_media_by_genre(self):
        return self.__media_by_genre
    
    def add_media(self, media):
        self.__media_items.append(media)
        
        


# Create Library using Library class
lb = Library("Phitron LB")
print(lb.library_name)




    
music1 = Music("Music 1", "3.45 Min", "This is a music and it's duration is 3.45 min")
music2 = Music("Music 2", "6.45 Min", "This is a music and it's duration is 6.45 min")
video1 = Video("Video 1", "4.54 Min", "This is a video of some songs")
video2 = Video("Video 2", "5.16 Min", "This is a video of some songs")
audiobook1 = AudioBook("Audio Book 1", "10.56 Min", "This is a description of audio book of Atomic Habit")
audiobook2 = AudioBook("Audio Book 2", "9.52 Min", "This is a description of audio book of Atomic Habit")
# music1.play()
# music1.get_description()
# music1.info()
# video1.info()
# audiobook1.info()

# add media items
lb.add_media(music1)
lb.add_media(music2)
lb.add_media(video1)
lb.add_media(video2)
lb.add_media(audiobook1)
lb.add_media(audiobook2)

# print(len(lb.get_media_items()))




