class RobotState:
    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def update(self, lidar_distance):
        pass

## Pathfinding state til når der ikke er noget tæt på:
class PathfindingState(RobotState):
    def on_enter(self):
        print("entering Pathfinding State [1]")

    def update(self, lidar_distance):
        if lidar_distance <= 2 and lidar_distance > 0.5:
            return AvoidanceState()
        elif lidar_distance <= 0.5:
            return EmergencyState()

    def on_exit(self):
        print("Exiting Pathfinding State")

## Avoidance state så den kører omkring ting tættere end 2 meter:
class AvoidanceState(RobotState):
    def on_enter(self):
        print("Entering Avoidance State [2]")

    def update(self, lidar_distance):
        if lidar_distance > 2:
            return PathfindingState()
        elif lidar_distance <= 0.5:
            return EmergencyState()

    def on_exit(self):
        print("Exiting Avoidance State")
        
## Emergency state, så den stopper vis noget et tættere end 0.5 meter
class EmergencyState(RobotState):
    def on_enter(self):
        print("Entering Emergency State [3]")
        
    def update(self, lidar_distance):
        if lidar_distance <= 2 and lidar_distance > 0.5:
            return AvoidanceState()
        elif lidar_distance > 2:
            return PathfindingState()
        
    def on_exit(self):
        print("exiting Emergency State")

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

# Eksempel brug
robot = Robot()

# SKriv forskellige distancer ind herunder, så giver den dig en liste af hvordan den skifter states:
for lidar_distance in [3, 0.1, 2, 4]:
    robot.update(lidar_distance)
