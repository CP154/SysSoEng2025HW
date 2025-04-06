from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_double_integrator',
            executable='double_integrator',
            name='double_integrator',
            output='screen'
        ),
        Node(
            package='my_double_integrator',
            executable='reference_position_publisher',
            name='reference_position_publisher',
            output='screen',
            parameters=[{'amplitude': 5.0}]  # Adjust amplitude as needed
        ),
        Node(
            package='my_double_integrator',
            executable='pid_controller',
            name='pid_controller',
            output='screen',
            parameters=[{'kp': 2.0}]  # Adjust gain as needed
        ),
        Node(
            package='my_double_integrator',
            executable='position_plotter',
            name='position_plotter',
            output='screen'
        ),
    ])
