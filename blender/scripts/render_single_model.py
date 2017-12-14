import os

import bpy
import mathutils
import numpy as np

render_folder_path = "../rendered_images/"
source_file_name = os.path.basename(bpy.data.filepath)
subfolder_path = render_folder_path + "/" + source_file_name
os.makedirs(subfolder_path, exist_ok=True)

y_offset_limit = 5.00000
y_offset_step = 0.5
y_offset_range = np.arange(-y_offset_limit, y_offset_limit + y_offset_step, y_offset_step)

camera_anchor = bpy.data.objects["CameraAnchor"]
camera = bpy.data.objects["Camera"]

animation_number_of_frames = 120
scene = bpy.context.scene

for y_offset in y_offset_range:
    # set cameraAnchor to new position
    camera_anchor.location = mathutils.Vector((0.0, y_offset, 0.0))

    # start saving animation
    for frame_number in range(0, animation_number_of_frames + 1, 10):
        scene.frame_set(frame_number)

        frame_file_name = source_file_name + ".x0y" + str(y_offset) + "z0.n" + str(
            frame_number)
        bpy.context.scene.render.filepath = os.path.join(subfolder_path, frame_file_name)

        bpy.ops.render.render(write_still=True)
