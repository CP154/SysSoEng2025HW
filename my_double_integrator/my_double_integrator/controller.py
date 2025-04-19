import rclpy
from rclpy.node import Node

from pid_controller_pkg.msg import ChristophPehlReference
from pid_controller_pkg.msg import ChristophPehlState
from pid_controller_pkg.msg import ChristophPehlControl
#Paketimporte 



class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')
        self.refresh_time = 0.1
        self.declare_parameter('kp', 2.0)
        self.kp = self.get_parameter('kp').value

        #Name Christoph Pehl und Matrikelnummer 5047889 angepasst
        self.control_publisher = self.create_publisher(ChristophPehlControl, 'control_signal_5047889', 10)
        self.state_subscriber = self.create_subscription(ChristophPehlState, 'integrator_state_5047889', self.update_state, 10)
        self.reference_subscriber = self.create_subscription(ChristophPehlReference, 'reference_position_5047889', self.update_reference_position, 10)

        self.timer = self.create_timer(self.refresh_time, self.publish_control_signal)

        self.current_position = 0.0
        self.reference_position = 0.0

    def update_state(self, msg):
        self.current_position = msg.position

    def update_reference_position(self, msg):
        self.reference_position = msg.reference_position

    def publish_control_signal(self):
        #Einfacher P Regler
        error = self.reference_position - self.current_position
        acceleration = self.kp * error
        #Typen gefixt
        control_msg = ChristophPehlControl()
        control_msg.acceleration = acceleration
        self.control_publisher.publish(control_msg)


       


def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

