# Needs testing to verify that this is actually working as expected, at this time it appears to work.
# Cycles through tracks in project and returns true if it finds any tracks with record armed turned on, otherwise returns false

def check_for_armed():
    track_count = RPR_CountTracks(0)
    for x in range(0, track_count):
      tr = RPR_GetTrack(0, x)
      tr_name, track, track_state = RPR_GetTrackState(tr, 64)
      if track_state == 192 or track_state == 194:
        return True
    return False
    
    
check_for_armed()
