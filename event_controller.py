from presenter import Presenter
from tkinter import Event

class EventController():

    _drag_bound = None
    _inital_pos = None
    presenter = None

    def __init__(self, presenter: Presenter = None) -> None:
        self.presenter = presenter


    def set_drag_bounds(self, x = 0 , y = 0, width = 0, height = 0):
        if(width <= 0 or height <= 0
            or x >= width or y >= height 
            or x < 0 or y < 0):
            return
        self._drag_bound = (x, y, width, height)


    def capture_key_events(self, event: Event = None):
        if(event == None):
            return
        if event.keysym == 'Left' :
            self.capture_load_previous_action()
        elif event.keysym == 'Right' :
            self.capture_load_next_action()
    

    def capture_load_previous_action(self):
        self.presenter.load_previous()

    
    def capture_load_next_action(self):
        self.presenter.load_next()
    

    def capture_left_click_action(self, event:Event = None):
        self._inital_pos = None
        self.presenter.on_clear()

    
    def capture_right_click_action(self, event:Event = None):
        self.presenter.on_save()


    def define_roi_area(self, event: Event = None):
        if(self._inital_pos == None):
            self._inital_pos = (event.x, event.y)
        
        self.presenter.update_roi(self._inital_pos[0],
                                  self._inital_pos[1],
                                  max(min(event.x,self._drag_bound[2]), self._drag_bound[0]),
                                  max(min(event.y,self._drag_bound[3]), self._drag_bound[1]))
        

