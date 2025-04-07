---
layout: post
title: Linear isometries preserve angles
---

In my previous post on [classifying isometries in $\mathbb{R}^2$]({% post_url 2025-03-01-planar-isometries %}), I proved that any linear isometry $T: \mathbb{R}^2\to\mathbb{R}^2$ satisfies
\\[\langle v, w\rangle = \langle T(v), T(w)\rangle\\]
for all $v, w\in\mathbb{R}^2$, where $\langle\cdot, \cdot\rangle$ is the dot product on $\mathbb{R}^2$. In other words, $T$ preserves the angle between any pair of vectors $v, w\in\mathbb{R}^2$.

This turns out to be true if $V$ is any vector space with an inner product. Let $V$ be an [inner-product space](https://en.wikipedia.org/wiki/Inner_product_space) over $\mathbb{R}$ or $\mathbb{C}$, and let $T: V\to V$ be a linear isometry. Then for all $v, w\in V$, we have that
\\[||v + w||^2 = ||T(v + w)||^2 = ||T(v) + T(w)||^2.\\]
Expanding both sides gives
\\[||v||^2 + \langle v, w\rangle + \langle w, v\rangle + ||w||^2 = ||T(v)||^2 + \langle T(v), T(w)\rangle + \langle T(w), T(v)\rangle + ||T(w)||^2.\\]
Since $||v|| = ||T(v)||$ and $||w|| = ||T(w)||$, we have that
\\[\langle v, w\rangle + \langle w, v\rangle = \langle T(v), T(w)\rangle + \langle T(w), T(v)\rangle.\\]

If $V$ is a vector space over $\mathbb{R}$, then the inner product is symmetric, so
\\[2\langle v, w\rangle = 2\langle T(v), T(w)\rangle\\]
and hence $\langle v, w\rangle = \langle T(v), T(w)\rangle$.

If $V$ is a vector space over $\mathbb{C}$, then the inner product is conjugate-symmetric, which means
\\[\langle v, w\rangle + \overline{\langle v, w\rangle} = \langle T(v), T(w)\rangle + \overline{\langle T(v), T(w)\rangle}.\\]
Hence,
\\[2\text{Re}(\langle v, w\rangle) = 2\text{Re}(\langle T(v), T(w)),\\]
so
\\[\text{Re}(\langle v, w\rangle) = \text{Re}(\langle T(v), T(w)\rangle).\\]
This equation holds for _all_ vectors $v, w\in V$. Since $-iv$ is also an element of $V$, we can substitute $v$ for $-iv$ to get
\\[\text{Re}(\langle -iv, w\rangle) = \text{Re}(\langle T(-iv), T(w)\rangle).\\]
This simplifies to
\\[\text{Re}(-i\langle v, w\rangle) = \text{Re}(-i\langle T(v), T(w)\rangle).\\]
Since $\text{Re}(-iz) = \text{Im}(z)$ for any complex number $z$, it follows that
\\[\text{Im}(\langle v, w\rangle) = \text{Im}(\langle T(v), T(w)\rangle).\\]
Therefore, $\langle v, w\rangle = \langle T(v), T(w)\rangle$ since their real and imaginary parts are equal.
