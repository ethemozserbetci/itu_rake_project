import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    tb3_nav_dir = get_package_share_directory('turtlebot3_navigation2')
    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb3_nav_dir, 'launch', 'navigation2.launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'True', 
            'map': os.path.expanduser('~/ros2_ws/src/itu_rake_project/config/map.yaml')
        }.items()
    )

    coord_node = Node(
        package='itu_rake_project',
        executable='coordinate_tracker',
        name='coordinate_tracker',
        output='screen'
    )

    return LaunchDescription([
        nav_launch,
        coord_node
    ])
