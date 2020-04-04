import src.bioswimmer as bswim
import simulation.src.network_data as data
import src.calc_velocity as calc
import math

class MidBrain:
    def __init__(self, points_file_path, angles_file_path):
        self.path_coordinate_tuples = bswim.get_csv_coordinate_tuples(points_file_path)
        self.compass_angle_list = bswim.get_csv_coordinate_tuples(angles_file_path)
        self.x_acceleration = 0.0
        self.y_acceleration = 0.0
        self.z_acceleration = 0.0
        self.v_north = 0.0
        self.v_east = 0.0
        self.v_surface = 0.0
        self.compass_direction = 0.0
        self.gps_latitude = 0.0 
        self.gps_longitude = 0.0
        self.depth = 0.0
        self.time_stamp = 0

    def get_mid_brain_data(self):
        data.get_data_string(self)

    def set_mid_brain_data(self, data):
        data.set_data_string(self, data)
        self.set_acceleration()

    def set_acceleration(self):
        def get_ideal_acceleration(current_velocity):
            return calc.SPEED_CONSTANT * calc.sign(current_velocity) * (3/2) * math.sqrt(abs(current_velocity))
            
        self.y_acceleration = get_ideal_acceleration(self.v_north)
        self.x_acceleration = get_ideal_acceleration(self.v_east)
        self.z_acceleration = get_ideal_acceleration(self.v_surface)
        
    def set_next_point(self):
        longitude, latitude, depth = self.path_coordinate_tuples[0]
        compass_angle = self.compass_angle_list[0]
        self.gps_latitude = latitude
        self.gps_longitude = longitude
        self.depth = depth
        self.compass_direction = compass_angle
        self.time_stamp += 1
        del self.path_coordinate_tuples[0]
        del self.compass_angle_list[0]