import rclpy
from rclpy.node import Node

## TODO:
# Custom message types msg type is your FirstNameLastNameState for the double integrator state
# Custom message types msg type is your FirstNameLastNameReference for the reference position
# Custom message types msg type is your FirstNameLastNameControl for the control command



class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')
        self.refresh_time = 0.1
        self.declare_parameter('kp', 2.0)
        self.kp = self.get_parameter('kp').value

        # TODO: Change the message types to your custom message types
        # Topic names should include your matriculation number
        self.control_publisher = self.create_publisher(ControlCommand, 'control_signal', 10)
        self.state_subscriber = self.create_subscription(DoubleIntegratorState, 'integrator_state', self.update_state, 10)
        self.reference_subscriber = self.create_subscription(ReferencePosition, 'reference_position', self.update_reference_position, 10)
        self.timer = self.create_timer(self.refresh_time, self.publish_control_signal)

        self.current_position = 0.0
        self.reference_position = 0.0

    def update_state(self, msg):
        self.current_position = msg.position

    def update_reference_position(self, msg):
        self.reference_position = msg.reference_position

    def publish_control_signal(self):
        ## TODO # Implement the PID control algorithm


        #TODO Fix the type
        control_msg = ControlCommand()
        control_msg.acceleration = 0.0
        self.control_publisher.publish(control_msg)


def main(args=None):
    rclpy.init(args=args)
    node = PIDController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

