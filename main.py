from file_handler import read_file, split_into_chunks
from rule_engine import analyze_chunk
from database import create_database
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import time


def single_processing(chunks):
    results = []
    for chunk in chunks:
        results.append(analyze_chunk(chunk))
    return results


if __name__ == "__main__":

    create_database()

    lines = read_file("input.txt")
    chunks = split_into_chunks(lines, 100)

    print("\n----- PERFORMANCE COMPARISON -----\n")

    start = time.time()
    single_results = single_processing(chunks)
    end = time.time()
    print("Single Processing Time:", round(end - start, 4), "seconds")

    start = time.time()
    with ThreadPoolExecutor() as executor:
        thread_results = list(executor.map(analyze_chunk, chunks))
    end = time.time()
    print("ThreadPool Time:", round(end - start, 4), "seconds")

    start = time.time()
    with Pool() as pool:
        process_results = pool.map(analyze_chunk, chunks)
    end = time.time()
    print("Multiprocessing Time:", round(end - start, 4), "seconds")

    print("\nPerformance comparison completed.\n")