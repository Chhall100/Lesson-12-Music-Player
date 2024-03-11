import os
os.environ["KIVY_VIDEO"]="ffpylayer"

from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.video import Video
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDIcon
from plyer import filechooser

from mutagen.mp4 import MP4

Window.size(600,340)

class IconButton(ButtonBehavior, MDIcon):
    pass

class Videos(Video):
    def __init__(self, **kwargs):
        super(Videos, self).__init__(**kwargs)
        self.bind(position=MDApp.get_running_app().change_slider_value)
        
        def _on_eos(self, *largs):
            MDApp.get_running_app().root.ids.play_pause_button.icon='replay' 
            if MDApp.get_running_app().hide is True:
                MDApp.get_running_app().unhide_controls()
                
                def on_touch_down(self, touch):
                    if self.collide_point(*touch.pos):
                        if MDApp.get_running_app().hide is True:
                              MDApp.get_running_app().unhide_controls()
                        else:
                            if touch.pos[1]>60:
                                MDApp.get_running_app().hide_controls()
                                
                                
                                class CustomVideoPlayer(MDApp): 
                                 duration=0
                                time_duration='0:00'
                                current_time='0:00'
                                hide=False
                                
                            def on_start(self):
                                self.duration=MP4(self.root.ids.video.source).info.length
                                minutes=minutes*60
                                seconds=minutes*60
                                self.time_duration=str(round(minutes))+':'
                                +str(round(seconds)).zfill(2)
                                self.root.ids.time_duration.text=f'{self.current_time}/{self.time_duration}'
                                
                                def build(self):
                                    self.title='Custom Video Player BSIT 2-2'
                                    return Builder.load('vid-play.kv')
                                
                                def change_slider_value(self, instance, value):
                                    position=(value/self.duration)*100
                                    self.root.ids.slider.value=position
                                    minutes=value/60
                                    seconds=minutes*60
                                    self.current_time=str(round(minutes))+':' +str(round(seconds)).zfill(2)
                                self.root.ids.time_duration.text=f'{self.current_time}/{self.time_duration}'
                                
                                def play_pause(self,button):
                                    self.root.ids.layout.remove_widgets(self.root.ids.thumbnail)
                                    if button.icon!='replay':
                                        if button.icon=='play':
                                            button.icon='paues'
                                            self.root.ids.video.state='play'
                                        else:
                                            button.icon='pause'
                                            self.root.ids.video.reload()
    def previous(self):
        self.root.ids.video.seek(0, precise=True)
        
        def next(self):
            self.root.ids.video.seek(1, precise=True)
                                     
                            
