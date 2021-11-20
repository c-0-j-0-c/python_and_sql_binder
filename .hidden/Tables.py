import sys
if __name__ == "__main__":
    with open("tables.txt", encoding = 'utf-8') as t:
        tables = t.read()
        tablesList = tables.split()
        len_t = max([len(i) for i in tablesList])
    with open(sys.argv[1], encoding = 'utf-8') as f:
        text = f.read()
        db, attribStr = text.split(": ")
        attrib = attribStr.split()
        attrib_list = []
        attribs = (db + ": ").ljust(len_t + 2)
        for i, a  in enumerate(attrib):
            if len(attribs) < 55:
                attribs += a + ", "
            else:
                attrib_list.append(attribs+'\n')
                attribs = " " * (len_t + 2) + a
        attrib_list.append(attribs[:-2] if attribs.endswith(", ") else attribs)
        print("".join(attrib_list))
