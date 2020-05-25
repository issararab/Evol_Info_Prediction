from pathlib import Path
from allennlp.commands.elmo import ElmoEmbedder
import torch

##Load SeqVec
model_dir = Path('seq_vec')
weights = model_dir / 'weights.hdf5'
options = model_dir / 'options.json'
# embedder = ElmoEmbedder(options,weights, cuda_device=0)
embedder = ElmoEmbedder(options, weights, cuda_device=0)

start_token_embed = torch.FloatTensor(embedder.embed_sentence(['<s>'])).permute(1 ,0 ,2)
end_token_embed = torch.FloatTensor(embedder.embed_sentence(['<\s>'])).permute(1 ,0 ,2)

