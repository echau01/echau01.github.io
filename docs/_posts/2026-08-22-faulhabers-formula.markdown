---
layout: "post"
title: "Finding a formula for $1^k + 2^k + ... + n^k$"
---

In school, you probably had to memorize the formula
\\[1 + 2 + \dots + n = \frac{n(n+1)}{2}.\\]
If your math teacher was particularly enthusiastic, you may also have seen the formulas
\\[1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}\\]
and
\\[1^3 + 2^3 + \dots + n^3 = \left(\frac{n(n+1)}{2}\right)^2.\\]
From these few formulas, we might conjecture that such a formula exists for each natural number $k$. More specifically, for the general sum
\\[S_k(n) := 1^k + 2^k + \dots + n^k,\\]
the pattern seems to be that $S_k(n)$ is always a polynomial in $n$ of degree $k + 1$. This follows fairly easily by induction, as we shall now see.

**Theorem 1.** For all integers $k\geq 0$, there exists a polynomial $p_k$ of degree $k + 1$ such that $p_k(n) = \sum_{j=1}^n j^k$ for all integers $n\geq 0$. Moreover, the leading coefficient of $p_k$ is $\frac{1}{k+1}$. (By convention, the _empty sum_ $\sum_{j=1}^0 j^k$ is defined to be $0$.)

> _Proof._ In the base case $k = 0$, the polynomial $p_0(x) = x$ satisfies the conclusion of the theorem. Indeed, we have $\sum_{j=1}^n j^0 = n$ for all $n$, and the leading coefficient of $p_0$ is $\frac{1}{0 + 1} = 1$.
>
> Now pick an arbitrary value $k\geq 1$, and suppose the theorem holds for all smaller values of $k$. Then for all $n\geq 0$,
> <div>
\begin{align*}
    S_{k+1}(n) &= \sum_{j=1}^n j^{k+1} \\
    &= \sum_{j=0}^{n-1} (j+1)^{k+1} \\
    &= 1 - (n + 1)^{k+1} + \sum_{j=1}^n (j + 1)^{k+1} \\
    &= 1 - \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} + \sum_{j=1}^n \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}j^{\ell}\quad\text{(by the binomial theorem)} \\
    &= 1 - \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} + \sum_{\ell=0}^{k+1}\sum_{j=1}^n \binom{k+1}{\ell}j^{\ell}\quad\text{(interchanging the order of summation over $[1, n]\times [0, k+1]$)} \\
    &= 1 - \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} + \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}\sum_{j=1}^n j^{\ell} \\
    &= 1 - \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} + \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}S_{\ell}(n) \\
    &= 1 - \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} + \sum_{\ell=0}^k \binom{k+1}{\ell}S_{\ell}(n) + S_{k+1}(n).
\end{align*}
> </div>
> Therefore,
\\[0 = 1 - \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} + \sum_{\ell=0}^k \binom{k+1}{\ell}S_{\ell}(n).\\]
By extracting the $S_k(n)$ term from the last sum and isolating it, we see that
> <div>
\begin{align*}
    (k + 1)S_k(n) &= \sum_{\ell=0}^{k+1} \binom{k+1}{\ell}n^{\ell} - \sum_{\ell=0}^{k-1} \binom{k+1}{\ell}S_{\ell}(n) - 1 \\
    &= n^{k+1} + \sum_{\ell=0}^k \binom{k+1}{\ell}n^{\ell} - \sum_{\ell=0}^{k-1} \binom{k+1}{\ell}S_{\ell}(n) - 1.
\end{align*}
> </div>
Hence,
\\[S_k(n) = \frac{1}{k+1}\left[n^{k+1} + \sum_{\ell=0}^k \binom{k+1}{\ell}n^{\ell} - \sum_{\ell=0}^{k-1} \binom{k+1}{\ell}S_{\ell}(n) - 1\right].\\]
By the inductive hypothesis, for all $0\leq\ell\leq k-1$, the polynomial $p_{\ell}$ exists and has degree $\ell + 1$. Therefore, we can define
\begin{equation}\label{p_k definition}
    p_k(x) = \frac{1}{k+1}\left[x^{k+1} + \sum_{\ell=0}^k \binom{k+1}{\ell}x^{\ell} - \sum_{\ell=0}^{k-1} \binom{k+1}{\ell}p_{\ell}(x) - 1\right].
