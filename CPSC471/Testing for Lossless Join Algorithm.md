### Algorithm
**Input**: A universal relation R, a decomposition D = {R1, R2, R3, ..., Rm} of R, and a set F of functional dependencies
1. Create an initial matrix S with one row `i` for each relation `Ri` in `D`, and one column `j` for each attribute `Aj` in `R`
2. For each row `i` and column `j` in S, if relation `Ri` includes attribute `Aj` then set `S(i,j) = a`
3. For each FD `X -> Y`:
	- For each row `R1` that contains all attributes in `X`:
		- For each row `R2` that contains all attributes in `X` where `R1 != R2`:
			- For each attribute `k` in `Y`:
				- If `R1` contains `k`, then set `k` in `R2` to be the symbol `a`
 - Repeat step 3 until a *full loop execution* results in no changes to S
4. If a row is made up entirely of `a` symbols, the decomposition has the lossless join property. Otherwise, it does not.

### Example:
Let `R = {A, B, C, D, E, F}`, `D = {R1, R2, R3}`
`R1 = {A, B}`
`R2 = {C, D, E}`
`R3 = {A, C, F}`
`FD = { {A} -> {B}, {C} -> {D, E}, {A, C} -> {F} }`

**Step 1**:
| |A|B|C|D|E|F|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|R1| | | | | | |
|R2| | | | | | |
|R3| | | | | | |

**Step 2**:
| |A|B|C|D|E|F|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|R1|a|a| | | | |
|R2| | |a|a|a| |
|R3|a| |a| | |a|

**Step 3 (A -> B)**:
| |A|B|C|D|E|F|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|R1|a|a| | | | |
|R2| | |a|a|a| |
|R3|a|*a*|a| | |a|
 - A exists in R1 and R3, as B exists in R1 we can set B to be in R3

**Step 3 (C -> D, E)**:
| |A|B|C|D|E|F|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|R1|a|a| | | | |
|R2| | |a|a|a| |
|R3|a|a|a|*a*|*a*|a|
 - C exists in R2 and R3, as D exists in R2 we can set D to be in R3. Same with E

**Step 3 (A, C -> F)**:
| |A|B|C|D|E|F|
|:-|:-:|:-:|:-:|:-:|:-:|-:|
|R1|a|a| | | | |
|R2| | |a|a|a| |
|R3|a|a|a|a|a|a|
 - A and C exist in R3, but since no other relation contains both A, C we can't set F anywhere else

**Step 4**:
 - As `R3` is composed entirely of `a` symbols, the decomposition has the lossless join property.
