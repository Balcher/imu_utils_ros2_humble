# imu_utils_ros2_humble
calculate Allan variance for SIMU gyro & amp; acc  
Ref:  
1. https://github.com/alalagong/imu_allan
2. https://github.com/gaowenliang/code_utils
3. https://github.com/freesix/imu_utils_ros2

# introduction

imu_utils是一个轻量级的IMU标定工具，主要用于校准IMU的偏差和尺度因子，配置和使用相对简单，适合快速标定需求。

# 环境以及编译

1. 首先安装相关依赖
    ```
    sudo apt-get install liblapack-dev libsuitesparse-dev libcxsparse3 libgflags-dev libgoogle-glog-dev libgtest-dev libdw-dev
    ```
    以及`ceres-solver`，这个需要源码安装一下，源码位置：`https://github.com/ceres-solver/ceres-solver`
2. code_utils依赖ceres，imu_utils依赖code_utils, 所以需要先编译code_utils，然后再编译imu_utiles。
    ```
    colcon build --packages-select code_utils
    source ./install/setup.bash
    colcon build --packages-select imu_utils
    ```

# 运行
1. 首先录制一段IMU的数据，这个数据时间最好长一点，比如一两个小时这种。
2. 设置相关参数，在`/imu_utils.launch.py`中，更改`imu_topic`的话题名称。
3. 然后编译一下。
4. 同时运行rosbag和launch文件，或者先打开launch文件，然后再运行,rosbag运行的时候是以200倍速度播放的。
    ```
    ros2 launch imu_utils imu_utils.launch.py
    ros2 bag play -r 200 rosbag2_2024_12_17-14_33_26/
    ```
5. 在所设置的保存路径下会保存相关的标定结果。