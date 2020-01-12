from textgenrnn import textgenrnn

textgen = textgenrnn(name="poroshok_generator")
textgen.train_from_file("./raw_texts/poroshki.txt", new_model=True, num_epochs=20)