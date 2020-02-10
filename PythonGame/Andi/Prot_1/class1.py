class Enemies:
    def __init__(self, image, speed_x, speed_y, start_pos:list=[0,0]):
        self.image = image
        self.position = np.zeros((100,2))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.start_pos = start_pos




