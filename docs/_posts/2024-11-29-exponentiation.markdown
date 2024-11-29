---
layout: post
title: "The story of exponentiation"
---

# The basics

In its simplest form, exponentiation is repeated multiplication in the same way that multiplication is repeated addition. Just as $2\times 3$ is equal to $2 + 2 + 2$, so is $2^3$ equal to $2\times 2\times 2$. Hence we make this basic definition:

**Definition of positive-integer exponents.** If $b$ is any number (which we will call the _base_) and $n$ is a positive integer (which we will call the _exponent_), then
\\[b^n = \underbrace{b\times b\times \dots\times b}_{\text{$n$ times}}.\\]

There are a few shortcuts that help us simplify operations with exponents. They look like this:
\\[2^3 \times 2^2 = (2\times 2\times 2)\times (2\times 2) = 2^5 = 2^{3+2}\tag{1}\\]
\\[2^5 \div 2^2 = (2\times 2\times 2\times \cancel 2\times \cancel 2)\div (\cancel 2\times \cancel 2) = 2\times 2\times 2 = 2^3 = 2^{5-2}\tag{2}\\]
\\[(2^2)^3 = (2\times 2) \times (2\times 2) \times (2\times 2) = 2^{2 + 2 + 2} = 2^{2\times 3}\tag{3}\\]

We have only seen positive exponents so far, but we can actually extend our concept of exponentiation to include the zero exponent and negative exponents. Rule (2) will be the key here. First, observe that 
\\[2^0 = 2^{1 - 1} = 2^1\div 2^1 = 1.\\]
Then, for any positive integer $n$,
\\[2^{-n} = 2^{0 - n} = 2^0\div 2^n = \frac{1}{2^n}.\\]
Note that we don't have to use $2$ as our base; we can play this game with any non-zero base. (This argument does not quite work if the base is $0$ because we can't divide by $0$.)

Let's state our new observations:

**Definition of the zero exponent.** If $b$ is any non-zero number, then
\\[b^0 = 1.\\]

**Definition of negative-integer exponents.** If $b$ is any non-zero number and $n$ is a positive integer, then
\\[b^{-n} = \frac{1}{b^n}.\\]

At this point, we no longer need rule (2), since it is a consequence of rules (1) and (3):
\\[b^{m-n} = b^{m + (-n)} \stackrel{(1)}{=} b^m(b^{-n}) \stackrel{(3)}{=} b^m(b^n)^{-1} = b^m\left(\frac{1}{b^n}\right) = \frac{b^m}{b^n}.\\]

Rule (3) allows us to go even further: we can start thinking about non-integer exponents. Imagine that we want to assign a value to the expression $2^{1/3}$. Call this value $y$. Then
\\[y^3 = (2^{1/3})^3 = 2^{(1/3) \times 3} = 2^1 = 2.\\]
So $y$ is the cube-root of $2$. But remember that we set $y$ to be $2^{1/3}$. Therefore, $2^{1/3}$ is equal to $\sqrt[3]{2}$.

Let's generalize: if $b$ is any positive number and $n$ is a positive integer, then $b^{1/n}$ is equal to $\sqrt[n]{b}$, the $n$-th root of $b$. We want $b$ to be positive (at least for now) because problems arise with expressions like $(-1)^{1/2}$, which would be equal to $\sqrt{-1}$ (an imaginary number!).

What if the numerator is not $1$? We can apply rule (3) again: if $m$ is any integer and $n$ is a positive integer, then
\\[b^{m/n} = b^{(1/n)\times m} = (b^{1/n})^m = (\sqrt[n]{b})^m.\\]
We have now justified the definition of rational exponents.

**Definition of rational exponents.** Let $b$ be a positive number and $q$ be a rational number. This means $q$ can be written as a fraction $\frac{m}{n}$ where $m$ is an integer and $n$ is a positive integer. We now define
\\[b^q = (\sqrt[n]{b})^m.\\]

At this point, we should take a step back and remember that the exponent rules (1), (2), and (3) were only proved in the case where all exponents are positive integers. Do the same exponent rules still work when exponents can not only be negative but can also be fractions? The answer is that the exponent rules do work, but that is something we would have to _prove_ in order to be sure that "rational exponents" are not self-contradictory.

There is another subtle issue related to the fact that a rational number $q$ can have multiple fractional representations. For example, $\frac{1}{2}$ is equal to $\frac{3}{6}$. In order for rational exponents to make any sense, we need $2^{1/2}$ and $2^{3/6}$ to be the same, which can only be true if $\sqrt{2} = (\sqrt[6]{2})^3$. To verify that the definition of $b^{m/n}$ is consistent, we would need to check that if $\frac{m}{n} = \frac{p}{q}$, then $(\sqrt[n]{b})^m = (\sqrt[q]{b})^p$ for any $b > 0$.

