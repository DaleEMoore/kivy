__author__ = 'dalem'
# From: http://inclem.net/pages/kivy-crash-course/
#   https://www.youtube.com/watch?v=F7UKmK9eQLY&list=PLdNh1e1kmiPP4YApJm8ENK2yMlwF1_edq
#   buildozer init
#   ... write code ...
#   buildozer android debug

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello!",
                  font_size=150)
        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == "__main__":
    TutorialApp().run()
"""
/usr/bin/python2.7 /home/dalem/PycharmProjects/kivy/main.py
[INFO              ] Kivy v1.8.0
[INFO              ] [Logger      ] Record log in /home/dalem/.kivy/logs/kivy_14-10-21_1.txt
[INFO              ] [Factory     ] 157 symbols loaded
[DEBUG             ] [Cache       ] register <kv.lang> with limit=None, timeout=Nones
[DEBUG             ] [Cache       ] register <kv.image> with limit=None, timeout=60s
[DEBUG             ] [Cache       ] register <kv.atlas> with limit=None, timeout=Nones
[INFO              ] [Image       ] Providers: img_tex, img_dds, img_pygame, img_pil, img_gif
[DEBUG             ] [Cache       ] register <kv.texture> with limit=1000, timeout=60s
[DEBUG             ] [Cache       ] register <kv.shader> with limit=1000, timeout=3600s
[INFO              ] [Text        ] Provider: pygame
[DEBUG             ] [App         ] Loading kv </home/dalem/PycharmProjects/kivy/tutorial.kv>
[DEBUG             ] [App         ] kv </home/dalem/PycharmProjects/kivy/tutorial.kv> not found
[DEBUG             ] [Window      ] Ignored <egl_rpi> (import error)
[INFO              ] [Window      ] Provider: pygame(['window_egl_rpi'] ignored)
[DEBUG             ] [Window      ] Display driver x11
[DEBUG             ] [Window      ] Actual window size: 800x600
[DEBUG             ] [Window      ] Actual color bits r8 g8 b8 a0
[DEBUG             ] [Window      ] Actual depth bits: 24
[DEBUG             ] [Window      ] Actual stencil bits: 8
[DEBUG             ] [Window      ] Actual multisampling samples: 2
[INFO              ] [GL          ] OpenGL version <3.0 Mesa 10.1.3>
[INFO              ] [GL          ] OpenGL vendor <X.Org>
[INFO              ] [GL          ] OpenGL renderer <Gallium 0.4 on AMD SUMO2>
[INFO              ] [GL          ] OpenGL parsed version: 3, 0
[INFO              ] [GL          ] Shading version <1.30>
[INFO              ] [GL          ] Texture max size <16384>
[INFO              ] [GL          ] Texture max units <16>
[DEBUG             ] [Shader      ] Fragment compiled successfully
[DEBUG             ] [Shader      ] Vertex compiled successfully
[DEBUG             ] [ImagePygame ] Load </usr/lib/python2.7/dist-packages/kivy/data/glsl/default.png>
[INFO              ] [Window      ] virtual keyboard not allowed, single mode, not docked
[INFO              ] [OSC         ] using <multiprocessing> for socket
[DEBUG             ] [Base        ] Create provider from mouse
[DEBUG             ] [Base        ] Create provider from probesysfs
[DEBUG             ] [ProbeSysfs  ] using probsysfs!
[INFO              ] [Base        ] Start application main loop
[INFO              ] [GL          ] NPOT texture support is available
"""