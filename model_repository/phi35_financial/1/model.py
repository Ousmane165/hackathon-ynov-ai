# Exemple minimal de backend Python Triton.
# Le déploiement de production utilise Ollama.

import json
import numpy as np
import triton_python_backend_utils as pb_utils

class TritonPythonModel:
    def initialize(self, args):
        self.model_name = "phi35_financial"

    def execute(self, requests):
        responses = []
        for request in requests:
            prompt_tensor = pb_utils.get_input_tensor_by_name(request, "PROMPT")
            prompt = prompt_tensor.as_numpy()[0].decode("utf-8")
            answer = f"Réponse simulée Triton pour Phi-3.5-Financial : {prompt[:120]}"
            output = pb_utils.Tensor("RESPONSE", np.array([answer.encode("utf-8")], dtype=np.object_))
            responses.append(pb_utils.InferenceResponse(output_tensors=[output]))
        return responses
