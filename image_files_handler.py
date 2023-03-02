import os

class FileHandler():
    
    image_files = []
    root_dir = ""
    imgs_dir = ""
    labs_dir = ""   
    output_img_dir = ""
    output_lab_dir = ""
    current_pos = 0
    total_files = 0

    def __init__(self, root_dir_path = None) -> None:
        self.root_dir = root_dir_path
        self.imgs_dir = os.path.join(root_dir_path + os.sep, "images" + os.sep)
        self.labs_dir = os.path.join(root_dir_path +  os.sep, "labels" + os.sep)
        self.output_img_dir = os.path.join(root_dir_path + os.sep, "output" + os.sep, "images" + os.sep )
        self.output_lab_dir = os.path.join(root_dir_path + os.sep, "output" + os.sep, "labels" + os.sep )
        self.current_pos = 0
        self._fetch_images(self.imgs_dir)

    
    def _fetch_images(self, img_dir = ""):
        for (root, dirs, files) in os.walk(img_dir, topdown=False):
            self.image_files = files
            self.total_files = len(files)
            break
    
    def get_current_image_file(self)-> tuple:
        if(self.image_files == None):
            return None
        return (
                self._get_src_path(self.imgs_dir, self.image_files[self.current_pos]),
                self._get_src_path(self.labs_dir, self.image_files[self.current_pos])
            )
    

    def get_next_image_file(self) -> tuple:
        if(self.image_files == None):
            return None
        if(self.total_files > 0 and self.current_pos + 1 < self.total_files):
            self.current_pos += 1
            return (
                self._get_src_path(self.imgs_dir, self.image_files[self.current_pos]),
                self._get_src_path(self.labs_dir, self.image_files[self.current_pos])
            )
        else:
            return None
    
    def get_prev_image_file(self) -> tuple:
        if(self.image_files == None):
            return None
        if(self.total_files > 0 and self.current_pos - 1 >= 0):
            self.current_pos -= 1
            return (
                self._get_src_path(self.imgs_dir, self.image_files[self.current_pos]),
                self._get_src_path(self.labs_dir, self.image_files[self.current_pos])
            )
        else:
            return None
        
    def _get_src_path(self, src_dir, file_name) -> str:
            f_name = os.path.splitext(file_name)
            ext = f_name[-1]
            f_name = f_name[0]
            full_path = os.path.join(src_dir, f_name + ext)
            if os.path.exists(full_path):
                return full_path
            else:
                return os.path.join(src_dir, f_name + '.png')
        
    def get_output_image_dir(self) -> tuple:
        if not os.path.exists(self.output_img_dir):
            os.makedirs(self.output_img_dir)
        if not os.path.exists(self.output_lab_dir):
            os.makedirs(self.output_lab_dir)
        return (self.output_img_dir, self.output_lab_dir)