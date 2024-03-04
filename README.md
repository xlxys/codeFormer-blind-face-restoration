

# INTRODUCTION
 Face images captured in the wild often suffer from various degradation such as
compression, noise and blur which causes a loss of information.
Blind face restoration is a highly ill-posed problem that often requires auxiliary guidance
to improve the mapping from degraded inputs to desired outputs.
In order to do that they reduced the uncertainty and ambiguity of restoration mapping
by casting blind face restoration as a code prediction task.
To mitigate the ill-posedness of the problem, they used various priors :
- geometric priors - reference priors - generative priors
These approaches often suffer from high sensitivity to degradation or limited prior
expressiveness. This implies insufficient guidance for face restoration. Most recently
based on the generative prior, some methods project the degraded faces into a
continuous infinite space via iterative latent optimization or discrete latent encoding.


![alt text](https://github.com/xlxys/codeFormer-blind-face-restoration/blob/main/img1.png?raw=true)