\end{equation}
Note that $p_k$ is a polynomial because it is the sum of polynomials. Since $p_{\ell}(n) = S_{\ell}(n)$ for all $0\leq \ell\leq k-1$ and $n\geq 0$, we see that $p_k(n) = S_k(n)$ for all $n\geq 0$. All the polynomials $p_{\ell}$ where $\ell\leq k-1$ have degree at most $k$. Therefore, each term after the initial $x^{k+1}$ term in equation \eqref{p_k definition} has degree at most $k$, so $p_k$ has degree $k+1$, and the leading coefficient is $\frac{1}{k+1}$. $\square$

For all $k$, write the polynomial $p_k$ generically as
\begin{equation}\label{p_k coefficient definition}
    p_k(x) = c_0^{(k)}x^{k + 1} + c_1^{(k)}x^k + \cdots + c_{k + 1}^{(k)} = \sum_{j=0}^{k + 1} c_j^{(k)}x^{k + 1 - j}
\end{equation}
where the $c_j^{(k)}$ are the coefficients. (Note that the "$(k)$" superscript is **not** an exponent, but rather a second index.) We now focus on studying the $c_j^{(k)}$. Note that the constant term is $c_{k + 1}^{(k)} = p_k(0) = S_k(0) = 0$, so we actually have
\\[p_k(x) = \sum_{j=0}^k c_j^{(k)}x^{k+1-j}.\\]
Substituting the above into equation \eqref{p_k definition} gives
\begin{equation}\label{p_k equation}
    p_k(x) = \frac{1}{k+1}\left[x^{k+1} + \sum_{\ell=0}^k \binom{k+1}{\ell}x^{\ell} - \sum_{\ell=0}^{k-1} \binom{k+1}{\ell}\sum_{j=0}^{\ell}c_j^{(\ell)}x^{\ell + 1 - j} - 1\right].
\end{equation}

We already know that $c_0^{(k)} = \frac{1}{k+1}$ and that $c_{k+1}^{(k)} = S_k(0) = 0$. Now let $1\leq m\leq k$. We will obtain a recursive formula for $c_m^{(k)}$ by collecting all the $x^{k + 1 - m}$ terms in equation \eqref{p_k equation} and summing their coefficients.

The summation $\sum_{\ell=0}^k \binom{k+1}{\ell}x^{\ell}$ contributes one $x^{k + 1 - m}$ term with coefficient $\binom{k+1}{k + 1 - m} = \binom{k + 1}{m}$.

The double sum $\sum_{\ell=0}^{k-1} \binom{k+1}{\ell}\sum_{j=0}^{\ell}c_j^{(\ell)}x^{\ell + 1 - j}$ contributes one $x^{k + 1 - m}$ term with coefficient $\binom{k+1}{\ell}c_{\ell-k+m}^{(\ell)}$ for every iteration of the outer sum $\sum_{\ell=0}^{k-1}$ where $\ell\geq k-m$. To see why, consider which values of $j\in [0, \ell]$ satisfy $\ell + 1 - j = k + 1 - m$. Solving for $j$ gives $j = \ell - k + m$. Since $j\geq 0$, we require $\ell\geq k - m$, and since $j\leq\ell$, we require $m\leq k$ which is already true by assumption. Hence, for each value of $\ell\geq k - m$, we get one $x^{k + 1 - m}$ term when $j = \ell - k + m$.

Therefore, the sum of the coefficients of all $x^{k + 1 - m}$ terms is
\begin{equation}\label{coefficient recursive equation}
    c_m^{(k)} = \frac{1}{k+1}\left[\binom{k + 1}{m} - \sum_{\ell=k-m}^{k-1} \binom{k+1}{\ell}c_{\ell-k+m}^{(\ell)}\right].
