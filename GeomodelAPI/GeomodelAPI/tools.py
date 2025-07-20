import os 
import pandas as pd
import numpy as np
from pathlib import Path

class ProjectEror(Exception):
    pass

name_file_info = "_project_info.txt"

def copy_file_content(source_file: str, destination_file: str):
    """Копирует содержимое одного файла в другой (новый) файл"""
    
    source_path = Path(source_file)
    destination_path = Path(destination_file)

    content = source_path.read_text(encoding='utf-8')

    destination_path.write_text(content, encoding='utf-8')

def CreateProject(projects_name):
    Path(projects_name).mkdir()
    Path(projects_name + "/Wells").mkdir(parents=True)
    Path(projects_name + "/Well_tops").mkdir()

def is_project(path_project):
    path_file_info = path_project / name_file_info
    return path_project.exists() & path_project.is_dir() & path_file_info.exists()

def OpenProject(path):
    path_project = Path(path)

    if not is_project(path_project):
        raise ProjectEror("Ошибка открытия проекта")
    
    return path_project
        
def GetInfo(path_file_info):
    print (path_file_info.read_text())


