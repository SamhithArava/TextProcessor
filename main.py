from file_handler import read_file, split_into_chunks
from database import create_database, insert_result
from rule_engine import analyze_chunk
from concurrent.futures import ThreadPoolExecutor
import time


if __name__ == "__main__":

    start_time = time.time()

    create_database()

    lines = read_file("input.txt")
    chunks = split_into_chunks(lines, 100)

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(analyze_chunk, chunks))

    for chunk, result in zip(chunks, results):
        score, tag = result
        chunk_text = " ".join(chunk)
        insert_result(chunk_text, score, tag)

    end_time = time.time()

    print("Processing completed.")
    print("Execution Time:", end_time - start_time)