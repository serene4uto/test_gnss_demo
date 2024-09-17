from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch import LaunchContext
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import GroupAction


def generate_launch_description():
    gps_wpf_dir = get_package_share_directory("test_gnss_demo")
    mapviz_config_file = os.path.join(gps_wpf_dir, "config", "gps_wpf_demo.mvc")

    mapviz_group_action = GroupAction([ 
        Node(
            package="mapviz",
            executable="mapviz",
            name="mapviz",
            parameters=[{"config": mapviz_config_file}],
            # remappings=[('/fix', '/esp_gnss_demo/fix')]
        ),
        Node(
            package="swri_transform_util",
            executable="initialize_origin.py",
            name="initialize_origin",
            parameters=[
                {"local_xy_frame": "map"},
                {"local_xy_origin": "origin"},
                {
                    "local_xy_origins": [
                        36.1166293,
                        128.3647848,
                        0.0,
                        0.0,
                    ]
                },
            ],
            remappings=[('/fix', '/esp_gnss_demo/fix')]
        ),
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            name="swri_transform",
            arguments=["0", "0", "0", "0", "0", "0", "map", "origin"]
        )
    ])


    ld = LaunchDescription()

    ld.add_action(mapviz_group_action)

    return ld