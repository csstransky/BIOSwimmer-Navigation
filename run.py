import read_data as read
import bioswimmer as bioswimmer

string1 = "{01+00000+00000+00000-00000+00000+00000}"
string2 = "{04+00383+24888-00107}{06-00126}{03+00001+00000+00000+00000+00000+231}{05+00000+000000NaN+000000NaN-00000+00000+00NaN+0+00000}{07+08582}{10+43+00+00+1+09407}"
bioswimmer = bioswimmer.BIOSwimmer()
read.read_bioswimmer_data(bioswimmer, string1)
read.read_bioswimmer_data(bioswimmer, string2)