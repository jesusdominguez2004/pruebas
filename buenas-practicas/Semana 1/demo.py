
class Cadenas:
    def __init__(self) -> None:
        self.len = 0
        self.vector = []
    
    def set_len(self, x:int):
        self.len = x

    def get_len(self) -> int:
        return self.len

    def set_vector(self, x:list):
        self.vector = x

    def get_vector(self) -> list:
        return self.vector

