import os
from cx_Freeze import setup, Executable

executables = [
    Executable('mn2.py')
]

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

setup(name='Esteban Escapes',
      version='0.1',
      description='Game',
      options = {"build_exe": {"packages": ["pygame"], "include_files": ["MainMenu.py", "sp2.py", "settings.py", "MainMenuBackground.png", "images/*", "/*", "Ancient, Desert, Thoughtful Song - Non Copyright, Royalty Free.ogg", "map.txt", "transpBlack75.png", "pyramidSpinIMG/frame_00_delay-0.06s.png", "pyramidSpinIMG/frame_01_delay-0.06s.png", "pyramidSpinIMG/frame_02_delay-0.06s.png", "pyramidSpinIMG/frame_03_delay-0.06s.png", "pyramidSpinIMG/frame_04_delay-0.06s.png", "pyramidSpinIMG/frame_05_delay-0.06s.png", "pyramidSpinIMG/frame_06_delay-0.06s.png", "pyramidSpinIMG/frame_07_delay-0.06s.png", "pyramidSpinIMG/frame_08_delay-0.06s.png", "pyramidSpinIMG/frame_09_delay-0.06s.png", "pyramidSpinIMG/frame_10_delay-0.06s.png", "pyramidSpinIMG/frame_11_delay-0.06s.png", "pyramidSpinIMG/frame_12_delay-0.06s.png", "pyramidSpinIMG/frame_13_delay-0.06s.png", "pyramidSpinIMG/frame_14_delay-0.06s.png", "pyramidSpinIMG/frame_15_delay-0.06s.png", "pyramidSpinIMG/frame_16_delay-0.06s.png", "pyramidSpinIMG/frame_17_delay-0.06s.png", "pyramidSpinIMG/frame_18_delay-0.06s.png", "pyramidSpinIMG/frame_19_delay-0.06s.png", "pyramidSpinIMG/frame_20_delay-0.06s.png", "pyramidSpinIMG/frame_21_delay-0.06s.png", "pyramidSpinIMG/frame_22_delay-0.06s.png", "pyramidSpinIMG/frame_23_delay-0.06s.png", "pyramidSpinIMG/frame_24_delay-0.06s.png", "pyramidSpinIMG/frame_25_delay-0.06s.png", "pyramidSpinIMG/frame_26_delay-0.06s.png", "pyramidSpinIMG/frame_27_delay-0.06s.png", "pyramidSpinIMG/frame_28_delay-0.06s.png", "pyramidSpinIMG/frame_29_delay-0.06s.png", "pyramidSpinIMG/frame_30_delay-0.06s.png", "pyramidSpinIMG/frame_31_delay-0.06s.png", "images/ESTE.png", "images/Esteban/0.png", "images/Esteban/1.png", "images/Esteban/2.png", "images/Esteban/3.png", "images/Esteban/4.png", "images/Esteban/5.png", "images/Esteban/6.png", "images/Esteban/7.png", "images/hala.jpeg", "images/m.png", "images/ml.png", "images/mr.png", "images/mt.png", "images/platform-1.png", "images/skull.png", "images/templewip1.png", "images/tl.png", "images/tr.png"]}},
      executables =executables
      )