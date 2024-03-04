original work : https://github.com/sczhou/CodeFormer

## INTRODUCTION
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


   ![alt text](https://github.com/xlxys/codeFormer-blind-face-restoration/blob/main/images/img1.png?raw=true)


Some existing methods with continuous and discrete methods :
- Pulse, GFP-GAN. (Continuous)
- Nearest neighbor, CodeFormer, Ground truth. (Discrete)


   ![alt text](https://github.com/xlxys/codeFormer-blind-face-restoration/blob/main/images/img2.png?raw=true)


## RELATED WORK

Since faces are highly structured , geometric priors of faces are exploited for blind face
restoration. Some methods introduce in their design facial landmarks, face parsing maps
, facial component heatmaps or 3D shapes. These priors cannot be accurately acquired
from degraded faces , geometric priors are unable to provide rich details for HQ face
restoration.
Reference-based approaches have been proposed to circumvent the above limitations.
For example Li proposes a guided face restoration network, that consists of a wrapping
subnetwork and reconstruction, and a HQ guided image of the same identity as input is
used for better restoring the facial details . The issue is that they are not always available
. we have also :
DFDnet : pre constructs dictionaries composed of HQ facial component features, they are
still insufficient for HQ face restoration, especially for the regions out of the dictionary
scope ( Hair , skin .. ).
VQGAN-based methods : explores a learned HQ dictionary which contains more
generic and rich details of face restoration.
The generative facial priors from pre-trained generators (ex: StyleGAN2) have been
widely explored for blind face restoration. It is utilized via different strategies :
- iterative latent optimization for effective GAN inversion
- direct latent encoding of degraded faces
But to preserve the high fidelity of restored faces is challenging. To relive this issue,
Glean , GPen , GFGAN embed the generative prior into encoder-decoder network
structure with additional structural information from the input as guidance.



## DICTIONARY LEARNING :
The representation with the learned dictionaries has demonstrated its superiority in
image restoration, such as super-resolution and denoising. But they suffer from high
computational costs.
A HQ dictionary has inspired references-based restoration networks : LUT, self-reference,
as well as synthesis methods. Jo and Kim, construct a lookup table (LUT) by transferring
the network output values to a LUT. So a simple retrieval value is needed during
inference.This method of storing HQ textures in the image requires a huge LUT which
limits its practicality.
VQVAE : first to introduce a highly compressed codebook learned by a vector-quantized
autoencoder model.
VQGAN : reduces the size of the codebook without sacrificing its expressiveness, by
adopting adversarial loss and perceptual loss to enhance the perceptual quality .
The codebook automatically learns optimal elements for HQ image reconstructions.
providing superior efficiency and expressiveness as well as circumventing the laborious
dict design . In this paper, They exploit the discrete codebook prior by predicting code
sequences via global modeling. They secure prior effectiveness by fixing the encoder.
METHODOLOGY
The main focus of this work is to exploit a discrete representation space that reduces the
uncertainty of restoration mapping and complements HQ details for the degraded inputs.
They employed a transformer module to model the global composition of natural faces,
by incorporating the idea of vector quantization and pre-train a quantized autoencoder
through self reconstruction to obtain a discrete codebook and the corresponding
decoder.The prior from the codebook combination and decoder is then used for face
restoration.
Based on this prior codebook they employed a transformer, for the accurate prediction of
code combination from the LQ inputs. Also, a Controllable feature transformation
module to exploit a flexible trade-off between restoration quality and fidelity.
The training is divided into 3 steps :
1. Codebook learning
2. Codebook lookup Transformer learning
3. Controllable feature transformation

