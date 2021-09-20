import abc
from rgbmatrix import FrameCanvas

class IPanel(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_config') and
                callable(subclass.load_config) and 
                hasattr(subclass, 'set_canvas') and
                callable(subclass.set_canvas) and
                hasattr(subclass, 'update') and
                callable(subclass.update) and
                hasattr(subclass, 'draw') and
                callable(subclass.draw) or
                NotImplemented)

    @abc.abstractmethod
    def load_config(self, path: str, file_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def set_canvas(self, canvas: FrameCanvas):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError