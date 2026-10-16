from abc import ABC, abstractmethod

class Description:
    def __init__(self, description):
        self.__description = description  # Fixed typo

    def get_description(self):
        return self.__description


class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod  # Fixed abstract method decorator
    def play(self):
        pass


class Music(Media, Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Playing Music: {self.title}")

    def info(self):
        print(f"Title: {self.title} | Duration: {self.duration} | Description: {self.get_description()}")


class Video(Media, Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Playing Video: {self.title}")

    def info(self):
        print(f"Title: {self.title} | Duration: {self.duration} | Description: {self.get_description()}")


class AudioBook(Media, Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Playing AudioBook: {self.title}")

    def info(self):
        print(f"Title: {self.title} | Duration: {self.duration} | Description: {self.get_description()}")


class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}

    def get_media_items(self):
        return self.__media_items  # Fixed method name

    def get_media_by_genre(self):
        return self.__media_by_genre  # Fixed missing return statement

    def add_media(self, media):
        if isinstance(media, Music):
            genre = "Music"
        elif isinstance(media, Video):
            genre = "Video"
        elif isinstance(media, AudioBook):
            genre = "AudioBook"
        else:
            return  # Ignore unknown media types

        self.__media_items.append(media)

        if genre in self.__media_by_genre:
            self.__media_by_genre[genre].append(media)
        else:
            self.__media_by_genre[genre] = [media]


class User(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def play_media(self, library):
        pass


class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)

    def play_media(self, library):
        for media in library.get_media_items():
            media.play()


class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = ""

    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def get_favourite_genre(self):
        return self.__favourite_genre  # Fixed method signature

    def play_media(self, library):
        if self.__favourite_genre in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.__favourite_genre]:
                media.play()


# Usage
library = Library()
music1 = Music("Music Track 1", "3.45", "Author: Phitron")
music2 = Music("Music Track 2", "5.35", "Author: Phitron")
video = Video("Video Track 2", "5.35", "Author: T-series")
audio1 = AudioBook("Audio track", "3.87", "Author: Programming Hero")

library.add_media(music1)
library.add_media(music2)
library.add_media(video)
library.add_media(audio1)

free_user = FreeUser("amit")
premium_user = PremiumUser("sakib")

free_user.play_media(library)
