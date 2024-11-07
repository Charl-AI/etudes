# MNIST in every language

_I hire not the researcher who has trained 10000 models once, I hire the researcher who has trained 1 model 10000 times_ - Bruce Lee, probably

Are you a deep learning researcher who wants to learn a
new language? Has PhD life turned your brain into mush that can only understand
28\*28 pixel handwritten characters? You've come to the right place!

Here, I implement increasingly unorthodox MNIST classifiers in
increasingly unorthodox languages. Since I am not using any external libraries,
I also have to write everything from scratch, including dataloading, linear algebra,
autograd (if relevant) and model code.
Note that none of the code in this repo leverages GPU acceleration.
Speed is not the priority here.

Currently implemented:

- `lua/` - Standard MLP classifier with a torch-style autograd library
  and custom matrix algebra system.
