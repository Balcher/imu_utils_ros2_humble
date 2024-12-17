from launch import LaunchDescription
from launch_ros.actions import Node 
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # imu_utils_share_dir = get_package_share_directory('imu_utils')
    imu_utils_share_dir = "/home/jpx/Documents/imu_utils_ros2_humble/src/imu_utils"
    data_save_path = imu_utils_share_dir + '/data/'

    return LaunchDescription([
        Node(
            package='imu_utils',
            executable='imu_an',
            name='imu_utils_node',
            output='screen',
            parameters=[{
                'imu_topic': '/camera/gyro_accel/sample',
                'imu_name': 'my_imu',
                'data_save_path': data_save_path,
                'max_time_min': 50,  
                'max_cluster': 100
            }]
        )
    ])