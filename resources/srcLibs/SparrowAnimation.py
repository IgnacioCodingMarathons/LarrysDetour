import os
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.graphics.texture import TextureRegion
from xml.etree import ElementTree as ET
from kivy.core.image import Image as CoreImage
class SparrowAnimation(Image):
    atlas = StringProperty("")        # Path to XML
    interval = NumericProperty(1/30.) # Seconds between frames
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frames = []
        self.current_frame = 0
        self._anim_ev = None
    def on_atlas(self, *args):
        self.load_spritesheet()
    def load_spritesheet(self):
        self.frames.clear()
        self.current_frame = 0
        if not self.atlas or not os.path.exists(self.atlas):
            return
        tree = ET.parse(self.atlas)
        root = tree.getroot()
        image_path = os.path.join(os.path.dirname(self.atlas), root.attrib['imagePath'])
        base_image = CoreImage(image_path).texture
        for sub in root.findall('SubTexture'):
            x = int(sub.attrib['x'])
            y = int(sub.attrib['y'])
            w = int(sub.attrib['width'])
            h = int(sub.attrib['height'])
            tex = base_image.get_region(x, base_image.height - y - h, w, h)
            self.frames.append(tex)
        if self.frames:
            self.texture = self.frames[0]
            self.start()
    def start(self):
        if self._anim_ev:
            self._anim_ev.cancel()
        self._anim_ev = Clock.schedule_interval(self.update, self.interval)
    def update(self, dt):
        if not self.frames:
            return
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.texture = self.frames[self.current_frame]
    def on_parent(self, instance, parent):
        if parent:
            self.start()
        elif self._anim_ev:
            self._anim_ev.cancel()