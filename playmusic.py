import pygame, sys, os

FREQ = 44100   # audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 = mono, 2 = stereo
BUFFER = 1024  # audio buffer size in no. of samples

#for Clock
FPS = 30 

soundfile = os.path.join('music','music.mp3')

try:
    pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
except pygame.error, exc:
    print "Sound Error %s" % exc

try:
    pygame.init()

    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.event.set_allowed(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    pygame.event.wait()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN):
                pressed = pygame.key.name(event.key)
                print 'pressed ' + pressed
        
except pygame.error, exc:
    print >>sys.stderr, "Could not play sound file: %s" % soundfile
    print exc
