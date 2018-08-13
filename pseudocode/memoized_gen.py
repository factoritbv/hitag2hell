from naive import *
def fill_layer(a=None, b=None, filt_mask=0x5806b4a2d16c):
  state = [0 for _ in range(48+32)]
  for i0 in range(1<<bits[0]):
    state[2] = bool((i0 & 0x1))
    state[3] = bool((i0 & 0x2))
    state[5] = bool((i0 & 0x4))
    state[6] = bool((i0 & 0x8))
    state[8] = bool((i0 & 0x10))
    state[12] = bool((i0 & 0x20))
    state[14] = bool((i0 & 0x40))
    state[15] = bool((i0 & 0x80))
    state[17] = bool((i0 & 0x100))
    state[21] = bool((i0 & 0x200))
    state[23] = bool((i0 & 0x400))
    state[26] = bool((i0 & 0x800))
    state[28] = bool((i0 & 0x1000))
    state[29] = bool((i0 & 0x2000))
    state[31] = bool((i0 & 0x4000))
    state[33] = bool((i0 & 0x8000))
    state[34] = bool((i0 & 0x10000))
    state[43] = bool((i0 & 0x20000))
    state[44] = bool((i0 & 0x40000))
    state[46] = bool((i0 & 0x80000))
    # 0x5806b4a2d16c
    if (unbitslice(state,0) & filt_mask) != (test_states[0] & filt_mask):
      continue
    print 0, hex(unbitslice(state, 0))
    filter0_0 = f20a_bs(state[2],state[3],state[5],state[6])
    filter0_1 = f20b_bs(state[8],state[12],state[14],state[15])
    filter0_2 = f20b_bs(state[17],state[21],state[23],state[26])
    filter0_3 = f20b_bs(state[28],state[29],state[31],state[33])
    filter0_4 = f20a_bs(state[34],state[43],state[44],state[46])
    filter0 = f20c_bs(filter0_0, filter0_1, filter0_2, filter0_3, filter0_4)
    results0 = filter0 == keystream[0]
    if not results0:
      continue
    for i1 in range(1<<(bits[1]+1)):
      state[4] = bool((i1 & 0x1))
      state[7] = bool((i1 & 0x2))
      state[9] = bool((i1 & 0x4))
      state[13] = bool((i1 & 0x8))
      state[16] = bool((i1 & 0x10))
      state[18] = bool((i1 & 0x20))
      state[22] = bool((i1 & 0x40))
      state[24] = bool((i1 & 0x80))
      state[27] = bool((i1 & 0x100))
      state[30] = bool((i1 & 0x200))
      state[32] = bool((i1 & 0x400))
      state[35] = bool((i1 & 0x800))
      state[45] = bool((i1 & 0x1000))
      state[47] = bool((i1 & 0x2000))
      state[48] = bool((i1 & 0x4000)) # guess lfsr output 0
      # 0xfc07fef3f9fe
      filter1_0 = f20a_bs(state[3],state[4],state[6],state[7])
      filter1_1 = f20b_bs(state[9],state[13],state[15],state[16])
      filter1_2 = f20b_bs(state[18],state[22],state[24],state[27])
      filter1_3 = f20b_bs(state[29],state[30],state[32],state[34])
      filter1_4 = f20a_bs(state[35],state[44],state[45],state[47])
      filter2_0 = f20a_bs(state[4],state[5],state[7],state[8])
      filter2_3 = f20b_bs(state[30],state[31],state[33],state[35])
      filter3_0 = f20a_bs(state[5],state[6],state[8],state[9])
      filter5_2 = f20b_bs(state[22],state[26],state[28],state[31])
      filter6_2 = f20b_bs(state[23],state[27],state[29],state[32])
      filter7_2 = f20b_bs(state[24],state[28],state[30],state[33])
      filter9_1 = f20b_bs(state[17],state[21],state[23],state[24])
      filter9_2 = f20b_bs(state[26],state[30],state[32],state[35])
      filter10_0 = f20a_bs(state[12],state[13],state[15],state[16])
      filter11_0 = f20a_bs(state[13],state[14],state[16],state[17])
      filter12_0 = f20a_bs(state[14],state[15],state[17],state[18])
      filter14_1 = f20b_bs(state[22],state[26],state[28],state[29])
      filter15_1 = f20b_bs(state[23],state[27],state[29],state[30])
      filter15_3 = f20b_bs(state[43],state[44],state[46],state[48])
      filter16_1 = f20b_bs(state[24],state[28],state[30],state[31])
      filter18_1 = f20b_bs(state[26],state[30],state[32],state[33])
      filter19_1 = f20b_bs(state[27],state[31],state[33],state[34])
      filter20_1 = f20b_bs(state[28],state[32],state[34],state[35])
      filter21_0 = f20a_bs(state[23],state[24],state[26],state[27])
      filter24_0 = f20a_bs(state[26],state[27],state[29],state[30])
      filter25_0 = f20a_bs(state[27],state[28],state[30],state[31])
      filter26_0 = f20a_bs(state[28],state[29],state[31],state[32])
      filter1 = f20c_bs(filter1_0, filter1_1, filter1_2, filter1_3, filter1_4)
      results1 = filter1 == keystream[1]
      if not results1:
        continue
      for i2 in range(1<<(bits[2]+1)):
        state[10] = bool((i2 & 0x1))
        state[19] = bool((i2 & 0x2))
        state[25] = bool((i2 & 0x4))
        state[36] = bool((i2 & 0x8))
        state[49] = bool((i2 & 0x10)) # guess lfsr output 1
        # 0xfe07fffbfdff
        state[50] = lfsr_bs(state,2)
        filter2_1 = f20b_bs(state[10],state[14],state[16],state[17])
        filter2_2 = f20b_bs(state[19],state[23],state[25],state[28])
        filter2_4 = f20a_bs(state[36],state[45],state[46],state[48])
        filter3_3 = f20b_bs(state[31],state[32],state[34],state[36])
        filter4_0 = f20a_bs(state[6],state[7],state[9],state[10])
        filter4_1 = f20b_bs(state[12],state[16],state[18],state[19])
        filter4_2 = f20b_bs(state[21],state[25],state[27],state[30])
        filter7_0 = f20a_bs(state[9],state[10],state[12],state[13])
        filter7_1 = f20b_bs(state[15],state[19],state[21],state[22])
        filter8_2 = f20b_bs(state[25],state[29],state[31],state[34])
        filter10_1 = f20b_bs(state[18],state[22],state[24],state[25])
        filter10_2 = f20b_bs(state[27],state[31],state[33],state[36])
        filter11_1 = f20b_bs(state[19],state[23],state[25],state[26])
        filter13_0 = f20a_bs(state[15],state[16],state[18],state[19])
        filter13_1 = f20b_bs(state[21],state[25],state[27],state[28])
        filter16_0 = f20a_bs(state[18],state[19],state[21],state[22])
        filter16_3 = f20b_bs(state[44],state[45],state[47],state[49])
        filter17_1 = f20b_bs(state[25],state[29],state[31],state[32])
        filter17_3 = f20b_bs(state[45],state[46],state[48],state[50])
        filter19_0 = f20a_bs(state[21],state[22],state[24],state[25])
        filter20_0 = f20a_bs(state[22],state[23],state[25],state[26])
        filter21_1 = f20b_bs(state[29],state[33],state[35],state[36])
        filter22_0 = f20a_bs(state[24],state[25],state[27],state[28])
        filter23_0 = f20a_bs(state[25],state[26],state[28],state[29])
        filter2 = f20c_bs(filter2_0, filter2_1, filter2_2, filter2_3, filter2_4)
        results2 = filter2 == keystream[2]
        if not results2:
          continue
        for i3 in range(1<<bits[3]):
          state[11] = bool((i3 & 0x1))
          state[20] = bool((i3 & 0x2))
          state[37] = bool((i3 & 0x4))
          # 0xff07ffffffff
          state[51] = lfsr_bs(state,3)
          state[52] = lfsr_bs(state,4)
          state[53] = lfsr_bs(state,5)
          state[54] = lfsr_bs(state,6)
          state[55] = lfsr_bs(state,7)
          filter3_1 = f20b_bs(state[11],state[15],state[17],state[18])
          filter3_2 = f20b_bs(state[20],state[24],state[26],state[29])
          filter3_4 = f20a_bs(state[37],state[46],state[47],state[49])
          filter4_3 = f20b_bs(state[32],state[33],state[35],state[37])
          filter5_0 = f20a_bs(state[7],state[8],state[10],state[11])
          filter5_1 = f20b_bs(state[13],state[17],state[19],state[20])
          filter6_0 = f20a_bs(state[8],state[9],state[11],state[12])
          filter6_1 = f20b_bs(state[14],state[18],state[20],state[21])
          filter8_0 = f20a_bs(state[10],state[11],state[13],state[14])
          filter8_1 = f20b_bs(state[16],state[20],state[22],state[23])
          filter9_0 = f20a_bs(state[11],state[12],state[14],state[15])
          filter9_4 = f20a_bs(state[43],state[52],state[53],state[55])
          filter11_2 = f20b_bs(state[28],state[32],state[34],state[37])
          filter12_1 = f20b_bs(state[20],state[24],state[26],state[27])
          filter14_0 = f20a_bs(state[16],state[17],state[19],state[20])
          filter15_0 = f20a_bs(state[17],state[18],state[20],state[21])
          filter17_0 = f20a_bs(state[19],state[20],state[22],state[23])
          filter18_0 = f20a_bs(state[20],state[21],state[23],state[24])
          filter18_3 = f20b_bs(state[46],state[47],state[49],state[51])
          filter19_3 = f20b_bs(state[47],state[48],state[50],state[52])
          filter20_3 = f20b_bs(state[48],state[49],state[51],state[53])
          filter21_3 = f20b_bs(state[49],state[50],state[52],state[54])
          filter22_1 = f20b_bs(state[30],state[34],state[36],state[37])
          filter22_3 = f20b_bs(state[50],state[51],state[53],state[55])
          filter26_2 = f20b_bs(state[43],state[47],state[49],state[52])
          filter3 = f20c_bs(filter3_0, filter3_1, filter3_2, filter3_3, filter3_4)
          results3 = filter3 == keystream[3]
          if not results3:
            continue
          for i4 in range(1<<bits[4]):
            state[38] = bool((i4 & 0x1))
            # 0xff87ffffffff
            filter4_4 = f20a_bs(state[38],state[47],state[48],state[50])
            filter5_3 = f20b_bs(state[33],state[34],state[36],state[38])
            filter12_2 = f20b_bs(state[29],state[33],state[35],state[38])
            filter23_1 = f20b_bs(state[31],state[35],state[37],state[38])
            filter4 = f20c_bs(filter4_0, filter4_1, filter4_2, filter4_3, filter4_4)
            results4 = filter4 == keystream[4]
            if not results4:
              continue
            for i5 in range(1<<bits[5]):
              state[39] = bool((i5 & 0x1))
              # 0xffc7ffffffff
              filter5_4 = f20a_bs(state[39],state[48],state[49],state[51])
              filter6_3 = f20b_bs(state[34],state[35],state[37],state[39])
              filter13_2 = f20b_bs(state[30],state[34],state[36],state[39])
              filter22_2 = f20b_bs(state[39],state[43],state[45],state[48])
              filter24_1 = f20b_bs(state[32],state[36],state[38],state[39])
              filter5 = f20c_bs(filter5_0, filter5_1, filter5_2, filter5_3, filter5_4)
              results5 = filter5 == keystream[5]
              if not results5:
                continue
              for i6 in range(1<<bits[6]):
                state[40] = bool((i6 & 0x1))
                # 0xffe7ffffffff
                filter6_4 = f20a_bs(state[40],state[49],state[50],state[52])
                filter7_3 = f20b_bs(state[35],state[36],state[38],state[40])
                filter14_2 = f20b_bs(state[31],state[35],state[37],state[40])
                filter17_2 = f20b_bs(state[34],state[38],state[40],state[43])
                filter23_2 = f20b_bs(state[40],state[44],state[46],state[49])
                filter25_1 = f20b_bs(state[33],state[37],state[39],state[40])
                filter6 = f20c_bs(filter6_0, filter6_1, filter6_2, filter6_3, filter6_4)
                results6 = filter6 == keystream[6]
                if not results6:
                  continue
                for i7 in range(1<<bits[7]):
                  state[41] = bool((i7 & 0x1))
                  # 0xfff7ffffffff
                  filter7_4 = f20a_bs(state[41],state[50],state[51],state[53])
                  filter8_3 = f20b_bs(state[36],state[37],state[39],state[41])
                  filter10_3 = f20b_bs(state[38],state[39],state[41],state[43])
                  filter12_3 = f20b_bs(state[40],state[41],state[43],state[45])
                  filter15_2 = f20b_bs(state[32],state[36],state[38],state[41])
                  filter18_2 = f20b_bs(state[35],state[39],state[41],state[44])
                  filter20_2 = f20b_bs(state[37],state[41],state[43],state[46])
                  filter24_2 = f20b_bs(state[41],state[45],state[47],state[50])
                  filter26_1 = f20b_bs(state[34],state[38],state[40],state[41])
                  filter7 = f20c_bs(filter7_0, filter7_1, filter7_2, filter7_3, filter7_4)
                  results7 = filter7 == keystream[7]
                  if not results7:
                    continue
                  for i8 in range(1<<bits[8]):
                    state[42] = bool((i8 & 0x1))
                    # 0xffffffffffff
                    filter8_4 = f20a_bs(state[42],state[51],state[52],state[54])
                    filter9_3 = f20b_bs(state[37],state[38],state[40],state[42])
                    filter11_3 = f20b_bs(state[39],state[40],state[42],state[44])
                    filter13_3 = f20b_bs(state[41],state[42],state[44],state[46])
                    filter14_3 = f20b_bs(state[42],state[43],state[45],state[47])
                    filter16_2 = f20b_bs(state[33],state[37],state[39],state[42])
                    filter19_2 = f20b_bs(state[36],state[40],state[42],state[45])
                    filter21_2 = f20b_bs(state[38],state[42],state[44],state[47])
                    filter25_2 = f20b_bs(state[42],state[46],state[48],state[51])
                    filter9 = f20c_bs(filter9_0, filter9_1, filter9_2, filter9_3, filter9_4)
                    results9 = filter9 == keystream[9]
                    if not results9:
                      continue
                    state[56] = lfsr_bs(state, 8)
                    filter10_4 = f20a_bs(state[44],state[53],state[54],state[56])
                    filter10 = f20c_bs(filter10_0, filter10_1, filter10_2, filter10_3, filter10_4)
                    results10 = filter10 == keystream[10]
                    if not results10:
                      continue
                    state[57] = lfsr_bs(state, 9)
                    filter11_4 = f20a_bs(state[45],state[54],state[55],state[57])
                    filter11 = f20c_bs(filter11_0, filter11_1, filter11_2, filter11_3, filter11_4)
                    results11 = filter11 == keystream[11]
                    if not results11:
                      continue
                    state[58] = lfsr_bs(state, 10)
                    filter12_4 = f20a_bs(state[46],state[55],state[56],state[58])
                    filter12 = f20c_bs(filter12_0, filter12_1, filter12_2, filter12_3, filter12_4)
                    results12 = filter12 == keystream[12]
                    if not results12:
                      continue
                    state[59] = lfsr_bs(state, 11)
                    filter13_4 = f20a_bs(state[47],state[56],state[57],state[59])
                    filter13 = f20c_bs(filter13_0, filter13_1, filter13_2, filter13_3, filter13_4)
                    results13 = filter13 == keystream[13]
                    if not results13:
                      continue
                    state[60] = lfsr_bs(state, 12)
                    filter14_4 = f20a_bs(state[48],state[57],state[58],state[60])
                    filter14 = f20c_bs(filter14_0, filter14_1, filter14_2, filter14_3, filter14_4)
                    results14 = filter14 == keystream[14]
                    if not results14:
                      continue
                    state[61] = lfsr_bs(state, 13)
                    filter15_4 = f20a_bs(state[49],state[58],state[59],state[61])
                    filter15 = f20c_bs(filter15_0, filter15_1, filter15_2, filter15_3, filter15_4)
                    results15 = filter15 == keystream[15]
                    if not results15:
                      continue
                    state[62] = lfsr_bs(state, 14)
                    filter16_4 = f20a_bs(state[50],state[59],state[60],state[62])
                    filter16 = f20c_bs(filter16_0, filter16_1, filter16_2, filter16_3, filter16_4)
                    results16 = filter16 == keystream[16]
                    if not results16:
                      continue
                    state[63] = lfsr_bs(state, 15)
                    filter17_4 = f20a_bs(state[51],state[60],state[61],state[63])
                    filter17 = f20c_bs(filter17_0, filter17_1, filter17_2, filter17_3, filter17_4)
                    results17 = filter17 == keystream[17]
                    if not results17:
                      continue
                    state[64] = lfsr_bs(state, 16)
                    filter18_4 = f20a_bs(state[52],state[61],state[62],state[64])
                    filter18 = f20c_bs(filter18_0, filter18_1, filter18_2, filter18_3, filter18_4)
                    results18 = filter18 == keystream[18]
                    if not results18:
                      continue
                    state[65] = lfsr_bs(state, 17)
                    filter19_4 = f20a_bs(state[53],state[62],state[63],state[65])
                    filter19 = f20c_bs(filter19_0, filter19_1, filter19_2, filter19_3, filter19_4)
                    results19 = filter19 == keystream[19]
                    if not results19:
                      continue
                    state[66] = lfsr_bs(state, 18)
                    filter20_4 = f20a_bs(state[54],state[63],state[64],state[66])
                    filter20 = f20c_bs(filter20_0, filter20_1, filter20_2, filter20_3, filter20_4)
                    results20 = filter20 == keystream[20]
                    if not results20:
                      continue
                    state[67] = lfsr_bs(state, 19)
                    filter21_4 = f20a_bs(state[55],state[64],state[65],state[67])
                    filter21 = f20c_bs(filter21_0, filter21_1, filter21_2, filter21_3, filter21_4)
                    results21 = filter21 == keystream[21]
                    if not results21:
                      continue
                    state[68] = lfsr_bs(state, 20)
                    filter22_4 = f20a_bs(state[56],state[65],state[66],state[68])
                    filter22 = f20c_bs(filter22_0, filter22_1, filter22_2, filter22_3, filter22_4)
                    results22 = filter22 == keystream[22]
                    if not results22:
                      continue
                    state[69] = lfsr_bs(state, 21)
                    filter23_3 = f20b_bs(state[51],state[52],state[54],state[56])
                    filter23_4 = f20a_bs(state[57],state[66],state[67],state[69])
                    filter23 = f20c_bs(filter23_0, filter23_1, filter23_2, filter23_3, filter23_4)
                    results23 = filter23 == keystream[23]
                    if not results23:
                      continue
                    state[70] = lfsr_bs(state, 22)
                    filter24_3 = f20b_bs(state[52],state[53],state[55],state[57])
                    filter24_4 = f20a_bs(state[58],state[67],state[68],state[70])
                    filter24 = f20c_bs(filter24_0, filter24_1, filter24_2, filter24_3, filter24_4)
                    results24 = filter24 == keystream[24]
                    if not results24:
                      continue
                    state[71] = lfsr_bs(state, 23)
                    filter25_3 = f20b_bs(state[53],state[54],state[56],state[58])
                    filter25_4 = f20a_bs(state[59],state[68],state[69],state[71])
                    filter25 = f20c_bs(filter25_0, filter25_1, filter25_2, filter25_3, filter25_4)
                    results25 = filter25 == keystream[25]
                    if not results25:
                      continue
                    state[72] = lfsr_bs(state, 24)
                    filter26_3 = f20b_bs(state[54],state[55],state[57],state[59])
                    filter26_4 = f20a_bs(state[60],state[69],state[70],state[72])
                    filter26 = f20c_bs(filter26_0, filter26_1, filter26_2, filter26_3, filter26_4)
                    results26 = filter26 == keystream[26]
                    if not results26:
                      continue
                    state[73] = lfsr_bs(state, 25)
                    filter27_0 = f20a_bs(state[29],state[30],state[32],state[33])
                    filter27_1 = f20b_bs(state[35],state[39],state[41],state[42])
                    filter27_2 = f20b_bs(state[44],state[48],state[50],state[53])
                    filter27_3 = f20b_bs(state[55],state[56],state[58],state[60])
                    filter27_4 = f20a_bs(state[61],state[70],state[71],state[73])
                    filter27 = f20c_bs(filter27_0, filter27_1, filter27_2, filter27_3, filter27_4)
                    results27 = filter27 == keystream[27]
                    if not results27:
                      continue
                    state[74] = lfsr_bs(state, 26)
                    filter28_0 = f20a_bs(state[30],state[31],state[33],state[34])
                    filter28_1 = f20b_bs(state[36],state[40],state[42],state[43])
                    filter28_2 = f20b_bs(state[45],state[49],state[51],state[54])
                    filter28_3 = f20b_bs(state[56],state[57],state[59],state[61])
                    filter28_4 = f20a_bs(state[62],state[71],state[72],state[74])
                    filter28 = f20c_bs(filter28_0, filter28_1, filter28_2, filter28_3, filter28_4)
                    results28 = filter28 == keystream[28]
                    if not results28:
                      continue
                    state[75] = lfsr_bs(state, 27)
                    filter29_0 = f20a_bs(state[31],state[32],state[34],state[35])
                    filter29_1 = f20b_bs(state[37],state[41],state[43],state[44])
                    filter29_2 = f20b_bs(state[46],state[50],state[52],state[55])
                    filter29_3 = f20b_bs(state[57],state[58],state[60],state[62])
                    filter29_4 = f20a_bs(state[63],state[72],state[73],state[75])
                    filter29 = f20c_bs(filter29_0, filter29_1, filter29_2, filter29_3, filter29_4)
                    results29 = filter29 == keystream[29]
                    if not results29:
                      continue
                    state[76] = lfsr_bs(state, 28)
                    filter30_0 = f20a_bs(state[32],state[33],state[35],state[36])
                    filter30_1 = f20b_bs(state[38],state[42],state[44],state[45])
                    filter30_2 = f20b_bs(state[47],state[51],state[53],state[56])
                    filter30_3 = f20b_bs(state[58],state[59],state[61],state[63])
                    filter30_4 = f20a_bs(state[64],state[73],state[74],state[76])
                    filter30 = f20c_bs(filter30_0, filter30_1, filter30_2, filter30_3, filter30_4)
                    results30 = filter30 == keystream[30]
                    if not results30:
                      continue
                    state[77] = lfsr_bs(state, 29)
                    filter31_0 = f20a_bs(state[33],state[34],state[36],state[37])
                    filter31_1 = f20b_bs(state[39],state[43],state[45],state[46])
                    filter31_2 = f20b_bs(state[48],state[52],state[54],state[57])
                    filter31_3 = f20b_bs(state[59],state[60],state[62],state[64])
                    filter31_4 = f20a_bs(state[65],state[74],state[75],state[77])
                    filter31 = f20c_bs(filter31_0, filter31_1, filter31_2, filter31_3, filter31_4)
                    results31 = filter31 == keystream[31]
                    if not results31:
                      continue
                    print hex(lfsr_inv(lfsr_inv(unbitslice(state,2))))
