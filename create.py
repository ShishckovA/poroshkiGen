from textgenrnn import textgenrnn

name = "poroshok_generator1"
textgen = textgenrnn(name=name)
textgen.train_from_file("./raw_texts/poroshkiTMP.txt", new_model=True, num_epochs=10)
