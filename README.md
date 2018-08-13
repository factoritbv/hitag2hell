# Introduction

This repository complements the research documented in the paper `Hitag 2 Hell - Brutally optimizing guess-and-determine attacks', as presented at USENIX WOOT2018.

# Pseudocode

* `maskgen.py`: generate masks for which bits to guess in each layer
* `naive.py`: naive guess-and-determine implementation
* `unrolled.py`: naive implementation which is unrolled

* `tabled.py`: implementation which avoids impossible guesses
* `tabled_buffered.py`: implementation which avoids impossible guesses, and tries to mitigate the intense cache pressure

* `memoized.py`: implementation which applies memoization
* `generate_memoized_python.py`: generator for `memoized_gen.py`
* `memoized_gen.py`: generated code from `generate_memoized_python.py`, used in `memoized.py`

* `complexity.py`: compute complexity at each layer
* `hitag2.py`: HITAG2 implementation

# Implementations

Our best implementations from the research, as featured in the paper's appendix verbatim, are also included here for ease of use.
