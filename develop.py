import numpy as np
import pandas as pd



class Poissons:
    
    def __init__(self, deplacement, reproduction, energie):
        self.deplacement = deplacement
        self.reproduction = reproduction
        self.energie = energie


    def mouvement(self):
        #mouvement random sur les cases adjacentes si case = 0
        pass
    # def energie(self):
    #     vie = 1



class Requins(Poissons):
    def __init__(self, deplacement, reproduction, energie, alimentation):
        super().__init__(deplacement, reproduction, energie)
        self.alimentation = alimentation