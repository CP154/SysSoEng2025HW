import rclpy
from rclpy.node import Node

from pid_controller_pkg.msg import ChristophPehlState
from pid_controller_pkg.msg import ChristophPehlReference
#imports hinzugefügt

import matplotlib.pyplot as plt

class PlottingNode(Node):
    def __init__(self):
        super().__init__('plotting')
        
        #Typ und Name gefixt        
        self.subscription = self.create_subscription(ChristophPehlReference, '/reference_position_5047889', self.listener_callback, 20)
        self.output_subscription = self.create_subscription(ChristophPehlState, '/integrator_state_5047889', self.output_callback, 20)  
      
        self.reference_data = []
        self.output_data = []
        self.time_data = []
        self.time = 0.0
        self.reference_signal = 0.0 

        
        plt.ion()
        self.figure, self.ax = plt.subplots()

    def listener_callback(self, msg):
        self.reference_signal = msg.data

    def output_callback(self, msg):
        system_output = msg.data
        self.reference_data.append(self.reference_signal)
        self.output_data.append(system_output)
        self.time_data.append(self.time)
        self.time += 0.05

        
        self.update_plot()

        


    def update_plot(self):
        self.ax.clear()
        self.ax.plot(self.time_data, self.reference_data, label="Toxicity Reference")
        self.ax.plot(self.time_data, self.output_data, label="Toxicity")
        
        
        self.ax.legend()
        self.ax.set_xlabel("Time (in days)")
        self.ax.set_ylabel("Toxicity (mg/ml)")

        plt.draw()
        plt.pause(0.05)

def main(args=None):
    rclpy.init(args=args)
    node = PlottingNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
