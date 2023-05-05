import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["base64", "json", "time", "requests", "selenium", "logging"],
                     "include_files": ["chromedriver"]}
# 打包可能缺依赖

setup(name="video",
      version="0.1",
      description="Description of my program",
      options={"build_exe": build_exe_options},
      install_requires=['rich'],
      executables=[Executable("src/videos/AppGui.py", base=None)])
