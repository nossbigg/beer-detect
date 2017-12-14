from glob import glob
from subprocess import call

BLENDER_PATH = "/Applications/blender.app/Contents/MacOS/blender"
pythonRenderSingleModelFilepath = "./render_single_model.py"
blender_files = glob("../models/*.blend")

for blender_file_path in blender_files:
    command = BLENDER_PATH + " " + blender_file_path \
              + " --python " + pythonRenderSingleModelFilepath \
              + " --background"
    call(command, shell=True)
