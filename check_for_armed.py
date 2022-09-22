# Needs testing to verify that this is actually working as expected, at this time it appears to work.
# Cycles through tracks in project and returns true if it finds any tracks with record armed turned on, otherwise returns false

def fn_bits(n):
    while n:
        b = n & (~n+1)
        yield b
        n ^= b

def track_states(trck):
    status = {
        'hide from mcp': False,
        'hide from tcp': False,
        'rec monitoring auto': False,
        'rec monitoring on': False,
        'rec armed': False,
        'SIPd': False,
        'soloed': False,
        'muted': False,
        'has fx enabled': False,
        'selected': False,
        'folder': False
    }
    bits = fn_bits(trck)
    for bit in bits:
        if bit == 1:
            status['folder'] = True
        elif bit == 2:
            status['selected'] = True
        elif bit == 4:
            status['has fx enabled'] = True
        elif bit == 8:
            status['muted'] = True
        elif bit == 16:
            status['soloed'] = True
        elif bit == 32:
            status['SIPd'] = True
        elif bit == 64:
            status['rec armed'] = True
        elif bit == 128:
            status['rec monitoring on'] = True
        elif bit == 256:
            status['rec monitoring auto'] = True
        elif bit == 512:
            status['hide from tcp'] = True
        elif bit == 1024:
            status['hide from mcp'] = True
    return status

def check_for_armed():
    track_count = RPR_CountTracks(0)
    for x in range(0, track_count):
      tr = RPR_GetTrack(0, x)
      tr_name, track, track_state = RPR_GetTrackState(tr, 64)
      tatus = track_states(track_state)
      if status['rec armed'] or status['rec monitoring on']:
        return True
    return False
    
    
check_for_armed()
