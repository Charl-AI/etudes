---
title: "Chapter 3: More about Inference"
author: "Solutions and comments by C Jones"
header-includes:
  - \usepackage{graphicx}
  - \usepackage{microtype}
  - \usepackage{booktabs}
---

## 3.1

First, we state Bayes' rule with 'hypothesis' $\mathcal{H} = A$ being that the data $\mathcal{D}$ came from die $A$ and $\mathcal{H} = B$ being die $B$
$$p(\mathcal{H} = A \mid \mathcal{D}) = \frac{p(\mathcal{D} \mid \mathcal{H} = A) p(\mathcal{H
} = A)}{p(\mathcal{D})} =  \frac{p(\mathcal{D} \mid \mathcal{H} = A) p(\mathcal{H = A})}{p(\mathcal{D} \mid \mathcal{H} = A) p(\mathcal{H
} = A) + p(\mathcal{D} \mid \mathcal{H} = B) p(\mathcal{H
} = B)}, $$
where $\mathcal{D} = \{5,3,9,3,8,4,7 \}$. We may assume all rolls are IID, so
$$p(\mathcal{D} \mid \mathcal{H}) = \prod_{x \in \mathcal{D}} p(x \mid \mathcal{H}),$$  
with  $p(x \mid \mathcal{H})$ for each die calculated from the symbol tables given in the book. We can also assume a uniform prior over dice since the text says they were chosen randomly.
\begin{margintable}
\centering
  \begin{tabular}{l c c}
    \toprule
    $x$ & $p(x \mid A)$ & $p(x \mid B)$ \\
    \midrule
    $1$ & $0.30$ & $0.15$  \\
    $2$ & $0.20$ & $0.15$  \\
    $3$ & $0.15$ & $0.10$  \\
    $4$ & $0.10$ & $0.10$  \\
    $5$ & $0.05$ & $0.10$  \\
    $6$ & $0.05$ & $0.10$  \\
    $7$ & $0.05$ & $0.10$  \\
    $8$ & $0.05$ & $0.10$  \\
    $9$ & $0.05$ & $0.05$  \\
    $10$ & $0.00$ & $0.05$  \\
    \bottomrule
  \end{tabular}
\end{margintable}

Now we have this setup, the computational details aren't too interesting. We can just run these numbers through the Bayesian machine to arrive at our answer:
$$p(\mathcal{D} \mid A) = 0.05^4 \times 0.15^2 \times 0.10 = \frac{9}{64 \times 10^7} \approx 1.41 \times 10^{-8};$$
$$p(\mathcal{D} \mid B) = 0.10^6 \times 0.05 = 5 \times 10^{-8};$$
$$p(A \mid \mathcal{D}) \approx 0.22. $$

## 3.3

This problem is tricky because the particle detector only sees particles in a given range. So, unless we're willing to assume the range of the detector is much larger than the decay constant, we must deal with an akwardly truncated distribution.

Let's push ahead with Bayes' rule anyway. We'll write out the likelihood conditioned on $\lambda$ and we'll use the indicator function $\mathbb{1}$ to zero out positions outside the range of the detector. The book states that it is simply an exponential distribution
$$p(x \mid \lambda) = \mathbb{1}_{[1,20)} \frac{k}{\lambda} e^{-\frac{x}{\lambda}}, $$
where $k$ is a normalising constant (some function of lambda that makes the distribution valid). We can compute $k$ by solving the integral
$$1 = \int_{\mathbb{S}(X)} \mathbb{1}_{[1,20)} \frac{k}{\lambda} e^{-\frac{x}{\lambda}} \mathrm{d}x$$
$$ = \int_{1}^{20} \frac{k}{\lambda} e^{-\frac{x}{\lambda}} \mathrm{d}x.$$
And just like that, we've dealt with the hardest part of this problem! All the maths related to truncating the distribution gets absorbed by this integral when we compute $k$. If we had a detector with a different range, it would simply change the limits on this integral. 

Now, just like the last problem, we'll consider the decays as IID 
$$p(\{x_1, \dots, x_N \} \mid \lambda) = \prod_{x \in \{x_1, \dots, x_N\}} p(x \mid \lambda).$$
Finally, we're ready to write down our posterior
$$p(\lambda \mid \{x_1, \dots, x_N \}) = \frac{p(\{x_1, \dots, x_N \} \mid \lambda)p(\lambda)}{p(\{x_1, \dots, x_N\})}. $$
If we assume a uniform prior and ignore the normalising term $p(\{x_1, \dots, x_N\})$ (which is tricky to calculate since it requires an integral over $\lambda$), then we get the result that the posterior is proportional to the likelihood. We can also drop the indicator from the final equation because our observed data is implicitly conditioned on the particles being within range of the detector
$$p(\lambda \mid \{x_1, \dots, x_N \}) \propto p(\{x_1, \dots, x_N \} \mid \lambda)  $$
$$= \prod_{x \in \{x_1, \dots, x_N\}} \mathbb{1}_{[1,20)} \frac{k}{\lambda} e^{-\frac{x}{\lambda}} = \left(\frac{k}{\lambda}\right)^N e^{- \sum_{x \in \{x_1, \dots, x_N\}} \frac{x}{\lambda}}.$$


