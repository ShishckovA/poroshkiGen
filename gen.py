from textgenrnn import textgenrnn
from random import random

name = "poroshok_generator1"

textgen = textgenrnn(
    weights_path="./models/%s_weights.hdf5" % name,
    vocab_path="./models/%s_vocab.json" % name,
    config_path="./models/%s_config.json" % name)

k = 200
outname = "out.txt"
filename = "./generated_texts/" + outname

textgen.generate_to_file(filename, n=k, temperature=[random() for i in range(k)], progress=True)

f = open(filename, "r")
txt = f.read()
f.close()

txt = txt.replace("\n", "\n\n")
txt = txt.replace("\\n", "\n")

f = open(filename, "w", encoding="utf-8")
print(txt, file=f)
f.close()
