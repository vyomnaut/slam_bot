# slam_bot
ROS2 Humble | RTAB-Map SLAM | Nav2 Autonomous Navigation | Custom Hospital Gazebo World | Differential Drive Robot

00:38Claude responded: LiDAR + IMU + Odometrymarkdown# slam_bot 🤖

Autonomous Mobile Robot simulation built from scratch using ROS2 Humble, demonstrating a complete SLAM + Navigation pipeline in a custom hospital environment.

## 📹 Demo

[![slam_bot Demo](https://img.youtube.com/vi/QNGt4n7z3Pg/0.jpg)](https://youtu.be/QNGt4n7z3Pg)

## 🏥 About

This project simulates an Autonomous Mobile Robot (AMR) navigating through a hospital environment — directly inspired by real-world hospital logistics and the BGI Hackathon 2026. The robot builds a map of the environment using LiDAR-based SLAM, then autonomously navigates to goal positions while avoiding obstacles.

## 🛠️ Tech Stack

- **ROS2 Humble** — Robot middleware
- **RTAB-Map** — Graph-based SLAM with loop closure detection
- **Nav2** — Autonomous navigation, path planning, AMCL localization
- **Gazebo Classic** — Physics simulation
- **Python / C++** — Node development
- **Linux Ubuntu 22.04**

## 🤖 Robot Features

- Differential drive robot with custom URDF/Xacro
- 360° LiDAR sensor (12m range)
- IMU sensor for orientation
- Wheel odometry via Gazebo diff drive plugin
- Reactive obstacle avoidance

## 🗺️ Pipeline
LiDAR + IMU + Odometry
↓
RTAB-Map SLAM
↓
Occupancy Grid Map
↓
Nav2 (AMCL + Planner)
↓
Autonomous Navigation

## 🏗️ World

Custom hospital Gazebo world featuring:
- Main corridor with pillars
- 3 patient rooms with beds
- Nurse station
- Reception desk
- Blocked emergency exit (navigation challenge)

## 🚀 How to Run

**Prerequisites:**
```bash
sudo apt install ros-humble-rtabmap-ros ros-humble-navigation2 ros-humble-nav2-bringup -y
```

**Launch Gazebo + Robot:**
```bash
cd ~/slam_ws && source install/setup.bash
ros2 launch slam_bot gazebo.launch.py
```

**Launch SLAM:**
```bash
ros2 launch slam_bot slam.launch.py
```

**Launch Nav2:**
```bash
ros2 launch slam_bot nav2.launch.py
```

**Launch RViz:**
```bash
rviz2 -d /opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz
```

## 📁 Project Structure
slam_bot/
├── urdf/
│   └── robot.urdf.xacro      # Robot description
├── launch/
│   ├── gazebo.launch.py       # Gazebo + robot spawn
│   ├── slam.launch.py         # RTAB-Map SLAM
│   └── nav2.launch.py         # Nav2 navigation
├── worlds/
│   └── hospital.world         # Custom hospital environment
└── CMakeLists.txt

## 👤 Author

**Gourav Jaiswal**
B.Tech Robotics & Automation — Medicaps University, Indore
[GitHub](https://github.com/vyomnaut)
