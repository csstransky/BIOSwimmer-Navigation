# NOTE: Assuming an accerlation of 1 m/s^2 is ideal, may need to be lowered in the future to
# keep up with the BIOSwimmer's slow rate of change in the rotator
SPEED_RATE = 1

# TODO: This math is completely theoretical and untested, this will need to be edited and tested 
# in the future
# Assumed North and East are positive values (South and West are negative)
def get_new_velocity_double(destination_location, 
    current_location, current_velocity, current_accerlation):

    ideal_velocity = SPEED_RATE * (destination_location - current_location)
    needed_velocity = ideal_velocity - current_velocity
    needed_acceleration = SPEED_RATE - current_velocity
    return needed_velocity + needed_acceleration