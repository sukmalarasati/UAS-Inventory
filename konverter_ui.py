import glob

if __name__ == "__main__":
    data = []
    files = []
    for i in glob.glob("*.ui") + glob.glob("*.ico"):
        file = open(i, "rb")
        data.append(file.read())
        file.close()

        if i.endswith(".ui"):
            files.append([i.replace(".", "_").replace("/", "_").replace("\\", "_").upper(), i])
        else:
            files.append((i.replace(".", "_").replace("/", "_").replace("\\", "_").upper(), i))


    payloads = ["## Dibuat oleh konverter_ui.py ##\nimport io, os\n"]

    for d,f in zip(data, files):
        if type(f) is list:
            payloads.append(f"{f[0]} = lambda: io.BytesIO({repr(d)})")
            print(f"{f[1]} -> ui.{f[0]}()")
        else:
            vn, fn = f
            payloads.append(f"""def {vn}():\n  try:\n    file = open("{fn}", "wb")\n    file.write({repr(d)})\n    file.flush()\n    file.close()\n  except:\n    pass\n  return "{fn}"\n""")
            print(f"{f[1]} -> ui.{f[0]}()")

    file = open("ui.py", "w")
    file.write("\n".join(payloads))
    file.close()
