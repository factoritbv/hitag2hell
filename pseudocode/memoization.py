from tabled import *

def generate_memos(depth,
                   sub_masks=[0x00000000006c,
                              0x00000000d100,
                              0x000004a20000,
                              0x0002b0000000,
                              0x580400000000],
                   lfsr_mask=0xce0044c101cd):
    # keep track of known subfilters and bits
    filt_found = [ 
                  [0 for _ in range(len(sub_masks))]
                  for _ in range(len(keystream))
                 ]
    lfsr_found = [0 for _ in(range(len(keystream))) ]
    fill = 0
    lfsr_guess_delay = 0
    lfsr_guess_rounds = [0]*lfsr_guess_delay + [1 if i and i <= last_lfsr_guess else 0 for i in range(32)]
    print lfsr_guess_rounds

    for layer in range(len(masks)):
        print layer
        fill |= (masks[layer]<<layer) # track filter input
        if lfsr_guess_rounds[layer]:
            fill |= (1<<(47+layer-lfsr_guess_delay)) # track guessed LFSR output
            print "LFSR guess", 47+layer-lfsr_guess_delay
        if (((fill<<1)>>layer)&lfsr_mask) == lfsr_mask:
            fill |= (1<<(47+layer)) # track LFSR output
        lfsr_found[layer] = 1
        for next_bit in range(layer, depth):
            # greedily precompute LFSR output
            if (lfsr_mask is not None or layer == len(masks)-1) \
            and not lfsr_found[next_bit] \
            and (((fill<<1)>>next_bit)&lfsr_mask) == lfsr_mask:
                print "LFSR output for layer", next_bit-1, \
                      "known at layer", layer
                fill |= (1<<(47+next_bit))
                lfsr_found[next_bit] = 1
        found_on_layer = 0
        for next_bit in range(layer, depth):
            # find computable subfilters
            for subfilter in range(len(sub_masks)):
                if filt_found[next_bit][subfilter]:
                    continue
                target = sub_masks[subfilter]
                if ((fill>>next_bit) & target) == target:
                    print "Subfilter",      subfilter, \
                          "for layer",      next_bit, \
                          "known at layer", layer
                    filt_found[next_bit][subfilter] = 1
                    found_on_layer += 1
        print "Found", found_on_layer, "on layer", layer
        print hex(fill)

generate_memos(12)
