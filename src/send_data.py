import json
import src.calc_velocity as calc_velocity

# This buffer allows for the BIOSwimmer to get within an acceptable distance of 
# the GPS coordinates to consider that waypoint "completed"
# NOTE: Measurement is in decimal degrees 
# TODO: Testing will need to be done to find the best buffer to complete a destination point
GPS_BUFFER = 0.000003
DECIMAL_DEGREES_TO_METERS = 111319.5
# This buffer allows for the BIOSwimmer to reach an acceptable depth for it to be 
# considered "complete"
# NOTE: Measurement in feet
# TODO: Also an assumption based on the documentation and test data, need confirmation
# TODO: Testing will need to be done to find the best buffer for depth
DEPTH_BUFFER = 2
FEET_TO_METERS = 1 / 3.2808

def get_bioswimmer_velocity_byte_stream(bioswimmer):
    destination_longitude, destination_latitude, destination_depth = bioswimmer.path_coordinate_tuples[0]

    # NOTE: I'm assuming that y_acceleration is north/south, x_acceleration is east/west, etc.
    north_velocity = calc_velocity.get_new_velocity_double(destination_latitude, 
        bioswimmer.gps_latitude, bioswimmer.v_north, bioswimmer.y_acceleration)
    east_velocity = calc_velocity.get_new_velocity_double(destination_longitude, 
        bioswimmer.gps_longitude, bioswimmer.v_east, bioswimmer.x_acceleration)
    depth_velocity = calc_velocity.get_new_velocity_double(destination_depth,
        bioswimmer.depth, bioswimmer.v_surface, bioswimmer.z_acceleration)
    
    move_map = {
        "vNorth" : format(north_velocity * DECIMAL_DEGREES_TO_METERS, '0.6f'),
        "vEast" : format(east_velocity * DECIMAL_DEGREES_TO_METERS, '0.6f'),
        "depth" : format(depth_velocity * FEET_TO_METERS, '0.6f')
    }
    move_json = json.dumps(move_map)
    # NOTE: It seems that the BIOSwimmer does not want a typical JSON, and needs all the quotes
    # removed. Example: 
    # Correct: {vNorth: 3.0, vEast: 3.0, depth: -3.0} 
    # Wrong: {"vNorth": 3.0, "vEast": 3.0, "depth": -3.0}
    move_data = move_json.replace("\"", "")
    move_byte_stream = move_data.encode()
    return move_byte_stream

def is_current_gps_coordinate_complete(bioswimmer):
    destination_longitude, destination_latitude, destination_depth = bioswimmer.path_coordinate_tuples[0]
    return (abs(destination_latitude - bioswimmer.gps_latitude) <= GPS_BUFFER 
        and abs(destination_longitude - bioswimmer.gps_longitude) <= GPS_BUFFER
        and abs(destination_depth - bioswimmer.depth) <= DEPTH_BUFFER)

def send_velocity_data_to_bioswimmer(bioswimmer, client):
    move_byte_stream = get_bioswimmer_velocity_byte_stream(bioswimmer)
    client.send(move_byte_stream)
    return move_byte_stream
