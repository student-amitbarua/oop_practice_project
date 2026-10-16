from abc import ABC ,  @abstractmethod

class Description:
    def __init__(self, description):
        self.__descritption = description

    def get_description(self):
        return self.__descritption


class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        pass


class Music(Media, Description):
    def __init__(self, title, duration, description ):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)


    def play(self):
        print(f"playing Music: {self.title} ")
    def info(self):
        print(f"Title: {self.title} duration: {self.duration} description: {self.get_description()}")



class Video(Media, Description):
    def __init__(self, title, duration, description ):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)


    def play(self):
        print(f"playing Video: {self.title} ")
    def info(self):
     print(f"Title: {self.title} duration: {self.duration} description: {self.get_description()}")

class AudioBook(Media, Description):
    def __init__(self, title, duration, description ):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)


    def play(self):
        print(f"playing AudioBook: {self.title}")
 
    def info(self):
        print(f"Title: {self.title} duration: {self.duration} description: {self.get_description()}")


class Library:
    def __init__(self):
        self. __media_items = []
        self.__media_by_genre = {}
        self.__genre = " "


    def get_method_items(self):
        return self.__media_items
    
    def get_media_by_genre(self):
        self.__media_by_genre

    def add_media(self, media):
        pass

    def add_media(self, media):
        if isinstance(media, Music):
            self.__genre = "Music"
        if isinstance(self,Video):
            self.__genre = "Video"
        if isinstance(self, AudioBook):
            self.__genre = "AudioBook"

        self.__media_items.append(media)
        
        if self.__genre in self.__media_by_genre:
            self.__media_by_genre[self.__genre].append(media)
        else:
            self.__media_by_genre[self.__genre] = [media,]

class User(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def play_media(self):
        pass 

class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)

    def play_media(self, library):
        for media in library.get_media_items():
            media.play()

class PremimumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = " "

    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def get_favourite_genre(self, genre):
        return self.__favourite_genre

    def play_media(self, library):
        if self.__favourite_genre in library.get_media_by_genre():
          for media in library.get_media_by_genre()[self.__favourite_genre]:
            media.play()



library = Library()
music1 = Music('Music Track 1', '3.45', 'Author: Phitron')
music2 = Music('Music Track 2', '5.35', 'Author: Phitron')
video = Video('Video Track 2', '5.35', 'Author: T-series')
audio1 = AudioBook('Audio track', '3.87', 'Author: Programming Hero')

library.add_media(music1)
library.add_media(music2)
library.add_media(video)
library.add_media(audio1)

free_user = FreeUser('amit')

premimum_user = PremimumUser('sakib')
free_user .play_media(library)







