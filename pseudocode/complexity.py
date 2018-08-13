from naive import *
from math import log
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
        if __name__ == "__main__":
            print "Average output states at keystream test", layer, avg_states
        return layers_from_avg_to_min(layer+1, avg_states, min_states)

if __name__ == "__main__":
    # Total problem size starting from 1 candidate at layer 0
    last_layer, n_states = layers_from_avg_to_min(0,1,1)
    #print last_layer, n_states
    # Total problem size starting from 1 candidates at layer 1
    #cutoff, remaining = layers_from_avg_to_min(1,1,1)

