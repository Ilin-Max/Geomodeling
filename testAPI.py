from GeomodelAPI.GeomodelAPI.GeomodelProject import GeomodelProject

Project = GeomodelProject.OpenProject("test_project")
Project.AddWell("PA-128")
print(Project._main_path)
print(Project._wells_path)
print(Project.Wells)

