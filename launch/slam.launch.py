from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rtabmap_slam',
            executable='rtabmap',
            name='rtabmap',
            output='screen',
            parameters=[{
                'subscribe_depth': False,
                'subscribe_rgb': False,
                'subscribe_scan': True,
                'approx_sync': True,
                'use_action_for_goal': True,
                'Reg/Strategy': '1',
                'Reg/Force3DoF': 'true',
                'RGBD/NeighborLinkRefining': 'true',
                'Grid/FromDepth': 'false',
            }],
            remappings=[
                ('scan', '/scan'),
                ('odom', '/odom'),
            ]
        ),
    ])
