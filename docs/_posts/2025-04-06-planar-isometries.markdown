---
layout: post
title: 'Distance-preserving functions in $\mathbb{R}^2$'
---

An _isometry_ of $\mathbb{R}^2$ is a function $f: \mathbb{R}^2\to\mathbb{R}^2$ that preserves distances between points, which means
\\[||f(v) - f(w)|| = ||v - w||\\]
for all $v, w\in\mathbb{R}^2$.

In this post, we will prove a nice result that every isometry in $\mathbb{R}^2$ can be written as a translation composed with a rotation or a reflection. Note: we will use $0$ to mean the number $0$ as well as the zero vector in $\mathbb{R}^2$, but we will keep the usage unambiguous.

Let $f$ be any isometry of $\mathbb{R}^2$. Let $T(v) = f(v) - f(0)$ and $s(v) = v + f(0)$ for all $v\in\mathbb{R}^2$. Then $s$ is a translation and $f = s\circ T$. Now we need to prove that $T$ is a rotation or a reflection. For all $v, w\in\mathbb{R}^2$, we have that
\\[||T(v) - T(w)|| = ||f(v) - f(0) - (f(w) - f(0))|| = ||f(v) - f(w)|| = ||v - w||,\\]
so $T$ is an isometry. Note that $T(0) = 0$. Hence,
\\[||T(v)|| = ||T(v) - T(0)|| = ||v - 0|| = ||v||\\]
for all $v$.

The bulk of our work will be proving that $T$ is a linear transformation. The following lemma, which expands on the Triangle Inequality (<span>$||v + w||\leq ||v|| + ||w||$</span>), will be indispensable:

**Lemma.** Let $v, w\in\mathbb{R}^2\setminus\\{0\\}$. If <span>$||v + w|| = ||v|| + ||w||$</span>, then there exists a scalar $c > 0$ such that $v = cw$. In other words, the vectors $v$ and $w$ (visualized as arrows rooted at the origin) must point in the same direction.

> *Proof.* Let $v = (v_1, v_2)$ and $w = (w_1, w_2)$. Since <span>$||v + w|| = ||v|| + ||w||$</span>, we have that
\\[||v + w||^2 = ||v||^2 + ||w||^2 + 2||v||\cdot||w||.\\]
Hence,
\\[(v_1 + w_1)^2 + (v_2 + w_2)^2 = v_1^2 + v_2^2 + w_1^2 + w_2^2 + 2\sqrt{(v_1^2 + v_2^2)(w_1^2 + w_2^2)}.\\]
After expanding the left-hand side and cancelling like terms on both sides, we get
\\[2v_1w_1 + 2v_2w_2 = 2\sqrt{(v_1^2 + v_2^2)(w_1^2 + w_2^2)}.\\]
Cancelling the common factor of $2$ and squaring both sides yields
\\[v_1^2w_1^2 + v_2^2w_2^2 + 2v_1w_1v_2w_2 = (v_1^2 + v_2^2)(w_1^2 + w_2^2).\\]
Now we expand the right-hand side and cancel like terms to get
\\[2v_1w_1v_2w_2 = v_1^2w_2^2 + v_2^2w_1^2.\\]
Therefore,
\\[0 = v_1^2w_2^2 + v_2^2w_1^2 - 2v_1w_1v_2w_2 = (v_1w_2 - v_2w_1)^2\\]
and (miraculously) we deduce that $v_1w_2 = v_2w_1$. By assumption, $v = (v_1, v_2)\neq 0$, so one of $v_1, v_2$ is nonzero. Without loss of generality we can take $v_1$ to be nonzero. If $v_2 = 0$, then $v_1w_2 = 0$, so $w_2 = 0$. In this case, we have $v = (v_1, 0)$ and $w = (w_1, 0)$, so $v = \frac{v_1}{w_1}w$. Now suppose $v_2\neq 0$. If $w_2 = 0$, then $w_1 = 0$ also, which is impossible since $w\neq 0$. Hence, $w_2\neq 0$, so $w_1\neq 0$ and hence $\frac{v_1}{w_1} = \frac{v_2}{w_2}$. Therefore, $v = \frac{v_1}{w_1}w$.
>
> We have shown that there exists a real number $c$ such that $v = cw$. It remains to show that $c > 0$. Substituting $v = cw$ into the equation <span>$||v + w|| = ||v|| + ||w||$</span> and simplifying on both sides gives
\\[|c + 1|\cdot ||w|| = (|c| + 1)||w||.\\]
Hence, $|c + 1| = |c| + 1$. Suppose towards a contradiction that $c\leq 0$. Then $|c| = -c$, so $|c + 1| = -c + 1$. If $c + 1 = -c + 1$, then $c = 0$, so $v = 0$, contradicting the assumption that $v\neq 0$. The other possibility is that $-(c + 1) = -c + 1$, which implies the contradiction $-1 = 1$. Therefore, $c > 0$. QED.

