import rclpy
from rclpy.node import Node
from pid_controller_pkg.msg import ChristophPehlState
# Add your reference signal message import here! --> Nicht benötigter import??
from pid_controller_pkg.msg import ChristophPehlControl

class DoubleIntegrator(Node):
    def __init__(self):
        super().__init__('double_integrator')
        self.refresh_time = 0.1
        self.state_publisher = self.create_publisher(ChristophPehlState, 'integrator_state_5047889', 10) #angepasst
        self.control_subscriber = self.create_subscription(ChristophPehlControl, 'control_signal_5047889', self.update_acceleration, 10)
        self.timer = self.create_timer(self.refresh_time, self.publish_state)

        self.position = 0.0
        self.velocity = 0.0
        self.acceleration = 0.0

    def publish_state(self):
        self.velocity += self.acceleration * self.refresh_time
        self.position += self.velocity * self.refresh_time

        state_msg = DoubleIntegratorState()
        state_msg.position = self.position
        state_msg.velocity = self.velocity
        self.state_publisher.publish(state_msg)

    def update_acceleration(self, msg):
        self.acceleration = msg.acceleration


def main(args=None):
    rclpy.init(args=args)
    node = DoubleIntegrator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
