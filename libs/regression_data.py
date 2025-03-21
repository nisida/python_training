import numpy as np


class regression_data() :
    
    """ setup regression data
    """
    
    def __init__(self):
        # Data
        THROW  = np.array([22, 36, 24, 22, 27, 29, 26, 23, 31, 24, 23, 27, 31, 25, 23], dtype=np.float32) # ボール投げ
        GRIP   = np.array([28, 46, 39, 25, 34, 29, 38, 23, 42, 27, 35, 39, 38, 32, 25], dtype=np.float32) #  握力
        HEIGHT = np.array([146, 169, 160, 156, 161, 168, 154, 153, 160, 152, 155, 154, 157, 162, 142], dtype=np.float32) # 身長
        WEIGHT = np.array([34, 57, 48, 38, 47, 50, 54, 40, 62, 39, 46, 54, 57, 53, 32], dtype=np.float32) # 体重
        NORMALIZE = 100.0

        _l = []
        for i in range(15) :
            _a = np.array([GRIP[i], HEIGHT[i], WEIGHT[i]], dtype=np.float32)
            _l.append(_a)
        self.x = np.array(_l) / NORMALIZE
        self.y = THROW.reshape([THROW.shape[0], 1]) / NORMALIZE
        
        
    def get_data(self):
        return self.x, self.y
