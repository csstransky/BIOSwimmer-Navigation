


# The addition sign must be added to our strings
def double_to_string(double):
    return "+" + str(double) if double > 0 else str(double)

def get_imu_string(x_accerlation, y_accerlation, z_accerlation):
    imu_string = "{01"
    imu_string += double_to_string(x_accerlation)
    imu_string += double_to_string(y_accerlation)
    imu_string += double_to_string(z_accerlation)
    imu_string += "+00000+00000+00000}"
    return imu_string

def get_dvl_string(v_north, v_east, v_surface):
    dvl_string = "{03+00001"
    dvl_string += double_to_string(v_north)
    dvl_string += double_to_string(v_east)
    dvl_string += double_to_string(v_surface)
    dvl_string += "+00000+231}"
    return dvl_string

def get_gps_string(gps_latitude, gps_longitude):
    gps_string = "{05+00001"
    gps_string += double_to_string(gps_latitude)
    gps_string += double_to_string(gps_longitude)
    gps_string += "+00000+00000+00NaN+0+00000}"

def get_depth_string(depth):
    return "{06" + double_to_string(depth) + "}"

