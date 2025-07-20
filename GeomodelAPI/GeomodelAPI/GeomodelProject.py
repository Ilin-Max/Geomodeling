from pathlib import Path
from Geomodel.Geomodel.Fild import Fild
from Geomodel.Geomodel.Well import Well

class GeomodelProject(Fild):
    def __init__(self, name="", main_pach = ""):
        self._main_path = main_pach
        self._wells_path = ""
        self.name = name
        
    @classmethod
    def OpenProject(cls, project_path):
        if Path(project_path).is_dir:
            project = cls(name=Path(project_path).name, main_pach = Path(project_path).absolute())
            project._wells_path = project._main_path / "Wells"
            return project
        else:
            pass

    @staticmethod
    def CreateProject(name):
        try:
            Path(name).mkdir(exist_ok=True)
            Path(f"{name}/Wells").mkdir(parents=True, exist_ok=True)
        except OSError as e:
            print(f"Error creating directories: {e}")

    @property
    def Wells(self):
        return [f.name for f in self._wells_path.iterdir() if f.is_dir()]
    
    def AddWell(self, name):
        try:
            Path(self._wells_path / name).mkdir(exist_ok=True)
        except OSError as e:
            print(f"Error creating directories: {e}")

    def Update(self):
        pass