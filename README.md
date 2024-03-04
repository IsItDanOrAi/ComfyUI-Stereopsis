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



Frame Delay Module for Image Sequences
Overview

<img width="1196" alt="Frame Delay" src="https://github.com/IsItDanOrAi/ComfyUI-Stereopsis/assets/162214102/1b904b96-d22c-4552-bc3a-2025c6359336">

The DanFrameDelay module offers a sophisticated solution for manipulating image batches by repeating and inserting frames, thereby introducing a delay effect without altering the overall batch size. This functionality is crucial in applications requiring temporal adjustments within image sequences, such as video processing, animation, and dynamic visual effects creation.
Features

    Frame Selection and Delay: Allows the selection of a specific frame within a batch and introduces a delay by repeating the selected frame a specified number of times.
    Batch Size Maintenance: Ingeniously maintains the original batch size after frame insertion, ensuring consistency and compatibility with subsequent processing stages.
    Customizable Parameters: Provides flexibility in selecting the frame to delay and the extent of the delay, with sensible defaults and bounds.

Technical Details

    Input Types: Accepts an image batch as input along with parameters to select the frame (selected_frame) and define the delay (frame_delay).
    Return Types: Outputs an image batch where the selected frame has been repeated according to the specified delay, with the batch size kept constant.
    PyTorch Integration: Built with PyTorch, this module seamlessly integrates into workflows that utilize PyTorch for image manipulation and tensor operations.

Usage

This module falls under the IsItDanOrAi2 category, indicating its relevance in advanced image processing tasks that involve dynamic temporal adjustments. It is particularly useful in scenarios where precise control over the timing of frames within a sequence is needed, such as in video editing, computer vision tasks, or any application requiring temporal manipulation of image data.
Integration

    Node Class Mappings: Identified in systems by the name Dan_FrameDelay, making it readily accessible for integration into node-based architectures or graphical programming environments focused on image processing.
    Node Display Name Mappings: For ease of use and identification by end-users, the module is presented under the title Frame Delay in user interfaces.

Requirements

    PyTorch: As it relies on PyTorch for all tensor operations, having PyTorch installed and configured in the working environment is a prerequisite.
