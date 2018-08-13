from naive import *

def generate_fills(filt_mask=0x5806b4a2d16c):
    layer_fills = [{} for _ in range(len(masks))]
    for i in range(0, 1<<20):
        taps_fill = expand(filt_mask, i)
        out = f20(taps_fill)
        for layer in range(len(masks)):
            if out != keystream[layer]:
                continue
            new = taps_fill & masks[layer]
            old = taps_fill & ~masks[layer]
            assert old | new == taps_fill
            try:
                layer_fills[layer][old].append(new)
            except:
                layer_fills[layer][old] = [new]
    return layer_fills

def fill_layer(state, layer, filt_mask=0x5806b4a2d16c):
    if layer < len(masks):
        try:
            table = layer_fills[layer][state & filt_mask]
            for efill in table:
                new_state = state | efill
                assert f20(new_state) == keystream[layer]
                # debug test
                if testing and not layer and ((new_state & filt_mask) != (test_states[layer] & filt_mask)):
                   continue
                if layer < last_lfsr_guess:
                    fill_layer(new_state>>1, layer+1, filt_mask)
                    fill_layer(new_state>>1 | (1<<47), layer+1, filt_mask)
                else:
                    fill_layer(lfsr(new_state), layer+1, filt_mask)
        except: # Table miss
            pass
    else:
        test(state)

if __name__ == "__main__":
    print "Generating LUTs"
    layer_fills = generate_fills()
    #print len(layer_fills[0][0])
    print "Finding state"
    testing = True
    fill_layer(0, 0)
