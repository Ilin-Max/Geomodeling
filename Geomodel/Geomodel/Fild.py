from .Well import Well

class Fild():
    def __init__(self, name, wells = {}):
        self.name = name
        self.wells = wells

    def AddWell(self, well):
        if well not in self.wells.keys():
            self.wells[well.name] = well
        else:
            pass 
    
    def DelWell(self, well_name):
        try:
            del self.wells[well_name]
        except KeyError:
            pass
        