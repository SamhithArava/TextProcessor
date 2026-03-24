from file_handler import read_file, split_into_chunks
from rule_engine import analyze_chunk
from database import create_database, bulk_insert, test_query
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
    chunk_size = int(input("Enter chunk size: "))
    chunks = split_into_chunks(lines, chunk_size)

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

    data_to_insert = []

    for chunk, result in zip(chunks, single_results):
        score, tag = result
        chunk_text = " ".join(chunk)
        data_to_insert.append((chunk_text, score, tag))

    start = time.time()
    bulk_insert(data_to_insert)
    end = time.time()
    print("Bulk Insert Time:", round(end - start, 4), "seconds")

    query_time = test_query()
    print("Query Time:", round(query_time, 4), "seconds")

    print("\nMilestone 2 Execution Completed.\n")