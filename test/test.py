import src
import src.read_data as read
import src.send_data as send
import src.bioswimmer as bswim

def test_functions():
    string1 = "{01+00002+00002+00002-00000+00000+00000}"
    string2 = "{04+00383+24888-00107}{06-00126}{03+00001+00003+00001+00002+00000+231}{05+00000+000000NaN+000000NaN-00000+00000+00NaN+0+00000}{07+08582}{10+43+00+00+1+09407}"
    bioswimmer = bswim.BIOSwimmer("data/gps_data.csv", "data/camera_target.csv")
    print("---------==========================---------------")
    print(bioswimmer.path_coordinate_tuples)
    print("---------==========================---------------")
    print(vars(bioswimmer))
    read.read_bioswimmer_data(bioswimmer, string1)
    read.read_bioswimmer_data(bioswimmer, string2)
    print("\n", vars(bioswimmer))

    if send.is_current_gps_coordinate_complete(bioswimmer):
        print("************************************************************")
        print("Completed current coordinate: ", bioswimmer.path_coordinate_tuples[0])
        print("************************************************************")
        del bioswimmer.path_coordinate_tuples[0]
    move_byte_stream = send.get_bioswimmer_velocity_byte_stream(bioswimmer)
    print(move_byte_stream, "\n")
    print(bioswimmer.is_mission_complete())
