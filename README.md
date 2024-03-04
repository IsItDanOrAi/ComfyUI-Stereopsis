# ComfyUI-Stereopsis

This is an independent project trying to create a stereopsis effect for ComfyUI (Stable Diffusion).



Side By Side Module for Image Concatenation
Overview

<img width="1723" alt="Side-by-Side" src="https://github.com/IsItDanOrAi/ComfyUI-Stereopsis/assets/162214102/c4b70e1e-56ff-4010-954c-da2371b87903">

The Side_by_side module is a utility designed for concatenating two images side by side into a single image. It is implemented in Python using the PyTorch library, making it suitable for both academic research and industrial applications where image manipulation and processing are required.

Features

    Image Concatenation: Combines two images horizontally, aligning them side by side.
    Input Flexibility: Accepts two images as input, with no restriction on the images' width, but requires them to have the same height and channel depth.
    PyTorch Integration: Utilizes PyTorch for image manipulation, ensuring compatibility with other PyTorch-based pipelines and operations.

Technical Details

    Input Types: The module requires two inputs, each labeled as left_image and right_image. Both inputs are expected to be images, represented as PyTorch tensors.
    Return Types: The output is a single image, which is the result of concatenating the input images side by side.
    Functionality: By leveraging the torch.cat function, it combines the input images along the width dimension, creating a seamless side-by-side image composition.

Integration

    Node Class Mappings: The module is mapped under the name Dan_Stereopsis, enabling its integration into systems that utilize a node-based architecture for image processing or analysis tasks.
    Node Display Name Mappings: For user-friendly interaction within graphical interfaces, the module is titled Side By Side, ensuring intuitive identification and usage by end-users.

Requirements

    PyTorch: As a PyTorch-based module, it requires an environment where PyTorch is installed and configured.
