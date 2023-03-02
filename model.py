from event_controller import EventController
from presenter import Presenter
from image_files_handler import FileHandler
from image_processor import ImageProcessor
from PIL import Image

class Model():

    event_controller: EventController = None
    file_handler: FileHandler = None
    image_processor : ImageProcessor = None


    def __init__(self, presenter: Presenter = None  ) -> None:
        self.event_controller = EventController(presenter=presenter)
        self.image_processor = ImageProcessor()


    def set_root_data_dir(self, root_data_dir):
        self.file_handler = FileHandler(root_dir_path=root_data_dir)


    def update_window_size(self, window_width=0, window_height=0):
        self.event_controller.set_drag_bounds(0, 0, window_width, window_height)
        self.image_processor.update_output_size(window_width, window_height)


    def saved_cropped_image(self, bound: tuple = None)-> bool:
        if(self.file_handler == None or bound == None):
            return False
        return self.image_processor.save_cropped_image(
            self.file_handler.get_current_image_file(),
            self.file_handler.get_output_image_dir(),
            bound
        )

    def load_previous_image(self) -> Image:
        if(self.file_handler == None):
            return None
        file = self.file_handler.get_prev_image_file()
        if(file == None):
            return None
        return self.image_processor.load_image(file)
    

    def load_next_image(self) -> Image:
        if(self.file_handler == None):
            return None
        file = self.file_handler.get_next_image_file()
        if(file == None):
            return None
        return self.image_processor.load_image(file)
    
    
    def refresh(self) -> Image:
        if(self.file_handler == None):
            return None
        file = self.file_handler.get_current_image_file()
        if(file == None):
            return None
        return self.image_processor.load_image(file)
