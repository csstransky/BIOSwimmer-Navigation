import csv 

def get_csv_coordinate_tuples(file_path):
    # fixed_row_size of 3 is used for pathing, and a fixed_row_size of 2 is used for the cam target
    def get_csv_coordinate_tuple(row, fixed_row_size):
        # TODO: Is there a nicer way to do this?
        if fixed_row_size == 3:
            return float(row[0]), float(row[1]), float(row[2])
        elif fixed_row_size == 2: 
            return float(row[0]), float(row[1])
        elif fixed_row_size == 1:
            return float(row[0])
        else:
            print("ERROR: CSV FILE IS FORMATTED INCORRECTLY\n\n")

    coordinate_tuples = []
    with open(file_path, "r") as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')        
        fixed_row_size = len(csv_reader.__next__()) # get size and ignore the fields of the csv file
        for row in csv_reader: 
            coordinate_tuple = get_csv_coordinate_tuple(row, fixed_row_size)
            coordinate_tuples.append(coordinate_tuple) 
    return coordinate_tuples

class BIOSwimmer:
    def __init__(self, gps_file_path, target_file_path):
        self.path_coordinate_tuples = get_csv_coordinate_tuples(gps_file_path)
        # TODO: In the future, handle multiple camera target points instead of just 1
        self.camera_target_tuple = get_csv_coordinate_tuples(target_file_path)[0]
        self.x_acceleration = 0.0
        self.y_acceleration = 0.0
        self.z_acceleration = 0.0
        self.roll_rate = 0.0
        self.pitch_rate = 0.0
        self.yaw_rate = 0.0
        self.dvl_valid = False
        self.v_north = 0.0
        self.v_east = 0.0
        self.v_surface = 0.0
        self.compass_pitch = 0.0
        self.compass_direction = 0.0
        self.compass_roll = 0.0
        self.gps_sat_status = False
        self.gps_latitude = 0.0 
        self.gps_longitude = 0.0
        self.gps_speed_east = 0.0
        self.gps_speed_north = 0.0
        self.gps_altitude = 0.0 
        self.gps_num_satellites = 0.0
        self.gps_hdop = 0.0
        self.gps_bearing = 0.0 
        self.depth = 0.0
        self.tick_count = 0.0
        self.motor1_position = 0.0
        self.motor2_position = 0.0
        self.motor3_position = 0.0
        self.motion_state = 0.0
        self.time_stamp = 0

    def is_mission_complete(self):
        return self.path_coordinate_tuples == []

    def print(self):
        print("Longitude: \t", format(self.gps_longitude, '0.10f'),
            "\tLatitude: \t", format(self.gps_latitude, '0.10f'),
            "Depth: \t\t", format(self.depth, '0.6f'))
        print("vEast: \t\t", format(self.v_east, '0.6f'),
            "\tvNorth: \t", format(self.v_north, '0.6f'),
            "\tvSurface: \t", format(self.v_surface, '0.6f'))
        print("X Acc.: \t", format(self.x_acceleration, '0.6f'),
            "\tY Acc.: \t", format(self.y_acceleration, '0.6f'),
            "\tZ Acc.: \t", format(self.z_acceleration, '0.6f'))
        print("Tick Count: \t", self.tick_count)