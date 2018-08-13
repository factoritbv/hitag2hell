from tabled import *

def fill_layer(state, layer, filt_mask=0x5806b4a2d16c):
    buf = [[] for _ in range(len(masks)+1)]
    buf[layer].append(state)
    bsize = 10000000
    while any(map(len,buf)):
        #print layer, len(buf[layer])
        while len(buf[layer]) and len(buf[layer+1]) < bsize:
            state = buf[layer].pop()
            try:
                for fill in layer_fills[layer][state & filt_mask]:
                    new_state = state | fill
                    #assert f20(new_state) == keystream[layer]
                    if testing and not layer and ((new_state & filt_mask) != (test_states[layer] & filt_mask)):
                       continue
                    if layer < last_lfsr_guess:
                        buf[layer+1].append(new_state>>1)
                        buf[layer+1].append(new_state>>1|(1<<47))
                    else:
                        buf[layer+1].append(lfsr(new_state))
            except KeyError: # Table miss
                pass
        layer += 1
        if layer == len(masks):
            #print len(buf[len(masks)])
            while buf[len(masks)]:
                #buf[len(masks)].pop()
                test(buf[len(masks)].pop())
        layer %= len(masks)

if __name__ == "__main__":
    print "Generating LUTs"
    layer_fills = generate_fills()
    #print len(layer_fills[0][0])
    print "Finding state"
    testing = True
    fill_layer(0, 0)

