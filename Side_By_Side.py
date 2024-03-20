import torch

class Side_by_side:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "left_image": ("IMAGE",),
                "right_image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "Side_by_side"
    CATEGORY = "IsItDan-Stereopsis"

    def Side_by_side(self, left_image, right_image):
        # Assuming the input images are PyTorch tensors
       
        # Combine the input images side by side
        image_concatenated = torch.cat((left_image, right_image), dim=2)
        return (image_concatenated,)

