import json5,lupa,resources.srcLibs.sc2jlfdmf as csvThingy,sounddevice as sd,soundfile as sf,pygame,time,os,sys,resources.srcLibs.SparrowAnimation
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from multiprocessing import Process
dialogues=json5.loads(open("resources/dialogue.json","r").read())
dialogueID=json5.loads(open("resources/dialogueID.json","r").read())
loadingLines=json5.loads(open("resources/loadingLines.json","r").read())
dialogueModes=csvThingy.process("resources/dialogueModes.csv")
def deallocateEVERYTHING():
    for var in list(globals().keys()):
       if not var.startswith('__'):del globals()[var]
# audio
def playTHEAUDIO(audio, wait=True, start=0):
    data, sr=sf.read(f"resources/audio/{audio}")
    data=data[int(start*sr):]
    sd.play(data,sr)
    if wait:sd.wait()
# lua api
def dialogue(who,id,audio,wait=True):
    print(eval(f'dialogue{dialogueID[f"{who}.{id}"]}',{"dialogue":dialogues}))
    playTHEAUDIO(audio,wait)
dialogue("coathangerTree","3","tree/tips/3.wav")
def audio_task():
    playTHEAUDIO("PANTS.wav")
#if __name__=="__main__":
#    p=Process(target=audio_task)
#    p.start()
#    for _ in range(100000000):
#        sum(i*i for i in range(10000))
#    p.join()
Window.title = "Larry's Detour"
Window.size = (1280, 720)
class LoaderManager(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loading_screen = None
        self.lines = None
        self.loadLines()
        self.loadLayout("resources/layouts/title.kv")
    def loadLines(self):
        self.lines = loadingLines
    def loadLayout(self, layout_path):
        if layout_path.endswith("loading.kv"):
            return
        if not self.loading_screen:
            Builder.load_file("resources/layouts/loading.kv")
            self.loading_screen = Builder.load_string("""
LoadingScreen:
""") # man, what a sh-
            self.add_widget(self.loading_screen)
            self.loading_screen.opacity = 1
            self.loading_screen.percentage = 0
            self.loading_screen.status_line = self.lines["0"]
        Clock.schedule_once(lambda dt: self._start_loading(layout_path), 0)
    def _start_loading(self, layout_path):
        self.current_percent = 0
        self.target_layout = layout_path
        self._advance_loading()
    def _advance_loading(self, *args):
        if self.current_percent >= 100:
            self._transition()
            return
        self.current_percent += 1
        available = [int(k) for k in self.lines if int(k) <= self.current_percent]
        if available:
            key = str(max(available))
            self.loading_screen.status_line = self.lines[key]
        self.loading_screen.percentage = self.current_percent
        Clock.schedule_once(self._advance_loading, 0.01)
    def _transition(self):
        anim = Animation(y=self.height, d=0.6, t='in_quad')
        anim.bind(on_complete=lambda *args: self._finalize(self.target_layout))
        anim.start(self.loading_screen.children[0])
    def _finalize(self, layout_path):
        self.remove_widget(self.loading_screen)
        self.loading_screen = None
        Builder.unload_file(layout_path)
        Builder.load_file(layout_path)
        new_root = Builder.template("Root")
        self.clear_widgets()
        self.add_widget(new_root)
class Game(App):
    def build(self):
        self.manager = LoaderManager()
        return self.manager
    def switch_to_layout(self, name):
        self.manager.loadLayout(f"resources/layouts/{name}.kv")
    def play(self):
        self.switch_to_layout("play")
    def settings(self):
        self.switch_to_layout("settings")
    def help(self):
        self.switch_to_layout("help")
if __name__ == "__main__":
    Game().run()