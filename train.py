from textgenrnn import textgenrnn

name = "poroshok_generator1"

textgen = textgenrnn(
    weights_path="./models/%s_weights.hdf5" % name,
    vocab_path="./models/%s_vocab.json" % name,
    config_path="./models/%s_config.json" % name)

textgen.train_from_file("./raw_texts/poroshkiTMP.txt", new_model=False, num_epochs=20)
