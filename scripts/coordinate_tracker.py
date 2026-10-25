import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import threading

class CoordinateTracker(Node):
    def __init__(self):
        super().__init__('coordinate_tracker')
        
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        
        self.x = 0.0
        self.y = 0.0
        self.get_logger().info('Koordinat Takip Düğümü Başlatıldı!')

    def odom_callback(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

def main(args=None):
    rclpy.init(args=args)
    tracker = CoordinateTracker()
    
    executor_thread = threading.Thread(target=rclpy.spin, args=(tracker,), daemon=True)
    executor_thread.start()

    print("\n--- Koordinat Takip Ekranı ---")
    print("Anlık (X, Y) koordinatlarını görmek için ENTER tuşuna bas (Çıkış için Ctrl+C):\n")

    try:
        while rclpy.ok():
            input()
            print(f"--> Anlık Robot Koordinatları -> X: {tracker.x:.4f}, Y: {tracker.y:.4f}")
    except KeyboardInterrupt:
        pass

    tracker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
