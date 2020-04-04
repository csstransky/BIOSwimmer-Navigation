import math

# NOTE: Assuming an accerlation of 1 m/s^2 is ideal, may need to be lowered in the future to
# keep up with the BIOSwimmer's slow rate of change in the rotator
SPEED_CONSTANT = 1

def sign(number):
    return math.copysign(1, number)

# Algorithm that will keep a constant
# We notate the sign of a variable (+1 or -1) with this: (+/-x) = x / |x|
#   a = |C * sign(v0) * (3/2) * sqrt(|v0|) - a0|
#   v = C * sign(d) * |d| ^ (3/2) - a * v0
# TODO: This math is completely theoretical and untested, this will need to be edited and tested 
# in the future
# Assumed North and East are positive values (South and West are negative)
def get_new_velocity_double(destination_location, 
    current_location, current_velocity, current_accerlation):

    ideal_accerlation = SPEED_CONSTANT * sign(current_velocity) * (3/2) * math.sqrt(abs(current_velocity))
    needed_acceleration = abs(ideal_accerlation - current_accerlation)
    needed_velocity = needed_acceleration * current_velocity

    distance = destination_location - current_location
    ideal_velocity = SPEED_CONSTANT * sign(distance) * abs(distance) ** (3/2)

    return ideal_velocity - needed_velocity

# Simple algorithm that will keep acceleration at a rate of 1, and velocity at a rate of distance
#   a = |C * 1 - a0|
#   v = C * d - a * v0
def get_simple_new_velocity_double(destination_location, 
    current_location, current_velocity, current_accerlation):

    ideal_accerlation = SPEED_CONSTANT * 1
    needed_acceleration = abs(ideal_accerlation - current_accerlation)
    needed_velocity = needed_acceleration * current_velocity

    distance = destination_location - current_location
    ideal_velocity = SPEED_CONSTANT * distance

    return ideal_velocity - needed_velocity