\end{equation}
At this point, we are ready to compute $c_m^{(k)}$ for specific values of $1\leq m\leq k$. Let's start with $m = 1$: we have
<div>
\begin{align*}
    c_1^{(k)} &= \frac{1}{k+1}\left[\binom{k+1}{1} - \sum_{\ell=k-1}^{k-1} \binom{k+1}{\ell}c_{\ell-k+1}^{(\ell)}\right] \\
    &= \frac{1}{k+1}\left[(k + 1) - \binom{k+1}{k-1}c_0^{(k-1)}\right] \\
    &= \frac{1}{k+1}\left((k + 1) - \frac{(k+1)k}{2}\cdot \frac{1}{k}\right) \\
    &= 1 - \frac{1}{2} \\
    &= \frac{1}{2}
\end{align*}
</div>
for all $k\geq 1$. So now we know that the second coefficient of $p_k$ is always $\frac{1}{2}$ (for example, $p_1(x) = \frac{1}{2}x^2 + {\color{red}\frac{1}{2}} x$ and $p_2(x) = \frac{1}{3}x^3 + {\color{red}\frac{1}{2}}x^2 + \frac{1}{6}x)$. Let's compute the $m = 2$ and $m = 3$ cases:
<div>
\begin{align*}
    c_2^{(k)} &= \frac{1}{k+1}\left[\binom{k+1}{2} - \binom{k+1}{k-2}c_0^{(k-2)} - \binom{k+1}{k-1}c_1^{(k-1)}\right] \\
    &= \frac{1}{k+1}\left[\frac{(k+1)k}{2} - \frac{(k+1)(k)(k-1)}{6}\cdot\frac{1}{k-1} - \frac{(k+1)k}{2}\cdot\frac{1}{2}\right] \\
    &= k\left(\frac{1}{2} - \frac{1}{6} - \frac{1}{4}\right) \\
    &= \frac{1}{12}k
\end{align*}
</div>
for all $k\geq 2$, and
<div>
\begin{align*}
    c_3^{(k)} &= \frac{1}{k+1}\left[\binom{k+1}{3} - \binom{k+1}{k-3}c_0^{(k-3)} - \binom{k+1}{k-2}c_1^{(k-2)} - \binom{k+1}{k-1}c_2^{(k-1)}\right] \\
    &= \frac{1}{k+1}\left[\frac{(k+1)(k)(k-1)}{6} - \frac{(k+1)(k)(k-1)(k-2)}{24}\cdot\frac{1}{k-2} - \frac{(k+1)(k)(k-1)}{6}\cdot\frac{1}{2} - \frac{(k+1)k}{2}\cdot \frac{1}{12}(k-1)\right] \\
    &= k(k-1)\left(\frac{1}{6} - \frac{1}{24} - \frac{1}{12} - \frac{1}{24}\right) \\
    &= 0
\end{align*}
</div>
for all $k\geq 3$. A pattern is emerging: it looks like $c_j^{(k)}$ is always equal to $k(k-1)\cdots (k-j+2)$ multiplied by some constant. Indeed, we have $\binom{k+1}{j} = (k+1)[{\color{red}k(k-1)\cdots (k-j+2)}]$, and every term in the sum $\sum_{\ell=k-m}^{k-1} \binom{k+1}{\ell}c_{\ell-k+m}^{(\ell)}$ always seems to simplify to $(k+1)[{\color{red}k(k-1)\cdots (k-j+2)}]$ times some constant. We state this pattern as the following theorem.

**Theorem 2.** There exists a sequence of constants $a_0, a_1, a_2, a_3, \dots$ such that for all integers $j, k$ where $0\leq j\leq k$,
\\[c_j^{(k)} = \frac{k!}{(k-j+1)!}a_j.\\]

_Remark._ Note the order of the quantifiers: the sequence $a_0, a_1, a_2, a_3, \dots$ is _independent_ of any variables. They are pure constants. From our computation of $c_1^{(k)}$, $c_2^{(k)}$, and $c_3^{(k)}$, we can see that $a_1 = \frac{1}{2}$, $a_2 = \frac{1}{12}$, and $a_3 = 0$.

Before embarking on the proof, it will be helpful to figure out exactly what the constants $a_j$ are. Fix $k\geq 0$. If the theorem is true, then by taking $j = k$, we have
\\[c_k^{(k)} = \frac{k!}{(k - k + 1)!}a_k = k!a_k,\\]
so $a_k = \frac{1}{k!}c_k^{(k)}$. This is what $a_k$ _must be_ if there is any hope of the theorem being true, so now we know how to define the sequence $\\{a_j\\}$ in the proof.

