from textgenrnn import textgenrnn
from random import random

textgen = textgenrnn(
    weights_path="./poroshok_generator_weights.hdf5",
    vocab_path="./poroshok_generator_vocab.json",
    config_path="./poroshok_generator_config.json")

k = 20
name = "out.txt"
file = "./generated_texts/" + name

textgen.generate_to_file(file, n=k, temperature=[random() for i in range(k)], progress=True)

f = open(file, "r")
txt = f.read()
f.close()

txt = txt.replace("\n", "\n\n")
txt = txt.replace("\\n", "\n")

f = open(file, "w")
print(txt, file=f)
f.close()
