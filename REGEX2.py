import re
cumle="selam benim telefon numaram 0535-8886622"
patern=r"\d{3,4}-\d{7}"
print(re.search(patern,cumle))
cumle="en sevidiğim kanal base64"
patern=r"\s\w(5,)"
for eslesme in re.finditer(patern,cumle):
    print(eslesme.group(),eslesme.spam())