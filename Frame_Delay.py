import torch

class DanFrameDelay:
    """
    Correctly named and adjusted node for maintaining the batch size after repeating and inserting frames.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_batch": ("IMAGE",),
                "selected_frame": ("INT", {"default": 0, "min": 0, "max": 63}),
                "frame_delay": ("INT", {"default": 1, "min": 1, "max": 1024}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "DanFrameDelay"
    CATEGORY = "IsItDan-Stereopsis"

    def DanFrameDelay(self, image_batch, selected_frame, frame_delay):
        # Ensure selected_frame is within bounds
        selected_frame = min(image_batch.shape[0] - 1, selected_frame)
        # Extract the specific image from the batch
        selected_image = image_batch[selected_frame:selected_frame + 1].clone()
        # Repeat the selected image based on frame_delay
        repeated_images = selected_image.repeat(frame_delay, 1, 1, 1)
        # Create a new batch by removing the frame at the selected_frame index
        new_batch = torch.cat((image_batch[:selected_frame], image_batch[selected_frame + 1:]), 0)
        # Insert the repeated images back at the selected_frame position
        final_output_batch = torch.cat((new_batch[:selected_frame], repeated_images, new_batch[selected_frame:]), 0)
        # Ensure the final output matches the original batch size
        final_output_batch = final_output_batch[:image_batch.shape[0]]

        return (final_output_batch,)

