import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class AutoDrive(Node):
    def __init__(self):
        super().__init__('auto_drive')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.drive)
        self.start_time = time.time()

    def drive(self):
        msg = Twist()
        t = time.time() - self.start_time

        if t < 5:        # go forward
            msg.linear.x = 0.3
        elif t < 8:      # turn left
            msg.angular.z = 0.5
        elif t < 13:     # go forward
            msg.linear.x = 0.3
        elif t < 16:     # turn left
            msg.angular.z = 0.5
        elif t < 21:     # go forward
            msg.linear.x = 0.3
        elif t < 24:     # turn left
            msg.angular.z = 0.5
        elif t < 29:     # go forward
            msg.linear.x = 0.3
        elif t < 32:     # turn left
            msg.angular.z = 0.5
        else:            # stop
            msg.linear.x = 0.0

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = AutoDrive()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
