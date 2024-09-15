from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():

    params_file_path = get_package_share_directory('test_espgnss') + '/params/espgnss_eval_params.yaml'

    return LaunchDescription([

        DeclareLaunchArgument(
            'params_file',
            default_value=params_file_path,
            description='Path to the YAML file containing the evaluation parameters'
        ),
        
        # Micro-ROS Agent
        # Node(
        #     package='micro_ros_agent',
        #     executable='micro_ros_agent',
        #     name='micro_ros_agent',
        #     arguments=["serial", "--dev", "/dev/ttyUSB1", "-v6"]
        # ),

        Node(
            package='micro_ros_agent',
            executable='micro_ros_agent',
            name='micro_ros_agent',
            arguments=["udp4", "-p", "8888", "-v6"]
        ),

        # NTRIP Client
        Node(
            name='ntrip_client',
            namespace='',
            package='ntrip_client',
            executable='ntrip_ros.py',
            parameters=[LaunchConfiguration('params_file')],
        ),  

        # GNSS evaluation
        Node(
            package='gnss_eval_ros',
            executable='gnss_eval',
            name='gnss_eval',
            parameters=[LaunchConfiguration('params_file')],
            remappings=[('/fix', '/esp_gnss_demo/fix')]
        ),
    ])