import src.read_data as read
import src.send_data as send

def get_data_string(midbrain):
    # The addition sign must be added to our strings
    def double_to_string(double_val):
        string_val = str(double_val)
        if double_val > 0:
            string_val = "+" + string_val
        elif double_val == 0: 
            string_val = "+00000" # edge case
        return string_val

    def get_imu_string(x_acceleration, y_acceleration, z_acceleration):
        imu_string = "{01"
        imu_string += double_to_string(x_acceleration)
        imu_string += double_to_string(y_acceleration)
        imu_string += double_to_string(z_acceleration)
        imu_string += "+00000+00000+00000}"
        return imu_string

    def get_dvl_string(v_north, v_east, v_surface):
        dvl_string = "{03+00001"
        dvl_string += double_to_string(v_north)
        dvl_string += double_to_string(v_east)
        dvl_string += double_to_string(v_surface)
        dvl_string += "+00000+231}"
        return dvl_string

    def get_compass_string(compass_direction):
        return "{04+00383" + double_to_string(compass_direction) + "-00107}"

    def get_gps_string(gps_latitude, gps_longitude):
        gps_string = "{05+00001"
        gps_string += double_to_string(gps_latitude)
        gps_string += double_to_string(gps_longitude)
        gps_string += "+00000+00000+00NaN-1+00000}"
        return gps_string

    def get_depth_string(depth):
        return "{06" + double_to_string(depth) + "}"

    data_string = get_imu_string(midbrain.x_acceleration, midbrain.y_acceleration, midbrain.z_acceleration)
    data_string += get_dvl_string(midbrain.v_north, midbrain.v_east, midbrain.v_surface)
    data_string += get_compass_string(midbrain.compass_direction)
    data_string += get_gps_string(midbrain.gps_latitude, midbrain.gps_longitude)
    data_string += get_depth_string(midbrain.depth)
    return data_string

# Example of data sent: "{vNorth: 0.43, vEast: 1.56, depth: 0.56}"
def set_data_string(midbrain, data):
    data = data[1:-1]
    velocities = data.split(", ")
    for velocity in velocities:
        direction, speed = velocity.split(": ")
        if direction == "vNorth":
            midbrain.v_north = float(speed)
        elif direction == "vEast":
            midbrain.v_east = float(speed)
        elif direction == "depth":
            midbrain.v_surface = float(speed)


def update_bioswimmer_data_from_client(bioswimmer, midbrain):
    response = get_data_string(midbrain)
    read.read_bioswimmer_data(bioswimmer, response)

def send_velocity_data_to_bioswimmer(bioswimmer, midbrain):
    move_byte_stream = send.get_bioswimmer_velocity_byte_stream(bioswimmer)
    set_data_string(midbrain, move_byte_stream.decode())

    if send.is_current_gps_coordinate_complete(bioswimmer):
        print("************************************************************")
        print("Completed current coordinate: ", bioswimmer.path_coordinate_tuples[0])
        print("************************************************************")
        del bioswimmer.path_coordinate_tuples[0]
    return move_byte_stream