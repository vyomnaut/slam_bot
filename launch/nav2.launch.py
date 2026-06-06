import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    nav2_bringup = get_package_share_directory('nav2_bringup')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                os.path.join(nav2_bringup, 'launch', 'bringup_launch.py')
            ]),
            launch_arguments={
                'map': '/home/gourav/slam_ws/hospital_map.yaml',
                'use_sim_time': 'true',
            }.items()
        ),
    ])
