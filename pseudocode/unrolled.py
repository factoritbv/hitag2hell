from naive import *
def fill_layer(a=None, b=None, filt_mask=0x5806b4a2d16c):
  for i0 in range(1<<bits[0]):
    state0 = expand(masks[0], i0)
    if testing and (state0 & filt_mask) != (test_states[0] & filt_mask):
      continue
    if f20(state0) != keystream[0]:
      continue
    for i1 in range(1<<(bits[1]+1)): # guess LFSR output bit 0
      state1 = (state0>>1) | expand(masks[1]|(1<<47), i1)
      if testing and (state1 & filt_mask) != (test_states[1] & filt_mask):
        continue
      if f20(state1) != keystream[1]:
        continue
      for i2 in range(1<<(bits[2]+1)): # guess LFSR output bit 1
        state2 = (state1>>1) | expand(masks[2]|(1<<47), i2)
        if testing and (state2 & filt_mask) != (test_states[2] & filt_mask):
          continue
        if f20(state2) != keystream[2]:
          continue
        for i3 in range(1<<bits[3]):
          state3 = lfsr(state2) | expand(masks[3], i3)
          if testing and (state3 & filt_mask) != (test_states[3] & filt_mask):
            continue
          if f20(state3) != keystream[3]:
            continue
          for i4 in range(1<<bits[4]):
            state4 = lfsr(state3) | expand(masks[4], i4)
            if testing and (state4 & filt_mask) != (test_states[4] & filt_mask):
              continue
            if f20(state4) != keystream[4]:
              continue
            for i5 in range(1<<bits[5]):
              state5 = lfsr(state4) | expand(masks[5], i5)
              if testing and (state5 & filt_mask) != (test_states[5] & filt_mask):
                continue
              if f20(state5) != keystream[5]:
                continue
              for i6 in range(1<<bits[6]):
                state6 = lfsr(state5) | expand(masks[6], i6)
                if testing and (state6 & filt_mask) != (test_states[6] & filt_mask):
                  continue
                if f20(state6) != keystream[6]:
                  continue
                for i7 in range(1<<bits[7]):
                  state7 = lfsr(state6) | expand(masks[7], i7)
                  if testing and (state7 & filt_mask) != (test_states[7] & filt_mask):
                    continue
                  if f20(state7) != keystream[7]:
                    continue
                  for i8 in range(1<<bits[8]):
                    state8 = lfsr(state7) | expand(masks[8], i8)
                    if testing and (state8 & filt_mask) != (test_states[8] & filt_mask):
                      continue
                    if f20(state8) != keystream[8]:
                      continue
                    test(lfsr(state8))

if __name__ == "__main__":
    testing = True
    fill_layer()