\begin{marginfigure}
  \includegraphics[width=\linewidth]{chapter_3/assets/particle_surface.pdf}
  \caption{Log likelihood $p(x \mid \lambda)$ for a single particle. Observing a particle at extreme positions provides lots of information about $\lambda$. However, in the middle range, the surface is quite flat, indicating that a single particle detected here does not provide much information about $\lambda$.}
\end{marginfigure}

Note that, since k is a function of $\lambda$, we must remember to recompute it each time we calculate the posterior for a different $\lambda$.

We could treat this full posterior as the solution to the question 'what is $\lambda$'. If we want a point estimate, we could also take the MAP estimate $\hat{\lambda} = \mathrm{argmax}_{\lambda} \quad p(\lambda \mid \{x_1, \dots, x_N \})$.

## 3.8

This is just the Monty Hall problem, but we'll solve it in a Bayesian way. Let $X: \text{prize behind door \{A,B,C\}} \rightarrow \{0,1,2\}$  represent the winning door. We will assume a uniform prior over $X$, i.e. all doors are equally likely to be winners $p(x) = \frac{1}{3} \quad \forall x \in \{0,1,2\}$. Without loss of generality, at the start, we'll select door $A$, with ${p(\text{win}) = p(X=0) = \frac{1}{3}}$. We'll let $Y: \text{Monty opens door } \{A,B,C\} \rightarrow \{0,1,2 \}$ be the door that Monty opens after we've selected our door.

Monty will always open one of the two doors we didn't select. If the prize is behind our door, he selects at random, else he selects the door that doesn't have the prize. We can thus write out $p(y \mid x)$
\begin{table}
\centering
  \begin{tabular}{l |ccc}
    \toprule
    $p(y  \mid x)$ & $Y=0$ & $Y=1$ & $Y=2$ \\
    \midrule
    $X=0$ & $0$ & $0.5$ & $0.5$  \\
    $X=1$ & $0$ & $0$ & $1$  \\
    $X=2$ & $0$ & $1$ & $0$  \\
    \bottomrule
  \end{tabular}
\end{table}

Using the law of total probability, we may compute $p(y) = \sum_{y \in  \{0,1,2 \}} p(y \mid x)p(x)$. Thus $p(y) = 0.5$ if $y \in \{1,2\}$, $0$ otherwise \marginnote{The marginal distribution $p(y)$ should be pretty obvious from the problem's symmetry, but it's worth working it through.}.

We're finally ready to apply Bayes' rule. Again, without loss of generality, let's say that Monty opened door $Y=1$ to simplify the numbers:
$$p(x \mid y) = \frac{p(y\mid x)p(x)}{p(y)} = \frac{2}{3}p(y \mid x);$$
$$p(X=0 \mid Y=1) =  \frac{1}{3};$$
$$p(X=1 \mid Y=1) =  0;$$
$$p(X=2 \mid Y=1) =  \frac{2}{3}.$$
Thus we have the best chance of winning if we switch to door 2. 

## 3.9

When an earthquake opens one of the doors instead of Monty, the maths changes. When Monty opened a door in the last question, he introduced information -- he knows where the prize is and will never choose to open the prize door or the chosen door. The earthquake has no such knowledge. Using the same notation as the last question, we may write 
\begin{table}
\centering
  \begin{tabular}{l |ccc}
    \toprule
    $p(y  \mid x)$ & $Y=0$ & $Y=1$ & $Y=2$ \\
    \midrule
    $X=0$ & $0$ & $0.5$ & $0.5$  \\
    $X=1$ & $0.5$ & $0$ & $0.5$  \\
    $X=2$ & $0.5$ & $0.5$ & $0$  \\
    \bottomrule
  \end{tabular}
\end{table}
Here, the $y=x$ diagonal is zeroed out since we know that the earthquake didn't open the prize door. The rest of the terms are equal by symmetry \marginnote{Note that the $p(y\mid x)$ terms don't have to be exactly $0.5$ to make this argument work, they just have to be equal.} -- we assume that there is equal chance for the earthquake to open any one door as any other. If we run through the maths again, we get $p(x \mid y) = \frac{1}{3} \forall x\in \{0,1,2\}$, thus no advantage in switching.
