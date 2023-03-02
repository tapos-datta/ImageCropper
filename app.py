from tkinter import *
from tkinter import filedialog
from presenter import Presenter

from model import Model
from canvas_drawing import Drawing
from event_controller import EventController
from PIL import ImageTk, Image


class App(Presenter):

    _model : Model = None
    root : Tk
    root_width = 0
    root_height = 0
    _drawing = None
    _prev_btn = None
    _saved_btn = None
    _next_btn = None
    _clear_btn = None
    _status_label = None

    def __init__(self, tk_root, wWidth, wHeight, **argws) -> None:
        self.root = tk_root
        self.root_width = wWidth
        self.root_height = wHeight
        self._model = Model(self)
        self._create_view(tk_root)


    def _create_view(self, root):
        input_frame = LabelFrame(root, text="", width=self.root_width, height=8)
        input_frame.grid(row=0, column=0)
        
        # define input directory path
        dir_label = Label(input_frame, text="Dir-Path")
        dir_label.grid(row=0, column=0, padx=5, pady=5)

        input_dir_path = Label(input_frame, width=80, bg='#CFDFD3')
        input_dir_path.grid(row=0, column=1, columnspan=3, pady=5)

        # define load click
        load_btn = Button(input_frame, text="Load", width=8, command = lambda : self._open_dir_loader(input_frame, input_dir_path))
        load_btn.grid(row=0, column=5)

        #define Canvas
        image_canvas = Canvas(root, width=(self.root_width - 10), height=(self.root_height - 200), bg='#000000')
        self._drawing = Drawing(image_canvas)
        image_canvas.grid(row=1, column=0)
        

        operational_frame = LabelFrame(root, text="", width=self.root_width, height = 70)
        operational_frame.grid(row=2, column=0)
 
        prev_btn = Button(operational_frame, text="<<<", padx=7, pady=4, width=20)
        next_btn = Button(operational_frame, text=">>>", padx=7, pady=4, width=20)
        saved = Button(operational_frame, text="Crop & Saved", padx=8, pady=4,  width=20)
        clear = Button(operational_frame, text="Clear", padx=7, pady=4,  width=20)

        # add empty label in row 0 and column 0
        empty_row = Label(operational_frame, text="", height=1)
        empty_col_1 = Label(operational_frame, text="", width=1)
        empty_col_2 = Label(operational_frame, text="", width=1)
        
        prev_btn.grid(row=0, column=0)
        empty_col_1.grid(row=0, column=1)
        next_btn.grid(row=0, column=2)
        empty_row.grid(row=1, column=0)

        saved.grid(row=2, column=2)
        empty_col_2.grid(row=2, column=1)
        clear.grid(row=2, column=0)

        status_frame = LabelFrame(root, text="Status", width=350, height = 60, background="#FDD36A", padx=10, pady=10)
        status_frame.grid(row=3, column=0)

        status_label = Label(status_frame, text="Data not loaded", font=('Hack', 8), bg='#CFDFD3')
        status_label.grid(row=0, column=0)

        self._clear_btn = clear
        self._saved_btn = saved
        self._next_btn = next_btn
        self._prev_btn = prev_btn
        self._status_label = status_label


    def _open_dir_loader(self, root, input_dir_label):
        dirName = filedialog.askdirectory(initialdir="./demo_root", title = "select directory")
         
        canvas_size = self._drawing.get_canvas_size()

        self.root.bind('<Key>', self._model.event_controller.capture_key_events)
        self._drawing.canvas.bind('<Button-1>', self._model.event_controller.capture_left_click_action)
        self._drawing.canvas.bind('<Button-3>', self._model.event_controller.capture_right_click_action)
        self._drawing.canvas.bind('<B1-Motion>', self._model.event_controller.define_roi_area)
        self._clear_btn.configure(command=self._model.event_controller.capture_left_click_action)
        self._saved_btn.configure(command=self._model.event_controller.capture_right_click_action)
        self._next_btn.configure(command=self._model.event_controller.capture_load_next_action)
        self._prev_btn.configure(command=self._model.event_controller.capture_load_previous_action)
        self._model.update_window_size(canvas_size[0], canvas_size[1])

        if(dirName != "" ):
            input_dir_label.config(text = dirName)
            self._model.set_root_data_dir(dirName)
            self._status_label.config(text="Data loaded")
            self._drawing.draw_image(self._model.refresh())
            


    def update_roi(self, lx = 0, ly = 0, rx = 0, ry = 0):
       self._drawing.update_rect_pos(lx, ly, rx, ry)
       self._status_label.config(text="ROI selection")

    def on_clear(self):
        self._drawing.clear_rect_from_canvas()
        self._status_label.config(text="Cleared ROI")


    def on_save(self):
        bound = self._drawing.get_current_bound()
        status = self._model.saved_cropped_image(bound=bound)
        if status == True:
            self._status_label.config(text="Saved successfully")
        else:
            self._status_label.config(text="Saved failed")  



    def load_previous(self):
        self._clear_btn.invoke()
        self._drawing.draw_image(self._model.load_previous_image())


    def load_next(self):
        self._clear_btn.invoke()
        self._drawing.draw_image(self._model.load_next_image())


        