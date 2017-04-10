## *********************************************************
## 
## File autogenerated for the realsense_camera package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 235, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'R200_DEPTH_CONTROL', 'lower': 'r200_depth_control', 'srcline': 109, 'name': 'R200_Depth_Control', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::R200_DEPTH_CONTROL', 'field': 'DEFAULT::r200_depth_control', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 50, 'description': 'R200 Depth Control Preset', 'max': 5, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_preset', 'edit_method': "{'enum_description': 'Depth Control Preset Choices', 'enum': [{'srcline': 39, 'description': 'Individual Depth Control was changed', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': -1, 'ctype': 'int', 'type': 'int', 'name': 'UNUSED'}, {'srcline': 40, 'description': 'Default settings on chip. Similar to Medium. Best for Outdoors.', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Default'}, {'srcline': 41, 'description': 'Disable almost all hardware-based outlier removal.', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'Off'}, {'srcline': 42, 'description': 'Lower number of outliers removed. Minimal false negatives.', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'Low'}, {'srcline': 43, 'description': 'Medium number of outliers removed. Balanced approach.', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'Medium'}, {'srcline': 44, 'description': 'Medium-High number of outliers removed. Derived optimization function.', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'Optimized'}, {'srcline': 45, 'description': 'Higher number of outliers removed. Minimal false positives.', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'High'}]}", 'default': 5, 'level': 64, 'min': -1, 'type': 'int'}, {'srcline': 52, 'description': 'Estimate Median Decrement', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_estimate_median_decrement', 'edit_method': '', 'default': 5, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 54, 'description': 'Estimate Median Increment', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_estimate_median_increment', 'edit_method': '', 'default': 5, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 56, 'description': 'Median Threshold', 'max': 1023, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_median_threshold', 'edit_method': '', 'default': 235, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 58, 'description': 'Score Minimum Threshold', 'max': 1023, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_score_minimum_threshold', 'edit_method': '', 'default': 27, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 60, 'description': 'Score Maximum Threshold', 'max': 1023, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_score_maximum_threshold', 'edit_method': '', 'default': 420, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 62, 'description': 'Texture Count Threshold', 'max': 31, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_texture_count_threshold', 'edit_method': '', 'default': 8, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 64, 'description': 'Texture Difference Threshold', 'max': 1023, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_texture_difference_threshold', 'edit_method': '', 'default': 80, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 66, 'description': 'Second Peak Threshold', 'max': 1023, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_second_peak_threshold', 'edit_method': '', 'default': 70, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 68, 'description': 'Neighbor Threshold', 'max': 1023, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_neighbor_threshold', 'edit_method': '', 'default': 90, 'level': 32, 'min': 0, 'type': 'int'}, {'srcline': 70, 'description': 'LR Threshold', 'max': 2047, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/home/nvidia/jetson-car/src/vision/realsense_camera/cfg/zr300_params.cfg', 'name': 'r200_dc_lr_threshold', 'edit_method': '', 'default': 12, 'level': 32, 'min': 0, 'type': 'int'}], 'type': '', 'id': 1}], 'parameters': [{'srcline': 280, 'description': 'Enable Depth', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'enable_depth', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 280, 'description': 'Backlight Compensation', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_backlight_compensation', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Brightness', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_brightness', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Contrast', 'max': 64, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_contrast', 'edit_method': '', 'default': 50, 'level': 0, 'min': 16, 'type': 'int'}, {'srcline': 280, 'description': 'Exposure', 'max': 666, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_exposure', 'edit_method': '', 'default': 166, 'level': 0, 'min': 50, 'type': 'int'}, {'srcline': 280, 'description': 'Gain', 'max': 256, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_gain', 'edit_method': '', 'default': 64, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Gamma', 'max': 280, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_gamma', 'edit_method': '', 'default': 300, 'level': 0, 'min': 100, 'type': 'int'}, {'srcline': 280, 'description': 'Hue', 'max': 2200, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_hue', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2200, 'type': 'int'}, {'srcline': 280, 'description': 'Saturation', 'max': 255, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_saturation', 'edit_method': '', 'default': 64, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Sharpness', 'max': 7, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_sharpness', 'edit_method': '', 'default': 50, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'White Balance', 'max': 8000, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_white_balance', 'edit_method': '', 'default': 4600, 'level': 0, 'min': 2000, 'type': 'int'}, {'srcline': 280, 'description': 'LR Gain', 'max': 6399, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r200_lr_gain', 'edit_method': '', 'default': 400, 'level': 0, 'min': 100, 'type': 'int'}, {'srcline': 280, 'description': 'LR Exposure', 'max': 164, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r200_lr_exposure', 'edit_method': '', 'default': 164, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 280, 'description': 'Enable Auto Exposure', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_enable_auto_exposure', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Enable Auto White Balance', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'color_enable_auto_white_balance', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Enable LR Auto Exposure', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r200_lr_auto_exposure_enabled', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Emitter Enabled', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r200_emitter_enabled', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Depth Clamp Min', 'max': 65535, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r200_depth_clamp_min', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Depth Clamp Max', 'max': 65535, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r200_depth_clamp_max', 'edit_method': '', 'default': 65535, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Exposure', 'max': 331, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_exposure', 'edit_method': '', 'default': 40, 'level': 0, 'min': 40, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Gain', 'max': 2047, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_gain', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Enable Auto Exposure', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_enable_auto_exposure', 'edit_method': '', 'default': 1, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Auto Exposure Mode', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_auto_exposure_mode', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Auto Exposure Antiflicker Rate', 'max': 60, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_auto_exposure_antiflicker_rate', 'edit_method': '', 'default': 60, 'level': 0, 'min': 50, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Auto Exposure Pixel Sample Rate', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_auto_exposure_pixel_sample_rate', 'edit_method': '', 'default': 1, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 280, 'description': 'Fisheye Auto Exposure Skip Frames', 'max': 3, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fisheye_auto_exposure_skip_frames', 'edit_method': '', 'default': 2, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 280, 'description': 'Frames Queue Size', 'max': 20, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'frames_queue_size', 'edit_method': '', 'default': 20, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 280, 'description': 'Hardware Logger Enabled', 'max': 1, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'hardware_logger_enabled', 'edit_method': '', 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

zr300_params_UNUSED = -1
zr300_params_Default = 0
zr300_params_Off = 1
zr300_params_Low = 2
zr300_params_Medium = 3
zr300_params_Optimized = 4
zr300_params_High = 5
