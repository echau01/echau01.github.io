---
layout: post
title: "Conjugation: what $gfg^{-1}$ actually means"
---

Let's start with some linear algebra: recall that two $n\times n$ matrices $S$ and $T$ (which represent linear transformations $\mathbb{R}^n\to\mathbb{R}^n$) are _similar_ if there is an invertible matrix $B$ such that
\\[S = BTB^{-1}.\\]
In my first linear algebra class, I learned that that if $S$ and $T$ are similar, then they represent the same transformation but in different bases of $\mathbb{R}^n$. I was told that this was a special case of a mathematical concept called _conjugation_---if we have a function $f: A\to A$ and an invertible function $g: A\to A$, then we can "conjugate $f$ by $g$" to form a function $f^g = g\circ f\circ g^{-1}$, which is somehow very similar to $f$. For example:

- $f$ is invertible if and only if $f^g$ is invertible.
- $f$ and $f^g$ have the same number of fixed points.
- $f\circ f\circ f$ is the identity function on $A$ if and only if $f^g\circ f^g\circ f^g$ is also the identity function on $A$.
- There is a bijection between $f(A)$ and $f^g(A)$. Symbolically, $\|f(A)\| = \|f^g(A)\|$.

They are by no means identical functions, but basically every property of $f$ can be translated to a corresponding property of $f^g$. Let's investigate this intuition further.

# Why $f^g$ and $f$ are so similar

(From now on, I will omit the composition symbol $\circ$ for brevity, e.g. I will write $fg$ instead of $f\circ g$.)

Observe that for all $x\in A$,
\\[f^g(g(x)) = (gfg^{-1})(g(x)) = (gf)(x) = g(f(x)).\\]
Therefore, $f^g$ is the map $g(x)\mapsto g(f(x))$. (Since $g$ is a bijection, this map is well-defined.) Imagine $f$ and $g$ as "lenses" that make us view each object $x\in A$ as $f(x)$ and $g(x)$, respectively. Then **$f^g$ is the action of applying the $f$-lens while looking through the $g$-lens**.

To use a real-life analogy, imagine that $A$ is a Petri dish of bacteria, $g$ is the action of looking at the bacteria through a microscope, and $f$ is the action of staining the bacteria with a dye. While looking through the microscope, we apply the dye to the bacteria. In real life, we have transformed the bacteria with the function $f$, but what we _see_ through the microscope is the function $f^g$---the transformation that turns enlarged bacteria (i.e. $g(x)$) into enlarged dyed bacteria (i.e. $g(f(x))$). This analogy is not quite perfect since $g$ in this scenario is not actually a function from $A$ to itself, but I think it illustrates the map $g(x)\mapsto g(f(x))$ quite well.

Therefore, $f^g$ and $f$ transform the elements of $A$ in exactly the same way. The only difference between $f^g$ and $f$ is that we view the inputs and outputs of $f^g$ through the $g$-lens.

# Equivalent functions

Another way we can get the similarity between $f^g$ and $f$ is by generalizing a bit. Imagine we have two sets $A$ and $A'$ that can be put into bijection with each other. Let $f: A\to A$ and $f': A'\to A'$ be functions, and suppose there is a bijection $x\in A\longleftrightarrow x'\in A'$ such that $[f(x)]' = f'(x')$ for all $x$. Then $f$ and $f'$ are essentially the same function. Imagine superimposing the set $A$ on top of $A'$ so that each $x\in A$ overlaps with the corresponding $x'\in A'$. If we apply $f$ to $A$ and watch how the points move, we would see exactly the same thing as if we apply $f'$ to $A'$. Hence, $f$ and $f'$ are essentially the same function, and we call them _equivalent_. 

I will now show that equivalent functions and conjugates are the same thing. Let $g: A\to A'$ such that $g(x) = x'$. For all $x\in A$, we have
\\[g(f(x)) = [f(x)]' = f'(x') = f'(g(x)),\\]
so $gf = f'g$ and hence $gfg^{-1} = f'$. This means equivalent functions are conjugates. On the other hand,
<div>
\begin{align}
    [f(x)]' &= g(f(x)) \\
    &= (gfg^{-1})(g(x)) \\
    &= (gfg^{-1})(x')
\end{align}
</div>
for all $x\in A$, so conjugates are equivalent functions.

Specializing $A'$ to $A$, we conclude that $f^g$ and $f$ are equivalent functions, and any function equivalent to $f$ must be conjugate with $f$.

Addendum: another way to think of $f$ and $f'$ being equivalent is to note that the following diagram commutes.

<img src="/assets/images/2024-11-11-conjugation/equivalent-functions-cd.PNG" alt="Commutative diagram for gf = f'g" width="200" style="display: block; margin: auto">

# Similar matrices revisited

When we see the matrix equation $S = BTB^{-1}$, we now know that $S$ maps $Bx$ to $BTx$ for all $x\in\mathbb{R}^n$. What does that mean in the context of linear algebra?

Since $B$ is invertible, the columns of $B$ form a basis $\mathcal{B} = \\{v_1, v_2, \dots, v_n\\}$ of $\mathbb{R}^n$. If $x$ is a vector expressed in $\mathcal{B}$-coordinates, then $Bx$ is the same vector expressed in standard coordinates. Therefore, $S$ maps $x$ to $Tx$ in $\mathcal{B}$-coordinates. To translate back to standard coordinates, all we need to do is multiply the input (i.e. $x$) and output (i.e. $Tx$) by $B$. Modulo the coordinate system, $S$ and $T$ really are the same linear transformation.
