# Mackay's Information Theory, Inference, and Learning Algorithms

Solutions to selected problems I found interesting from the book.

Solutions are written up in the `README.md` file for the relevant chapter and displayed as PDFs in `solutions.pdf`. I also run simulations and generate plots for some in the accompanying python files. The markdown may be built to PDF in the Tufte style using pandoc:

```bash
pandoc --standalone -V documentclass=tufte-handout \
    -t pdf chapter_1/README.md -o tmp.pdf
```

You can auto-reload on save if you have `watchexec` installed:

```bash
watchexec -e md "pandoc chapter_1/README.md -o tmp.pdf -V documentclass=tufte-handout"
```

To use advanced elements like margin figures and notes, simply fall back to pure LaTeX, e.g.

```
\marginnote{An unnumbered marginnote.}

![A standard figure. It is constrained to the main text column.](fig.png)

\begin{figure*}
  \includegraphics[width=\linewidth]{placeholder.png}
  \caption{This is a wide figure. It spans across the entire page, including the margin.}
\end{figure*}

\begin{marginfigure}
  \includegraphics{placeholder.png}
  \caption{This figure lives entirely in the right margin.}
\end{marginfigure}

```

(You can also view the markdown through the rendering on GitHub, although more complex elements like marginfigures may fail to load)

## Some thoughts on the book

- This book is brilliant! Mackay was a true polymath and it shows. It's not intuitive why information theory and machine learning deserve to be covered in a single book, but he justifies it extremely well with the overarching Bayesian theme. The way he applies these foundations to answer questions in Physics, Computer Science, and Biology is really special.

- Mackay was a Physicist by training and I sometimes feel a culture clash (in a good way!) between the way he solves problems and the way that's intuitive to me. For example, in problem 1.3, it's straightforward to derive the exact result using the Binomial CDF. I would have stopped here and then used a computer to perform any tedious calculations. However, Mackay pushes ahead with a series of approximations. He first drops terms, then uses Stirling's formula to approximate the Binomial coefficients. It was not obvious to me what the point of all this was -- why bother with this analytical manipulation when we can just use a computer? However, I must admit that working through these approximations really helps give an intuition for how all these fields are connected. I used to think that Physicists were unecessarily obsessed with finding analytical approximations at the expense of prediction accuracy, but now I'm starting to understand that these approximations can give real insight into the problems.
