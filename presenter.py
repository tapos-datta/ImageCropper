from abc import ABC, abstractmethod

class Presenter(ABC) :
    @abstractmethod
    def update_roi(self, x = 0, y = 0, width = 0, height = 0):
        pass

    @abstractmethod
    def on_clear(self):
        pass

    @abstractmethod
    def on_save(self):
        pass

    @abstractmethod
    def load_previous(self):
        pass

    @abstractmethod
    def load_next(self):
        pass