Now let's prove that $T$ is linear.

**Proposition 1.** Let $c\in\mathbb{R}$ and $v\in\mathbb{R}^2$. Then $T(cv) = cT(v)$.

> *Proof.* If $c = 0$ or $v = 0$, then clearly $T(cv) = 0 = cT(v)$. Also, if $c = 1$, then $T(cv) = T(v) = cT(v)$.
>
> Fix $v\neq 0$, and note that <span>$||T(v)|| = ||v||\neq 0$</span>, so $T(v)\neq 0$. First, suppose that $c > 1$. Then <span>$||T(cv)|| = ||cv|| = c||v||$</span>. Observe that
\\[||T(cv) - T(v)|| = ||cv - v|| = (c - 1)||v||\neq 0,\\]
so $T(cv) - T(v)\neq 0$. Moreover,
> <div>
> \begin{align*}
>   ||[T(cv) - T(v)] + T(v)|| &= ||T(cv)|| \\
>   &= c||v|| \\
>   &= (c - 1)||v|| + ||v|| \\
>   &= ||T(cv) - T(v)|| + ||T(v)||.
> \end{align*}
> </div>
> Since $T(cv) - T(v)$ and $T(v)$ are nonzero, the Lemma says that there exists $k > 0$ such that $T(cv) - T(v) = kT(v)$. Hence, $T(cv) = (k + 1)T(v)$, so
\\[c||v|| = ||T(cv)|| = ||(k+1)T(v)|| = (k+1)||v||.\\]
It follows that $c = k + 1$ and hence $T(cv) = cT(v)$.
>
> Now suppose $0 < c < 1$. Then $\frac{1}{c} > 1$ and hence
\\[T(v) = T\left(\frac{1}{c}cv\right) = \frac{1}{c}T(cv),\\]
so $cT(v) = T(cv)$.
>
> Finally, suppose $c < 0$. Then
> \\[||T(cv) - T(-cv)|| = ||cv - (-cv)|| = 2|c|\cdot ||v|| = ||T(cv)|| + ||T(-cv)||.\\]
> The above equation can be rewritten as
\\[||T(cv) + (-T(-cv))|| = ||T(cv)|| + ||-T(-cv)||,\\]
which fits the hypothesis of the Lemma. Since $T(cv)$ and $-T(-cv)$ are nonzero (they both have magnitude <span>$|c|\cdot ||v||\neq 0$</span>), the Lemma says there exists $j > 0$ such that $T(cv) = j(-T(-cv))$. Now $-c > 0$, so $T(-cv) = -cT(v)$ and hence $T(cv) = jcT(v)$. By comparing magnitudes once again, we get
\\[|c|\cdot ||v|| = ||T(cv)|| = ||jcT(v)|| = j|c|\cdot ||v||.\\]
Therefore, $j = 1$, so $T(cv) = cT(v)$. QED.

**Proposition 2.** For all $v, w\in\mathbb{R}^2$, $T(v + w) = T(v) + T(w)$.

