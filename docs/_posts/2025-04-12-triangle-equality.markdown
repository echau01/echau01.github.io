---
layout: post
title: The "Triangle Equality" (isometries part 3)
---

My [first post on isometries]({% post_url 2025-03-01-planar-isometries %}) showed that if $T$ is an isometry on $\mathbb{R}^2$ such that $T(0) = 0$, then $T$ an orthogonal linear transformation. We will now generalize this result to all inner product spaces.

I'll briefly review the argument from the original post. We first proved this key lemma:

**Lemma.** If $v, w\in\mathbb{R}^2$ are nonzero and <span>$||v + w|| = ||v|| + ||w||$</span>, then there exists $c > 0$ such that $v = cw$.

Then, we proved that $T$ is linear---this portion of the argument only uses the lemma and the fact that $\mathbb{R}^2$ is a normed vector space. We could replace $\mathbb{R}^2$ with any normed vector space $V$ and the same argument would work (assuming that the Lemma holds if we replace $\mathbb{R}^2$ with $V$). Finally, we proved that every linear isometry on $\mathbb{R}^2$ is orthogonal, and we generalized this result to all inner product spaces in a [follow-up post]({% post_url 2025-04-07-isometries-and-orthogonality %}).

In fact, the only part of the proof that has not already been generalized to arbitrary inner product spaces is the Lemma. This post is dedicated to proving the generalized lemma.

**Generalized Lemma.** Let $V$ be an inner product space. Suppose $v, w\in V\setminus\\{0\\}$ satisfy <span>$||v + w|| = ||v|| + ||w||$</span>. Then there exists a positive scalar $c > 0$ such that $v = cw$.

_Proof._ Since <span>$||v + w|| = ||v|| + ||w||$</span>, we have
<div>
\begin{align*}
    ||v||^2 + 2\text{Re}(\langle v, w\rangle) + ||w||^2 &= ||v + w||^2 \\
    &= (||v|| + ||w||)^2 \\
    &= ||v||^2 + 2||v||\cdot ||w|| + ||w||^2,
\end{align*}
</div>
so $\text{Re}(\langle v, w\rangle) = ||v||\cdot ||w||$. The Cauchy--Schwarz inequality for inner product spaces says that $|\langle v, w\rangle|\leq ||v||\cdot ||w||$, so $|\langle v, w\rangle|\leq \text{Re}(\langle v, w\rangle)$. But clearly
<div>
\begin{align*}
    |\langle v, w\rangle|^2 &= \text{Re}(\langle v, w\rangle)^2 + \text{Im}(\langle v, w\rangle)^2 \\
    &\geq \text{Re}(\langle v, w\rangle)^2,
\end{align*}
</div>
so $|\langle v, w\rangle| = \text{Re}(\langle v, w\rangle)$. Hence, $\text{Im}(\langle v, w\rangle) = 0$, so $\langle v, w\rangle = \text{Re}(\langle v, w\rangle) = ||v||\cdot ||w||$.

Since $v$ and $w$ are nonzero, we know that $||v||$ and $||w||$ are positive. Let $c = \frac{||v||}{||w||} > 0$. We will show that $v = cw$. Note that
<div>
\begin{align*}
    \langle cw, v - cw\rangle &= \langle cw, v\rangle - \langle cw, cw\rangle \\
    &= c\langle w, v\rangle - c^2||w||^2 \\
    &= c||v||\cdot ||w|| - c^2||w||^2 \\
    &= c^2||w||^2 - c^2||w||^2\quad\text{(since $||v|| = c||w||$)}\\
    &= 0.
\end{align*}
</div>
Hence, $cw$ and $v - cw$ are orthogonal. The "Pythagorean Theorem" in inner product spaces says that if $\langle x, y\rangle = 0$, then $||x + y||^2 = ||x||^2 + ||y||^2$. Hence,
<div>
\begin{align*}
    ||v||^2 &= ||cw + (v - cw)||^2 \\
    &= ||cw||^2 + ||v - cw||^2 \\
    &= (c||w||)^2 + ||v - cw||^2 \\
    &= ||v||^2 + ||v - cw||^2,
\end{align*}
</div>
so $||v - cw||^2 = 0$. We conclude that $v - cw = 0$ and hence $v = cw$. QED.

This concludes the proof of our generalized theorem:

**Theorem.** Let $V$ be an inner product space and $f: V\to V$ be an isometry. Then the function $T: V\to V$ defined by $T(v) = f(v) - f(0)$ is an angle-preserving linear transformation.

In fact, we never use the assumption that $f$ maps $V$ to itself. This means we can generalize the theorem even further: if $V$ and $W$ are inner product spaces (over the same field $F\in\\{\mathbb{R}, \mathbb{C}\\}$) and $f: V\to W$ is an isometry, then $f-f(0)$ is linear and angle-preserving.
