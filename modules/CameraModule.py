import cv2 as cv

class CameraModule:

    def __int__(self):
        self.camera = cv.VideoCapture(0)

        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera.")

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            _return, frame = self.camera.read()

            if _return:
                return (_return, cv.cvtColor(frame, cv.COLOR_BGR2RGB))

            else:
                return (_return, None)
        else:
            return None