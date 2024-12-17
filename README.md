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