> _Proof._ For all $j\geq 0$, define $a_j = \frac{1}{j!}c_j^{(j)}$. We now prove the theorem by induction on $k\geq 0$.
>
> Let $k = 1$ and suppose $0\leq j\leq k$. Then $j = 0$. Hence, $a_j = a_0 = \frac{1}{0!}c_0^{(0)} = c_0^{(0)}$, so
\\[c_j^{(k)} = c_0^{(0)} = \frac{1!}{(1 - 0 + 1)!}c_0^{(0)} = \frac{k!}{(k - j + 1)!}a_j.\\]
Therefore, the theorem is true for $k = 0$.
>
> Pick an arbitrary value $k\geq 1$ and suppose the theorem holds for all smaller values of $k$. If $j = 0$, then since $a_0 = \frac{1}{0!}c_0^{(0)} = 1$, we have that
\\[c_j^{(k)} = c_0^{(k)} = \frac{1}{k+1} = \frac{k!}{(k - 0 + 1)!}a_0 = \frac{k!}{(k - j + 1)!}a_j.\\]
Hence, the theorem holds for $j = 0$. Now fix $1\leq j\leq k$. Using equation \eqref{coefficient recursive equation} and the inductive hypothesis, we have
> <div>
\begin{align*}
    c_j^{(k)} &= \frac{1}{k+1}\left[\binom{k + 1}{j} - \sum_{\ell=k-j}^{k-1} \binom{k+1}{\ell}c_{\ell-k+j}^{(\ell)}\right] \\
    &= \frac{1}{k+1}\left[\binom{k + 1}{j} - \sum_{\ell=k-j}^{k-1} \binom{k+1}{\ell}\left(\frac{\ell!}{(\ell-(\ell-k+j)+1)!}a_{\ell-k+j}\right)\right] \\
    &= \frac{1}{k+1}\left[\binom{k+1}{j} - \sum_{\ell=k-j}^{k-1} \frac{(k+1)!}{(k + 1 - \ell)!}\left(\frac{1}{(k-j+1)!}a_{\ell-k+j}\right)\right] \\
    &= \frac{1}{k+1}\left[\binom{k+1}{j} - \frac{(k+1)!}{(k-j+1)!}\sum_{\ell=k-j}^{k-1} \frac{a_{\ell-k+j}}{(k+1-\ell)!}\right] \\
    &= \frac{k!}{j!(k+1-j)!} - \frac{k!}{(k-j+1)!}\sum_{\ell=k-j}^{k-1} \frac{a_{\ell-k+j}}{(k+1-\ell)!} \\
    &= \frac{k!}{(k-j+1)!}\left(\frac{1}{j!} - \sum_{\ell=k-j}^{k-1} \frac{a_{\ell-k+j}}{(k+1-\ell)!}\right).
\end{align*}
> </div>
> The proof will be complete if we can prove the recursive relation
\begin{equation}\label{a_j recursive equation}
    a_j = \frac{1}{j!} - \sum_{\ell=k-j}^{k-1} \frac{a_{\ell-k+j}}{(k+1-\ell)!}
\end{equation}
for all $1\leq j\leq k$. We split the proof to an independent Lemma.

**Lemma 3.** Define $a_j = \frac{1}{j!}c_j^{(j)}$ for all $j\geq 0$. Then equation \eqref{a_j recursive equation} holds for all integers $j, k$ where $1\leq j\leq k$.

> _Proof._ This is a simple computation. First, observe that
> <div>
\begin{align*}
    \frac{1}{j!} - \sum_{\ell=k-j}^{k-1} \frac{a_{\ell-k+j}}{(k+1-\ell)!} &= \frac{1}{j!} - \sum_{\ell=k-j}^{k-1} \frac{c_{\ell-k+j}^{(\ell-k+j)}}{(\ell-k+j)!(k+1-\ell)!} \\
    &= \frac{1}{j!} - \sum_{\ell=0}^{j-1} \frac{c_{\ell}^{(\ell)}}{\ell!(j+1-\ell)!}\quad\text{(by shifting the index $\ell\mapsto \ell-k+j$)} \\
    &= \frac{1}{j!} - \sum_{\ell=0}^{j-1} \frac{1}{(j+1)!}\binom{j+1}{\ell}c_{\ell}^{(\ell)} \\
    &= \frac{1}{j!}\left(1 - \frac{1}{j+1}\sum_{\ell=0}^{j-1} \binom{j+1}{\ell}c_{\ell}^{(\ell)}\right).
