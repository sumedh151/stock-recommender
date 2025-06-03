
from scipy import spatial

class Measure:
    def __init__(self, X, Y):
        self.x = X
        self.y = Y
        self._cosine = None
        self._euclidean = None

    @property
    def cosine_sim(self):
        if self._cosine is None:
            self._cosine = 1 - spatial.distance.cosine(self.x, self.y)
        return self._cosine

    @property
    def euclidean(self):
        if self._euclidean is None:
            self._euclidean = spatial.distance.euclidean(self.x, self.y)
        return self._euclidean
