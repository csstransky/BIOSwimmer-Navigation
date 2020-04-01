import re

# NOTE: This seems to be the maximum buffer from the BIOSwimmer, tweaking might need to be
# done in case the true maximum buffer length is different
BUFFER = 2048 

def update_bioswimmer(bioswimmer, command_columns):
    def update_imu_data(bioswimmer, command_columns):
        bioswimmer.x_acceleration = float(command_columns[1])
        bioswimmer.y_acceleration = float(command_columns[2])
        bioswimmer.z_acceleration = float(command_columns[3])
        bioswimmer.roll_rate = float(command_columns[4])
        bioswimmer.pitch_rate = float(command_columns[5])
        bioswimmer.yaw_rate = float(command_columns[6])
        return

    def update_dvl_data(bioswimmer, command_columns):
        bioswimmer.dvl_valid = bool(command_columns[1])
        bioswimmer.v_north = float(command_columns[2])
        bioswimmer.v_east = float(command_columns[3])
        bioswimmer.v_surface = float(command_columns[4])
        bioswimmer.dvl_bottom_dist = float(command_columns[5])
        bioswimmer.dvl_water_temp = float(command_columns[6])
        return

    def update_compass_data(bioswimmer, command_columns):
        bioswimmer.compass_pitch = float(command_columns[1])
        bioswimmer.compass_direction = float(command_columns[2])
        bioswimmer.compass_roll = float(command_columns[3])
        return

    def update_gps_data(bioswimmer, command_columns):
        bioswimmer.gps_sat_status = bool(command_columns[1])
        bioswimmer.gps_latitude = float(command_columns[2]) if "NaN" not in command_columns[2] else 0 
        bioswimmer.gps_longitude = float(command_columns[3]) if "NaN" not in command_columns[3] else 0
        bioswimmer.gps_speed_east = float(command_columns[4])
        bioswimmer.gps_speed_north = float(command_columns[5])
        bioswimmer.gps_altitude = float(command_columns[6]) if "NaN" not in command_columns[6] else 0
        bioswimmer.gps_num_satellites = float(command_columns[7])
        bioswimmer.gps_hdop = float(command_columns[8])
        # TODO: Find out what the hell is missing in this command
        bioswimmer.gps_bearing = float(command_columns[9]) if len(command_columns) <= 8 else 0
        return

    def update_depth_data(bioswimmer, command_columns):
        bioswimmer.depth = float(command_columns[1])
        return

    def update_system_data(bioswimmer, command_columns):
        bioswimmer.tick_count = float(command_columns[1])
        return

    def update_skip_waypoint_data(bioswimmer, command_columns):
        # No data for this command
        return

    def update_actuators_data(bioswimmer, command_columns):
        bioswimmer.motor1_position = float(command_columns[1])
        bioswimmer.motor2_position = float(command_columns[2])
        bioswimmer.motor3_position = float(command_columns[3])
        bioswimmer.motion_state = float(command_columns[4])
        bioswimmer.time_stamp = int(command_columns[5])
        return

    def wrong_command_error(bioswimmer, command_columns):
        print("**********INVALID COMMAND**********")
        print(command_columns)
        print("***********************************")
        return

    command = command_columns[0]
    # Awkward way to do a switch case in Python
    switcher = {
        '01': update_imu_data,
        '03': update_dvl_data,
        '04': update_compass_data,
        '05': update_gps_data,
        '06': update_depth_data,
        '07': update_system_data,
        '09': update_skip_waypoint_data,
        '10': update_actuators_data
    }
    switcher.get(command, wrong_command_error)(bioswimmer, command_columns)
    return

def read_bioswimmer_data(bioswimmer, serial_data):
    def tokenize_commands(serial_data):
        return re.findall(r'\{([^}]+)', serial_data)

    def tokenize_command_columns(command):
        return re.split(r'\W+', command)

    commands = tokenize_commands(serial_data)

    for command in commands:
        command_columns = tokenize_command_columns(command)
        update_bioswimmer(bioswimmer, command_columns)
    return

def update_bioswimmer_data_from_client(bioswimmer, client):
    response = client.recv(BUFFER).decode('utf-8')
    read_bioswimmer_data(bioswimmer, response)