> *Proof.* If $v = w$, then by Proposition 1,
\\[T(v + w) = T(2v) = 2T(v) = T(v) + T(w).\\]
Suppose $v\neq w$. Let $m = \frac{1}{2}(v + w)$. Then $m$ is the midpoint of the line segment between $v$ and $w$, which means <span>$||v - m|| = ||m - w||$</span> and <span>$||v - w|| = ||v - m|| + ||m - w||$</span>. Hence,
\\[||T(v) - T(m)|| = ||T(m) - T(w)||\\]
and
> <div>
> \begin{align*}
>   ||[T(v) - T(m)] + [T(m) - T(w)]|| &= ||T(v) - T(w)|| \\
>   &= ||v - w|| \\
>   &= ||v - m|| + ||m - w|| \\
>   &= ||T(v) - T(m)|| + ||T(m) - T(w)||.
> \end{align*}
> </div>
> The assumption $v\neq w$ implies that $m\neq v$ and $m\neq w$. Hence, $T(v) - T(m)\neq 0$ and $T(m) - T(w)\neq 0$ since $T$ is an isometry. By the Lemma, there exists $c > 0$ such that $T(v) - T(m) = c[T(m) - T(w)]$. Hence,
\\[||T(v) - T(m)|| = c||T(m) - T(w)||.\\]
But $||T(v) - T(m)|| = ||T(m) - T(w)||\neq 0$, so $c = 1$. Therefore,
\\[T(m) = \frac{1}{2}[T(v) + T(w)].\\]
Finally, recalling that $m = \frac{1}{2}(v + w)$, we deduce that
\\[T(v + w) = T(2m) = 2T(m) = T(v) + T(w)\\]
by Proposition 1. QED.

