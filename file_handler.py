def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    print("File loaded successfully.")
    print("Total lines:", len(lines))
    return lines


def split_into_chunks(lines, chunk_size=100):
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
    print("Total chunks created:", len(chunks))
    return chunks
