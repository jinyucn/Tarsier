# Copyright (2024) Bytedance Ltd. and/or its affiliates

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from third_party.tarsier.models.modeling_tarsier import TarsierForConditionalGeneration, LlavaConfig
from third_party.tarsier.dataset.processor import Processor
import torch
import base64
from third_party.tarsier.tools.color import Color

def load_model_and_processor(model_name_or_path, max_n_frames=8):
    print(Color.red(f"Load model and processor from: {model_name_or_path}; with max_n_frames={max_n_frames}"), flush=True)
    processor = Processor(
        model_name_or_path,
        max_n_frames=max_n_frames,
    )
    model_config = LlavaConfig.from_pretrained(
        model_name_or_path,
        trust_remote_code=True,
    )
    model = TarsierForConditionalGeneration.from_pretrained(
        model_name_or_path,
        config=model_config,
        device_map='auto',
        torch_dtype=torch.float16,
        trust_remote_code=True
    )
    model.eval()
    return model, processor

def file_to_base64(img_path):
    with open(img_path, 'rb') as video_file:
        video_b64_str = base64.b64encode(video_file.read()).decode()
    return video_b64_str

