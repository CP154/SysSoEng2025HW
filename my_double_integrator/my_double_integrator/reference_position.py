import rclpy
from rclpy.node import Node
from pid_controller_pkg.msg import ChristophPehlReference #referenz importiert
import math


class ReferencePositionPublisher(Node):
    def __init__(self):
        super().__init__('reference_position_publisher')
        self.refresh_time = 0.1
        self.declare_parameter('amplitude', 5.0)
        self.amplitude = self.get_parameter('amplitude').value
        
        self.reference_publisher = self.create_publisher(ChristophPehlReference, 'reference_position_5047889', 10) #Angepasst
        self.timer = self.create_timer(self.refresh_time, self.publish_reference_position)

        self.time_elapsed = 0.0

    def publish_reference_position(self):
        self.time_elapsed += self.refresh_time
        reference_msg = ReferencePosition()
        reference_msg.reference_position = self.amplitude * math.sin(0.1 * self.time_elapsed)
        self.reference_publisher.publish(reference_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ReferencePositionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
