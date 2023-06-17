import glob

data = []
files = []
for i in glob.glob("*.ui"):
    file = open(i, "r")
    data.append(file.read())
    file.close()

    files.append(i.replace(".", "_").replace("/", "_").replace("\\", "_").upper())


payloads = ["## Dibuat oleh konverter_ui.py ##\nimport io\n"]

for d,f in zip(data, files):
    payloads.append(f"{f} = io.BytesIO({repr(d.encode('utf8'))})")

file = open("ui.py", "w")
file.write("\n".join(payloads))
file.close()