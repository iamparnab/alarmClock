import pygame


class PlayTone:
    def __init__(self, dd):
        pygame.init()
        self.dd = dd

    def play(self):
        text = self.dd.currentText()
        try:
            if text == 'Bird':
                pygame.mixer.music.load('./RingTones/bird.wav')
            elif text == 'Bird 2':
                pygame.mixer.music.load('./RingTones/bird_chirping2.wav')
            elif text == 'Mario':
                pygame.mixer.music.load('./RingTones/mario.wav')
            elif text == 'Rooster':
                pygame.mixer.music.load('./RingTones/rooster.wav')
            else:
                pygame.mixer.music.load(None)
        except:
            self.stop()
        else:
            pygame.mixer.music.play(loops=1, start=0.0)

    def stop(self):
        pygame.mixer.music.stop()