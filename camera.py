from time import time


class Camera(object):

    def __init__(self):
        self.frames = [open('templates/images/' + 'frame' + str(f) + '.jpg', 'rb').read() for f in list(range(412))]
        self.counter = 0
        self.last_frame_update_time = time()

    def get_frame(self):
        current_time = time()
        if current_time - self.last_frame_update_time > 0.033333:
            self.counter += 1
            self.last_frame_update_time = current_time

        return self.frames[self.counter % 412]

        # return self.frames[int(time() * 100) % 412]
        # self.counter += 1
        # return self.frames[self.counter % 412]
