

from .Side_By_Side import Side_by_side
from .Frame_Delay import DanFrameDelay

NODE_CLASS_MAPPINGS = {
    "Dan_Stereopsis": Side_by_side,
    "Dan_FrameDelay": DanFrameDelay
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Dan_Stereopsis": "Side By Side",
    "Dan_FrameDelay": "Frame Delay"
}
 