# On to the fun stuff

Everything we have seen until now is taught in high school. But readers have probably seen expressions like $2^{\sqrt{3}}$ or the famous $e^{i\pi}$ --- note that $\sqrt{2}$ is an irrational number, and $i\pi$ is not even a real number! So the story is not done yet; there is still a lot to cover beyond the basics that we have seen so far.

Real-valued exponents aren't too hard to conceptualize --- but we need calculus to do so. Take the example of $2^{\sqrt{3}}$. Any real number can be "approached" by a sequence of rational numbers. For example, consider $\sqrt{3}$, which has the decimal expansion $1.73205\dots$. The sequence
\\[\\{1, 1.7, 1.73, 1.732, 1.7320, 1.73205, \dots\\}\\]
is a sequence of rational numbers that converges to $\sqrt{3}$. We now consider the sequence
\\[S = \\{2^1, 2^{1.7}, 2^{1.73}, 2^{1.7320}, 2^{1.73205}, \dots,\\}\\]
which also converges to a real number $L$. This number $L$ is what we call $2^{\sqrt{3}}$.

**Definition of real exponents.** Let $b > 0$ and $x$ be real numbers. Let $\\{q_1, q_2, q_3, \dots\\}$ be a sequence of rational numbers such that $\lim_{n\to\infty} q_n = x$. Then
\\[b^x = \lim_{n\to\infty} b^{q_n}.\\]

Showing that this definition makes sense involves a few things:
- We need to prove that every real number $x$ really does have a rational sequence $\\{q_n\\}$ that converges to $x$.
- We need to prove that $\lim_{n\to\infty} b^{q_n}$ actually exists.
- We need to prove that if $\\{q_n\\}$ and $\\{r_n\\}$ are two rational sequences that converge to the same real number $x$, then $\lim_{n\to\infty} b^{q_n} = \lim_{n\to\infty} b^{r_n}$ (otherwise there would be two potential values for $b^x$).

All of these are standard exercises for a real analysis class. Also, we can prove that the exponent laws still hold.

Now we come to what is probably the most important theorem concerning real exponents.

**Theorem.** The equation
\\[e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}\\]
holds for all real numbers $x$.

We can use the properties of uniform convergence to prove that $\frac{d}{dx}e^x = e^x$. Hence, $e^x$ is strictly increasing, which means it is invertible as a function $\mathbb{R}\to (0, \infty)$. The inverse function is the "natural" logarithm $\log: (0, \infty)\to\mathbb{R}$, which is indispensable in math. The chain rule, together with the identity $x = e^{\ln(x)}$ and exponent rule (3), gives the famous differentiation rules
\\[\frac{d}{dx}b^x = b^x\log(b)\\]
and
\\[\frac{d}{dx}x^c = cx^{c-1}.\\]

# Complex exponents in brief

We know that $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ converges to $e^x$ for all real $x$. Since this power series has an infinite radius of convergence, it converges for every _complex_ number $x$. Hence, we define
\\[e^x := \sum_{n=0}^{\infty} \frac{x^n}{n!}\\]
for all complex numbers $x$. From here, we can prove the famous Euler identity: $e^{i\theta} = \sin(\theta) + i\cos(\theta)$ for all $\theta\in\mathbb{R}$.

Things get quite complicated from here. It is possible to make sense of expressions like $(-1)^i$ as follows:

1. First, write $(-1)^i = e^{i\log(-1)}$. This immediately raises the question of what $\log(-1)$ is.

2. In the complex numbers, $\log(-1)$ is a _multivalued_ expression: it is the set of all $z\in\mathbb{C}$ such that $e^z = -1$. Hence,
\\[\log(-1) = \\{\dots, -3i\pi, -i\pi, i\pi, 3i\pi, \dots\\} = e^{(2n + 1)i\pi}\text{ where $n\in\mathbb{Z}$.}\\]

3. Therefore,
\\[(-1)^i = e^{i\log(-1)} = e^{i(2n+1)i\pi} = e^{-(2n+1)\pi}\\]
where $n$ ranges through $\mathbb{Z}$. So $(-1)^i$ has _infinitely many values!_

We can pick a "branch" of the logarithm to select a single value for $\log(-1)$ and hence for $(-1)^i$. The map $z\mapsto (-1)^z$ is then a single-valued function that we can do calculus on.

In all of this complexity, the exponent rules no longer hold in general, unless we add some restrictions.

# In conclusion...

Remember how we began this story: by defining exponentiation as repeated multiplication. Now look at where we ended up, having brought limits and power series and multivalued functions into the mix. By extending the definition of exponents to larger and larger sets of numbers, we introduced more and more complexity until the original concept of repeated multiplication seems to have disappeared. However, it is important to remember that repeated multiplication is ultimately the foundation of all the extensions we made.
