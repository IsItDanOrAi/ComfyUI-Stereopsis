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
    CATEGORY = "IsItDanOrAi"

    def Side_by_side(self, left_image, right_image):
        # Assuming the input images are PyTorch tensors
       
        # Combine the input images side by side
        image_concatenated = torch.cat((left_image, right_image), dim=2)
        return (image_concatenated,)

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "Dan_Stereopsis": Side_by_side
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Dan_Stereopsis": "Side By Side"
}