Next, we want to prove that $T$ is [orthogonal](https://en.wikipedia.org/wiki/Orthogonal_transformation), which means $T$ preserves angles between vectors. Symbolically, we want to prove the following result.

**Proposition 3.** Every $v, w\in\mathbb{R}^2$ satisfies $\langle v, w\rangle = \langle T(v), T(w)\rangle$ where $\langle\cdot, \cdot \rangle$ is the standard inner product on $\mathbb{R}^2$ (i.e. the "dot product").

> *Proof.* For any $v, w\in\mathbb{R}^2$,
> <div>
> \begin{align*}
>   ||v + w||^2 &= \langle v + w, v + w\rangle \\
>   &= \langle v, v\rangle + \langle v, w\rangle + \langle w, v\rangle + \langle w, w\rangle \\
>   &= ||v||^2 + 2\langle v, w\rangle + ||w||^2
> \end{align*}
> </div>
> since the inner product on $\mathbb{R}^2$ is symmetric. Similarly,
\\[||T(v) + T(w)||^2 = ||T(v)||^2 + 2\langle T(v), T(w)\rangle + ||T(w)||^2.\\]
Since $T$ is a linear isometry, we have
\\[||v + w||^2 = ||T(v + w)||^2 = ||T(v) + T(w)||^2,\\]
so
\\[||v||^2 + 2\langle v, w\rangle + ||w||^2 = ||T(v)||^2 + 2\langle T(v), T(w)\rangle + ||T(w)||^2.\\]
Hence, $\langle v, w\rangle = \langle T(v), T(w)\rangle$ since <span>$||v|| = ||T(v)||$</span> and <span>$||w|| = ||T(w)||$</span>. QED.

In particular, since the basis vectors $e_1 = (1, 0)$ and $e_2 = (0, 1)$ are orthogonal, the vectors $T(e_1)$ and $T(e_2)$ must also be orthogonal. Since <span>$||T(e_1)|| = ||e_1|| = 1$</span> and <span>$||T(e_2)|| = ||e_2|| = 1$</span>, we know that $T(e_1)$ and $T(e_2)$ must be on the unit circle. Hence, there exists angles $\theta$ and $\gamma$ such that $T(e_1) = (\cos\theta, \sin\theta)$ and $T(e_2) = (\cos\gamma, \sin\gamma)$. The matrix of $T$ is therefore
<div>
\[T = \begin{bmatrix}\cos\theta & \cos\gamma \\ \sin\theta & \sin\gamma\end{bmatrix}.\]
</div>
Our goal now is to compute $\cos\gamma$ and $\sin\gamma$ in terms of $\cos\theta$ and $\sin\theta$. Since $T$ preserves angles, we have that
\\[0 = \langle e_1, e_2\rangle = \langle T(e_1), T(e_2)\rangle = \cos\theta\cos\gamma + \sin\theta\sin\gamma = \cos(\theta - \gamma),\\]
so $\gamma - \theta = \frac{n\pi}{2}$ where $n$ is an odd integer. Because cosine and sine are $2\pi$-periodic, we can assume that $n = 1$ or $n = -1$ without loss of generality.

If $\gamma - \theta = \frac{\pi}{2}$, then trigonometric identities tell us that $\cos\gamma = -\sin\theta$ and $\sin\gamma = \cos\theta$. Hence,
<div>
\[T = \begin{bmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{bmatrix},\]
</div>
so $T$ is a counterclockwise rotation by the angle $\theta$.

If $\gamma - \theta = -\frac{\pi}{2}$, then $\cos\gamma = \sin\theta$ and $\sin\gamma = -\cos\theta$ by trigonometric identities, so
<div>
\[T = \begin{bmatrix}\cos\theta & \sin\theta \\ \sin\theta & -\cos\theta\end{bmatrix}.\]
</div>
Hence, $T$ reflects points across the line passing through the origin that makes a counterclockwise angle of $\frac{\theta}{2}$ with the positive $x$-axis.

With that, we have established that $T$ must be a rotation or a reflection, and we have finished classifying all isometries of $\mathbb{R}^2$.

## Generalizing to $\mathbb{R}^n$

The key Lemma generalizes to $\mathbb{R}^n$ for any $n\geq 1$.

**Generalized Lemma.** Let $v, w\in\mathbb{R}^n\setminus\\{0\\}$ such that <span>$||v + w|| = ||v|| + ||w||$</span>. Then there exists $c > 0$ such that $v = cw$.

> *Proof.* Let $v = (v_1, \dots, v_n)$ and $w = (w_1, \dots, w_n)$. Squaring both sides of <span>$||v + w|| = ||v|| + ||w||$</span> gives
\\[||v + w||^2 = ||v||^2 + ||w||^2 + 2||v||\cdot ||w||.\\]
In terms of the $v_i$ and $w_i$,
\\[\sum_{i=1}^n (v_i^2 + w_i^2 + 2v_iw_i) = \sum_{i=1}^n (v_i^2 + w_i^2) + 2\sqrt{\sum_{i=1}^n v_i^2\sum_{j=1}^n w_j^2}.\\]
Hence,
\\[\sum_{i=1}^n v_iw_i = \sqrt{\sum_{i=1}^n v_i^2 \sum_{j=1}^n w_j^2} = \sqrt{\sum_{i=1}^n\sum_{j=1}^n v_i^2w_j^2}.\\]
When we square both sides, we get
\\[\sum_{i=1}^n\sum_{j=1}^n v_iw_iv_jw_j = \left(\sum_{i=1}^n v_iw_i\right)^2 = \sum_{i=1}^n\sum_{j=1}^n v_i^2w_j^2.\\]
Hence,
\\[\sum_{i=1}^n\sum_{j=1}^n (v_iw_iv_jw_j - v_i^2w_j^2) = 0.\\]
We can rewrite the sum as
\\[\sum_{1\leq i < j\leq n} (2v_iw_iv_jw_j - v_i^2w_j^2 - v_j^2w_i^2) = 0.\\]
Hence,
\\[\sum_{1\leq i < j\leq n} -(v_iw_j - v_jw_i)^2 = 0\\]
and it follows that $v_iw_j = v_jw_i$ for all $i < j$. The desired result now follows by the same argument given in the proof of the original Lemma after we had deduced that $v_1w_2 = v_2w_1$.

The three Propositions also work in exactly the same way in $\mathbb{R}^n$ (their proofs only depend on the Lemma, which we have now shown to be true in $\mathbb{R}^n$). Hence, we obtain the following generalized result.

**Theorem.** If $T$ is an isometry on $\mathbb{R}^n$ such that $T(0) = 0$, then $T$ is an orthogonal linear transformation.

*Corollary.* Let $O(n)$ be the group of orthogonal transformations of $\mathbb{R}^n$, $I(n)$ be the group of isometries on $\mathbb{R}^n$, and $T(n)$ be the group of translations on $\mathbb{R}^n$, with each group operation being function composition. Then $O(n)\cong I(n)/T(n)$.

> *Proof.* The map $\phi(f) = f - f(0)$ is a surjective homomorphism $I(n)\to O(n)$ with kernel $T(n)$.
