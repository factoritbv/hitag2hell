def generate_masks(filt_mask=0x5806b4a2d16c,
                   lfsr_mask=0xce0044c101cd):
    masks = []
    fill = last_lfsr_guess = 0
    while fill != 0xffffffffffff:
        masks.append(filt_mask) # use taps mask
        fill |= filt_mask # track known bits
        # Check if LFSR output should be guessed
        if (fill & lfsr_mask) != lfsr_mask:
            last_lfsr_guess += 1
        fill >>= 1 # update LFSR state
        fill |= (1<<47) # guess or get LFSR output
        # Take out known bits from next mask
        filt_mask &= ~fill
        #print hex(fill)
    return masks, last_lfsr_guess

if __name__ == "__main__":
    m,i = generate_masks()
    print map(hex,m)
    print i

