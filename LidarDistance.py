class RobotState:
    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self, lidar_distance):
        pass

class PathfindingState(RobotState):
    def on_enter(self):
        print("Entering Pathfinding State")

    def update(self, lidar_distance):
        if lidar_distance < 2:
            return AvoidanceState()
        # Pathfinding logic goes here

    def on_exit(self):
        print("Exiting Pathfinding State")

class AvoidanceState(RobotState):
    def on_enter(self):
        print("Entering Avoidance State")

    def update(self, lidar_distance):
        if lidar_distance >= 2:
            return PathfindingState()
        # Avoidance logic goes here

    def on_exit(self):
        print("Exiting Avoidance State")

class Robot:
    def __init__(self):
        self.state = PathfindingState()
        self.state.on_enter()

    def update(self, lidar_distance):
        new_state = self.state.update(lidar_distance)
        if new_state is not None:
            self.state.on_exit()
            self.state = new_state
            self.state.on_enter()

# Example usage
robot = Robot()
# Simulate different LiDAR distances
for lidar_distance in [3, 1.5, 3]:
    robot.update(lidar_distance)
