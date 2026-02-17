from file_handler import read_file, split_into_chunks
from database import create_database
from multiprocessing import Pool

def process_chunk(chunk):
    return len(chunk)

if __name__ == "__main__":
    create_database()
    lines = read_file("input.txt")
    chunks = split_into_chunks(lines, 100)

    with Pool(2) as p:
        result = p.map(process_chunk, chunks)

    print("Parallel processing result:", result)
