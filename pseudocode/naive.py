from maskgen import *
from hitag2 import *

def popcount(x):
    return "{0:0b}".format(x).count('1')

masks, last_lfsr_guess = generate_masks()
bits = [popcount(x) for x in masks]

state = hitag2_init(0x414141414141, 0x42424242, 0x43434343)
keystream_int = hitag2(state,32)
keystream = map(int, "{0:032b}".format(keystream_int))
#print keystream
def expand(mask, x):
    res = 0
    for i in range(0, 48):
        if mask & 1:
            res |= (x & 1)<<i
            x >>= 1
        mask >>= 1
    return res

def compress(mask, x):
    result = 0;
    bits_eaten = 0;
    bit_index = 0
    while bits_eaten < popcount(mask):
        if((mask>>bit_index)&1):
            if((x>>bit_index)&1):
                result |= (1 << bits_eaten)
            bits_eaten += 1
        bit_index += 1
    return result

def test(state):
    for bit in range(len(masks), 32):
        if f20(state) != keystream[bit]:
            return
        state = lfsr(state)
    for _ in range(32):
        state = lfsr_inv(state)
    print hex(state)

#test(state)

test_states = []
for _ in range(len(masks)):
    test_states.append(state)
    state = lfsr(state)

def fill_layer(state, layer, filt_mask=0x5806b4a2d16c):
    if layer < len(masks):
        for fill in range(0, 1<<bits[layer]):
            new_state = state | expand(masks[layer], fill)
            # debug test
            if testing and (new_state & filt_mask) != (test_states[layer] & filt_mask):
                continue
            #print layer, hex(new_state), fill
            if f20(new_state) != keystream[layer]:
                continue
            if layer < last_lfsr_guess:
                fill_layer(new_state>>1, layer+1, filt_mask)
                fill_layer((new_state>>1) | (1<<47), layer+1, filt_mask)
            else:
                fill_layer(lfsr(new_state), layer+1, filt_mask)
    else:
        test(state)

if __name__ == "__main__":
    testing = True
    fill_layer(0, 0)