\end{align*}
> </div>
> We now invoke equation \eqref{coefficient recursive equation} to deduce that
\\[c_j^{(j)} = \frac{1}{j+1}\left(\binom{j+1}{j} - \sum_{\ell=0}^{j-1} \binom{j+1}{\ell} c_{\ell}^{(\ell)}\right) = 1 - \frac{1}{j+1}\sum_{\ell=0}^{j-1} \binom{j+1}{\ell}c_{\ell}^{(\ell)}.\\]
Therefore,
\\[\frac{1}{j!} - \sum_{\ell=k-j}^{k-1} \frac{a_{\ell-k+j}}{(k+1-\ell)!} = \frac{1}{j!}c_j^{(j)} = a_j\\]
as required. This completes the proof of the Lemma and consequently Theorem 2. $\square$

To conclude, we now have that
<div>
\begin{align*}
    p_k(x) &= \frac{1}{k+1}x^{k+1} + \sum_{j=1}^k c_j^{(k)}x^{k-j+1}\quad\text{(recall that $c_{k+1}^{(k)} = 0$)} \\
    &= \frac{1}{k+1}x^{k+1} + \sum_{j=1}^k \frac{k!}{(k-j+1)!}a_jx^{k-j+1} \\
    &= \frac{1}{k+1}x^{k+1} + \sum_{j=1}^k \frac{k!}{j!(k-j+1)!}c_j^{(j)}x^{k-j+1} \\
    &= \frac{1}{k+1}\left(x^{k+1} + \sum_{j=1}^k \binom{k+1}{j}c_j^{(j)}x^{k-j+1}\right) \\
    &= \frac{1}{k+1}\sum_{j=0}^k \binom{k+1}{j}c_j^{(j)}x^{k-j+1}\quad\text{(since $c_0^{(0)} = 1$)}
\end{align*}
</div>
for all $k\geq 0$.

