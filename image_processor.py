import cv2
import os
import numpy as np
from PIL import Image

class ImageProcessor():

    _out_width = 0
    _out_height = 0

    def __init__(self, out_width=0, out_height=0) -> None:
        self._out_width = out_width
        self._out_height = out_height


    def update_output_size(self, out_width=0, out_height=0):
        self._out_width = out_width
        self._out_height = out_height


    def load_image(self, image_path: tuple) -> Image: 
        img = self._load_image(image_path[0], (self._out_width, self._out_height))
        lab = self._load_image(image_path[1], (self._out_width, self._out_height))
        if img.any() is False or lab.any() is False:
            return None
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        lab = cv2.cvtColor(lab, cv2.COLOR_BGR2RGB)
        lab = cv2.cvtColor(lab, cv2.COLOR_RGB2GRAY)
        blend = img.copy()
        blend[np.where(lab > 0)] = [206,55,230] 
        
        cv2.addWeighted(img, 0.5, blend, 0.5, 0.0, img);
        im_pil = Image.fromarray(img)
        return im_pil
    

    def _load_image(self, src_path, dest_size)-> cv2.Mat:
        img  = cv2.imread(src_path, cv2.IMREAD_UNCHANGED)
        if img.any() is False:
            return None
        if(dest_size[0] <= 0 or dest_size[1] <= 0):
            return img
        else:
            w = img.shape[1]
            h = img.shape[0]
            img = cv2.resize(img,
                        dest_size,
                        w * 1.0 / dest_size[0], h * 1.0 / dest_size[1],
                        cv2.INTER_LINEAR
                    )
        return img


    def _write_image(self, image,  src_dir, file_name, extension):
        out_path = os.path.join(src_dir, file_name + extension)
        cv2.imwrite(out_path, image)


    def save_cropped_image(self, src_path: tuple = None , output_dir: tuple = None, bound: tuple = None) -> bool:
        if src_path == None or output_dir == None or bound == None:
            return False
        _, tail = os.path.split(src_path[0])
        file_name = os.path.splitext(tail)
        extension = file_name[-1]
        file_name = file_name[0]

        img  = self._load_image(src_path[0], (-1, -1))
        lab  = self._load_image(src_path[1], (-1, -1))

        if img.any() is False or lab.any() is False:
            return None
 
        x1 = min((bound[0], bound[2]))
        x2 = max((bound[0], bound[2]))
        y1 = min((bound[1], bound[3]))
        y2 = max((bound[1], bound[3]))
        
        w = img.shape[1]
        h = img.shape[0]
        scalex = w * 1.0 / self._out_width
        scaley = h * 1.0 / self._out_height

        x1 = int(x1 * scalex)
        x2 = int(x2 * scalex)  
        y1 = int(y1 * scaley)
        y2 = int(y2 * scaley)
        
        if (x2 - x1) * (y2 - y1) <= (150 * 150):
            return False

        img = img[y1:y2, x1:x2]
        lab = lab[y1:y2, x1:x2]
        prefix = "_"+ str(x1) + "_"+ str(y1) + "_"+ str(x2) + "_"+ str(y2) + "_"
        
        self._write_image(img, output_dir[0], prefix + file_name, extension)
        self._write_image(lab, output_dir[1], prefix + file_name, extension)

        return True

    


