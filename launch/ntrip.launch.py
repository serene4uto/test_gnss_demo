from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('ntrip_client'), 'ntrip_client_launch.py')
            ),
            launch_arguments={
                'host': 'www.gnssdata.or.kr',
                'port': '2101',
                'mountpoint': 'KUNW-RTCM32',
                'username': 'kde1054@naver.com',
                'password': 'gnss'
            }.items()
        )
    ])