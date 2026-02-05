class camera:
    def __init__(self,camera_quality):
        self.camera_quality = camera_quality
    def display_camera_details(self):
        print("The camera qualit is",self.camera_quality)
class MusicPlayer:
    def __init__(self,sound_quality):
        self.sound_quality = sound_quality
    def display_sound_details(self):
        print("The sound qualit is",self.sound_quality)

class SmartPhone(camera,MusicPlayer):
    def __init__(self,camera_quality,sound_quality,brand):
        camera.__init__(self,camera_quality)
        MusicPlayer.__init__(self,sound_quality)
        self.brand = brand
    def display_brand_details(self):
        print("The brand details are",self.brand)
        
f23=SmartPhone("64px rear and 32px front","good","oppo")
f23.display_camera_details()
f23.display_sound_details()
f23.display_brand_details()