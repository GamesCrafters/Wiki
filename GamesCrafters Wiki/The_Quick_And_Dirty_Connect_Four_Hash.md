The\_Quick\_And\_Dirty\_Connect\_Four\_Hash
===========================================

Tier Offset
-----------

Tier \(n\) in Connect Four is the set of all positions in which there are exactly n pieces on the board. The size of tier n is: \(P_n=[{x}^{n}]{\left(\frac{1-x^{h+1}}{1-x}\right)}^{w}*\binom{n}{b}\) where \([x^{k}]F(x)\) denotes the coeficient of \(x^{k}\) in the polynomial expansion of \(F(x)\). w and h are the width and height of the board respectively. b is the number of black pieces on the board or \(b = \lceiling \frac{n}{2} \rceiling\)

The offset for a tier is the sum of the sizes of all the previous tiers: \(O_n=\sum_{k=0}^{n-1}P_k\)

Column Hash
-----------

This number uniquely hashes the column heights without caring about the color of the pieces. Let \(h_c\) denote the height of column c. \(n_c\) is the sum of the heights of the previous columns
\(n_c = \sum_{k=0}^{c-1}{h_k}\)

Color Hash
----------
