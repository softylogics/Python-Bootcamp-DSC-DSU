

import time
lyrics = 'Band:Pink Floyd,Song:Breathe,          Full Lyrics,Breathe breathe in the air,Dont be afraid to care ,Leave but dont leave me ,Look around, choose your own ground ,For long you live and high you fly,And smiles youll give and tears youll cry,And all your touch and all you see,Is all your life will ever be,Run, rabbit run,Dig that hole, forget the sun,And when at last the work is done,Dont sit down, its time to dig another one,For long you live and high you fly,But only if you ride the tide,And balanced on the biggest wave,You race towards an early grave'

split_lyrics = lyrics.split(',')

for line in range(len(split_lyrics)):
    print(split_lyrics[line])
    time.sleep(1)