The final expression we have obtained for $p_k(x)$ is called [Faulhaber's formula](https://en.wikipedia.org/wiki/Faulhaber%27s_formula). It is standard to define $B_j^+ := c_j^{(j)}$ for all $j\geq 0$, so that Faulhaber's formula is
\\[\boxed{p_k(x) = \frac{1}{k+1}\sum_{j=0}^k \binom{k+1}{j}B_j^+x^{k-j+1}.}\\]
The numbers $B_j^+$ are known as the _Bernoulli numbers_ and are widely studied; you can read more about them on their [Wikipedia page](https://en.wikipedia.org/wiki/Bernoulli_number). There is a similar sequence of numbers $B_j^-$ which are also called the Bernoulli numbers and are identical to $B_j^+$ except when $j = 1$, where $B_j^- = -\frac{1}{2}$ and $B_j^+ = \frac{1}{2}$. Therefore, the $B_j^+$ are usually called the _second_ Bernoulli numbers.

Faulhaber's formula leads to a fairly easy dynamic-programming algorithm to compute the polynomial $p_k$ (represented as a list of coefficients $[c_0^{(k)}, c_1^{(k)}, \dots, c_k^{(k)}]$) in $O(k^2)$ arithmetic operations.

## Exercises for the reader

(1) Prove that
\\[\sum_{\ell=0}^j \binom{j+1}{\ell} B_{\ell}^+ = j + 1.\\]

The remaining exercises deal with exponential generating functions, which are [formal power series](https://en.wikipedia.org/wiki/Formal_power_series) of the form $\sum_{n=0}^{\infty} a_n\frac{x^n}{n!}$. While these look like functions of $x$, it is important to note that generating functions are actually algebraic objects and do not have any inherent analytical properties.

(2) Let $f(x) := \sum_{n=0}^{\infty} B_n^+\frac{x^n}{n!}$ be the exponential generating function of the Bernoulli numbers $B_n^+$. Define $e^x := \sum_{n=0}^{\infty} \frac{x^n}{n!}$ and $g(x) := \sum_{n=0}^{\infty} \frac{1}{n+1}\frac{x^n}{n!}$. Prove that $xg(x) = e^x - 1$. Using the fact that the product of two exponential generating functions $A(x) = \sum_{n=0}^{\infty} a_n\frac{x^n}{n!}$ and $B(x) = \sum_{n=0}^{\infty} b_n\frac{x^n}{n!}$ is
\\[A(x)B(x) = \sum_{n=0}^{\infty} \left(\sum_{k=0}^n \binom{n}{k}a_{n-k}b_k\right)\frac{x^n}{n!},\\]
prove that $g(x)f(x) = e^x$.

_Remark._ The equations $xg(x) = e^x - 1$ and $g(x)f(x) = e^x$ naturally lead us to write $g(x) = \frac{e^x - 1}{x}$ and $f(x) = \frac{e^x}{g(x)} = \frac{xe^x}{e^x - 1}$. However, we are working in the [ring of formal power series](https://en.wikipedia.org/wiki/Formal_power_series#The_ring_of_formal_power_series) $\mathbb{R}[[x]]$, where $x$ and $e^x - 1$ do not actually have multiplicative inverses. Nevertheless, the notation $\frac{e^x - 1}{x}$ and $\frac{xe^x}{e^x - 1}$ is still completely fine because $\mathbb{R}[[x]]$ is an [integral domain](https://en.wikipedia.org/wiki/Integral_domain). This property means that $g(x) = \frac{e^x - 1}{x}$ is the _unique_ element whose product with $x$ is $e^x - 1$, and similarly, $f(x) = \frac{xe^x}{e^x - 1}$ is the _unique_ element whose product with $e^x - 1$ is $xe^x$. For additional practice working with this kind of algebra, here is a supplemental exercise: justify the equation $\frac{e^x}{g(x)} = \frac{xe^x}{e^x - 1}$ formally, and compare with how you would justify it "informally" (e.g. by multiplying by $\frac{x}{x}$).

(3) Prove that $f(x) - f(-x) = x$ (you can use without proof the fact that any equation involving $f(x)$ also holds for $f(-x)$ by replacing $x$ with $-x$ everywhere). Deduce that
\begin{equation}\label{relation between the two Bernoulli number types}
    B_n^+ - (-1)^nB_n^+ = \begin{cases}1 & \text{if $n=1$} \\\\ 0 & \text{if $n\neq 1$,}\end{cases}
\end{equation}
and conclude that $B_n^+ = 0$ for all odd $n > 1$.

_Remark._ The numbers $B_n^- := (-1)^nB_n^+$ are the other variant of Bernoulli numbers which we mentioned in the conclusion of this post. From equation \eqref{relation between the two Bernoulli number types}, it immediately follows that $B_n^- = B_n^+$ for all $n\neq 1$, and for $n = 1$ we have $B_1^- = B_1^+ - 1 = -\frac{1}{2}$.

(4) Prove that
\\[\sum_{j=0}^k \binom{k+1}{j}(-1)^jB_j^+ = \begin{cases}1 & \text{if $k=0$} \\\\ 0 & \text{if $k\neq 0$.}\end{cases}\\]
Hence, prove that $p_k(-1) = 0$ for all $k\neq 0$.

(5) Prove that
\\[\sum_{j=0}^k \binom{k}{j}(-1)^jB_j^+ = B_k^+\\]
(hint: consider the product $f(-x)e^x$).

(6) For all $k\geq 0$, let
\\[q_k(x) := p_k(x-1) = q_0^{(k)}x^{k+1} + q_1^{(k)}x^k + \cdots + q_k^{(k)}x + q_{k+1}^{(k)}\\]
where the $q_j^{(k)}$ are coefficients. Prove that $q_k^{(k)} = (-1)^kB_k^+$ for all $k\geq 0$. Conclude that $p_k(x)$ is divisible by $x^2(x+1)^2$ for all odd $k > 1$.
