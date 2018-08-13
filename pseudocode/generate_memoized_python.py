from tabled import *
from complexity import *
from math import log

def generate_python(depth,
                       sub_masks=[0x00000000006c,
                                  0x00000000d100,
                                  0x000004a20000,
                                  0x0002b0000000,
                                  0x580400000000],
                       lfsr_mask=0xce0044c101cd):
    memoize_filter = True
    memoize_lfsr = True
    # keep track of known subfilters and bits at each layer
    found = [[0 for _ in range(len(sub_masks))] for _ in range(32)]
    lfsr_found = [0 for _ in range(32)]
    fill = 0
    print "from naive import *"
    print "def fill_layer(a=None, b=None, filt_mask=0x5806b4a2d16c):"
    print "  state = [0 for _ in range(48+32)]"

    memo_funcs = ['f20a_bs', 'f20b_bs', 'f20b_bs', 'f20b_bs', 'f20a_bs']
    memo_input = [[2,3,5,6],[8,12,14,15],[17,21,23,26],[28,29,31,33],[34,43,44,46]]

    for layer in range(len(masks)):
        # define recursion loops
        if not layer:
            print "  "*(layer+1) + "for i%u in range(1<<bits[%u]):" % (layer, layer)
            inmask = 1
            for i in range(48):
                if (masks[layer]>>i) & 1:
                    print "  "*(layer+2) + "state[%u] = bool((i%u & %s))" % (i+layer, layer, hex(inmask))
                    inmask <<= 1
        elif layer <= last_lfsr_guess:
            print "  "*(layer+1) + "for i%u in range(1<<(bits[%u]+1)):" % (layer, layer)
            inmask = 1
            for i in range(48):
                if (masks[layer]>>i) & 1:
                    print "  "*(layer+2) + "state[%u] = bool((i%u & %s))" % (i+layer, layer, hex(inmask))
                    inmask <<= 1
            print "  "*(layer+2) + "state[%u] = bool((i%u & %s)) # guess lfsr output %u" % (47+layer, layer, hex(inmask), layer-1)
            fill |= (1<<(47+layer))
            lfsr_found[layer] = 1
        else:
            if not lfsr_found[layer]:
                print "  "*(layer+1) + "state[%u] = lfsr_bs(state,%u)" % (47+layer, layer-1)
                fill |= (1<<(47+layer))
                lfsr_found[layer] = 1
            print "  "*(layer+1) + "for i%u in range(1<<bits[%u]):" % (layer, layer)
            inmask = 1
            for i in range(48):
                if (masks[layer]>>i) & 1:
                    print "  "*(layer+2) + "state[%u] = bool((i%u & %s))" % (i+layer, layer, hex(inmask))
                    inmask <<= 1

        fill |= (masks[layer]<<(layer)) # mask
        print "  "*(layer+2) + "#", hex(fill>>layer & (1<<48)-1)

        # test at layer 0
        if testing and not layer:
            print "  "*(layer+2) + "if (unbitslice(state,%u) & filt_mask) != (test_states[%u] & filt_mask):" % (layer, layer)
            print "  "*(layer+3) + "continue"
            print "  "*(layer+2) + "print %u, hex(unbitslice(state, %u))" % (layer, layer)

        if depth < layer:
            depth = layer+1
        for next_bit in range(layer, len(masks)):
            # greedily precompute LFSR output
            if memoize_lfsr and ((((fill<<1)>>next_bit)&lfsr_mask) == lfsr_mask) and not lfsr_found[next_bit]:
                #print "LFSR output for layer", next_bit, \
                      #"can be determined at layer", layer
                print "  "*(layer+2) + "state[%u] = lfsr_bs(state,%u)" % (47+next_bit, next_bit-1)
                fill |= (1<<(47+next_bit))
                lfsr_found[next_bit] = 1
            if not memoize_filter:
                continue
        for next_bit in range(layer, depth):
            # solve next subfilters
            for subfilter in range(len(sub_masks)):
                if found[next_bit][subfilter]:
                    continue
                target = sub_masks[subfilter]
                if ((fill>>next_bit) & target) == target:
                    #print "Subfilter",      subfilter, \
                          #"for layer",      next_bit, \
                          #"known at layer", layer
                    print "  "*(layer+2) + "filter%u_%u = %s(state[%u],state[%u],state[%u],state[%u])" % ((next_bit, subfilter, memo_funcs[subfilter]) + tuple(map(lambda x: x+next_bit, memo_input[subfilter])))
                    found[next_bit][subfilter] = 1

        if layer == len(masks)-1:
            for bit in range(len(masks), 32):
                for subfilter in range(len(sub_masks)):
                    if not found[bit][subfilter]:
                        print "  "*(layer+2) + "filter%u_%u = %s(state[%u],state[%u],state[%u],state[%u])" % ((bit, subfilter, memo_funcs[subfilter]) + tuple(map(lambda x: x+bit, memo_input[subfilter])))
                        found[bit][subfilter] = 1
                print "  "*(layer+2) + "filter%u = f20c_bs(filter%u_0, filter%u_1, filter%u_2, filter%u_3, filter%u_4)" % (bit, bit, bit, bit, bit, bit)
                print "  "*(layer+2) + "results%u = filter%u == keystream[%u]" % (bit, bit, bit)
                print "  "*(layer+2) + "if not results%u:" % bit
                print "  "*(11) + "continue"
                if bit < 31 and not lfsr_found[bit]:
                    print "  "*(layer+2) + "state[%u] = lfsr_bs(state, %u)" % (47+bit, bit-1)
            print "  "*(layer+2) + "print hex(lfsr_inv(lfsr_inv(unbitslice(state,2))))"
        else:
            for subfilter in range(len(sub_masks)):
                if not found[layer][subfilter]:
                    print "  "*(layer+2) + "filter%u_%u = %s(state[%u],state[%u],state[%u],state[%u])" % ((layer, subfilter, memo_funcs[subfilter]) + tuple(map(lambda x: x+layer, memo_input[subfilter])))
                    found[layer][subfilter] = 1
                    
            print "  "*(layer+2) + "filter%u = f20c_bs(filter%u_0, filter%u_1, filter%u_2, filter%u_3, filter%u_4)" % (layer, layer, layer, layer, layer, layer)
            print "  "*(layer+2) + "results%u = filter%u == keystream[%u]" % (layer, layer, layer)
            print "  "*(layer+2) + "if not results%u:" % layer
            print "  "*(layer+3) + "continue"

    return found

# Find how many nested loops to peel for subfilter work
def layers_from_avg_to_min(layer=0, avg_states=1, min_states=32):
    if layer >= len(keystream) \
    or layer >= len(masks) and avg_states <= min_states:
        return layer, avg_states
    else:
        if layer < last_lfsr_guess:
            # guess LFSR output bit
            avg_states <<= 1
        try:
            # guess filter input bits
            avg_states <<= bits[layer]
        except:
            pass
        # strike half the candidates on average
        avg_states >>= 1
        #print "Avg states at layer", layer, avg_states
        return layers_from_avg_to_min(layer+1, avg_states, min_states)

# Total problem size starting from 1 candidate at layer 0
cutoff, remaining = layers_from_avg_to_min(0,1,1)
# Total problem size starting from 1 candidate at layer 1
#cutoff, remaining = layers_from_avg_to_min(1,1,1)
#print cutoff

testing = True
#testing = False
# use 32-way bitsliicing (log(32) = 5)
generate_python(cutoff-5)
#generate_python(0)
