import vk_api
def cut(text):
    if "©" in text:
        return text[:text.find("\n©")]
    if "(с)" in text:
        return text[:text.find("\n(с)")]
    return text
vk_session = vk_api.VkApi(token='0a8816082ae71bd4b5c6b6caedec89f490b45ba8042629efdaa308198427c32df4c7d3b2cdf51fafcf53f')
vk = vk_session.get_api()

count = vk.wall.get(owner_id=-31481258)['count']
texts = []
for i in range(0, count, 100):
    ctext = vk.wall.get(owner_id=-31481258, count=100, offset=i)
    for textd in ctext["items"]:
        texts.append(cut(textd["text"]))
    print(i / count * 100)
out = open("./raw_texts/poroshkiTMP.txt", "w", encoding="utf-8")
print(texts)
for elem in texts:
    if (50 <= len(elem) <= 120):
        print(elem.replace("\n", "\\n"), file=out)
out.close()