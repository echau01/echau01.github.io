---
layout: post
title: "A brief primer on block-diagonal matrices"
---

A square matrix is _block-diagonal_ if it has the form
<div>
\[\begin{bmatrix}
    B_1 & & & \\
    & B_2 & & \\
    & & \ddots & \\
    & & & B_k
\end{bmatrix}\]
</div>
where the _blocks_ $B_i$ are square sub-matrices centered on the main diagonal, and everything outside the blocks is 0. Here is an example of a $5\times 5$ block-diagonal matrix with a $2\times 2$ block and a $3\times 3$ block:

<div>
\[\begin{bmatrix}
    1 & 2 & 0 & 0 & 0 \\ 
    3 & 4 & 0 & 0 & 0 \\
    0 & 0 & 5 & 6 & 7 \\
    0 & 0 & 8 & 9 & 10 \\
    0 & 0 & 11 & 12 & 13
\end{bmatrix}.\]
</div>

Block-diagonal matrices are extremely useful because they represent linear transformations that can be decomposed into simpler linear transformations. Consider again the generic block-diagonal matrix
<div>
\[B = \begin{bmatrix}
    B_1 & & & \\
    & B_2 & & \\
    & & \ddots & \\
    & & & B_k
\end{bmatrix}.\]
</div>
For each $1\leq i\leq k$, let $\ell_i$ be the length of the block $B_i$ (i.e. $B_i$ is a $\ell_i\times \ell_i$ matrix). Then $B$ is an $n\times n$ matrix where $n = \sum_{i=1}^k \ell_i$. For each $x\in F^n$ (where $F$ is $\mathbb{R}$ or $\mathbb{C}$ or your favourite field), we can write
<div>
\[x = \begin{bmatrix}x_1 \\ x_2 \\ \vdots \\ x_k\end{bmatrix}\]
</div>
where $x_1\in F^{\ell_1}$ consists of the first $\ell_1$ components of $x$, $x_2\in F^{\ell_2}$ consists of the next $\ell_2$ components of $x$, and so on. The key fact is that
<div>
\[Bx = \begin{bmatrix}B_1 & & & \\ & B_2 & & \\ & & \ddots & \\ & & & B_k\end{bmatrix}\begin{bmatrix}x_1 \\ x_2 \\ \vdots \\ x_k\end{bmatrix} = \begin{bmatrix}B_1x_1 \\ B_2x_2 \\ \vdots \\ B_kx_k\end{bmatrix}.\]
</div>
Each block $B_i$ independently affects its own chunk of components $x_i$, and the final product $Bx$ is equal to the _direct sum_ of the vectors $B_ix_i$. Hence, we often say that $B$ is the direct sum of the $B_i$.

Computing all the $B_ix_i$ and then "concatenating" the results into one giant vector is easier than computing $Bx$ directly without taking advantage of the blocks. The smaller that each block is, the fewer arithmetic operations are required to compute $Bx$. This is most obvious when each block is a $1\times 1$ matrix (i.e. a single number), in which case $B$ is just a diagonal matrix and $Bx$ is very easy to compute.

Computing $\det(B)$ is also easier using the $B_i$---it turns out that
\\[\det(B) = \det(B_1)\det(B_2)\cdots\det(B_k).\\]
A short and easy proof can be found on [Math StackExchange](https://math.stackexchange.com/a/1219331). This determinant formula also implies that the characteristic polynomial of $B$ is the product of the characteristic polynomials of the $B_i$ (because $B-\lambda$ is also a block-diagonal matrix with blocks $B_i-\lambda$).

Finally, if
<div>
\[C = \begin{bmatrix}C_1 & & & \\ & C_2 & & \\ & & \ddots & \\ & & & C_k\end{bmatrix}\]
</div>
is a block-diagonal matrix with the same block sizes as $B$ (i.e. $B_i$ and $C_i$ have the same dimensions for all $1\leq i\leq k$), then the product $BC$ is what you would probably expect:
<div>
\[BC = \begin{bmatrix}B_1C_1 & & & \\ & B_2C_2 & & \\ & & \ddots & \\ & & & B_kC_k\end{bmatrix}.\]
</div>
