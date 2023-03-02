from tkinter import Canvas, NW, Tk
import tkinter
from PIL import Image, ImageTk

class Drawing():
    
    canvas: Canvas = None
    _bounds = None
    _rect_id = -1
    _image_id = None
    _tag = '_rectangle_'
    _image_tag = '_image_'
    _cur_image = None
    _root = None

    def __init__(self, canvas: Canvas = None ) -> None:
        self.canvas = canvas


    def update_rect_pos(self, ltx, lty, rbx, rby):
        lx = min(ltx, rbx)
        ly = min(lty, rby)

        rx = max(ltx, rbx)
        ry = max(lty, rby)

        self._bounds = (lx, ly, rx, ry)
        self._update_rect_on_canvas()

    def get_current_bound(self)->tuple:
        return self._bounds


    def clear_rect_from_canvas(self):
        if(self._rect_id != -1):
            self.canvas.delete(self._tag)
            self._rect_id = -1
            self._bounds = None
        else:
            return

    def _update_rect_on_canvas(self):
        if(self._rect_id == -1):
            # for windows os, stippling is working properly
            self.canvas.create_rectangle(self._bounds, tags=self._tag , fill="#FF5733", stipple='gray50')
            ## for mac os , stippling is not working
            # self.canvas.create_rectangle(self._bounds, tags=self._tag , fill="")
            self._rect_id = 1

        elif(self._bounds != None and self._rect_id > 0):
            self.canvas.coords(self._tag, self._bounds)
        
        else:
            return
    
    def get_canvas_size(self)-> tuple:
        return (self.canvas.winfo_width(), self.canvas.winfo_height())
    
    def draw_image(self, image: Image = None):
        if(image == None):
            return
        self._cur_image = ImageTk.PhotoImage(image)
        if self._image_id == None:
            self._image_id = self.canvas.create_image(0, 0, anchor=NW , image=self._cur_image, tags=self._image_tag)
        else:
            self.canvas.itemconfig(self._image_id,image=self._cur_image)
        


    # def _create_rectangle(x1, y1, x2, y2, **kwargs):
    #     if 'alpha' in kwargs:
    #         alpha = int(kwargs.pop('alpha') * 255)
    #         fill = kwargs.pop('fill')
    #         fill = root.winfo_rgb(fill) + (alpha,)
    #         image = Image.new('RGBA', (x2-x1, y2-y1), fill)
    #         images.append(ImageTk.PhotoImage(image))
    #         canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    #     canvas.create_rectangle(x1, y1, x2, y2, **kwargs)