import multiprocessing

def task(t):
    result = t * 2
    return result

if __name__ == "__main__":
    # Create a multiprocessing pool with the desired number of processes (e.g., 4).
    pool = multiprocessing.Pool(processes=4)

    # List of tasks to be processed in parallel.
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Distribute tasks among worker processes and collect the results.
    results = pool.map(task, tasks)

    # Close the pool to prevent any more tasks from being submitted.
    pool.close()

    # Wait for all worker processes to complete their tasks.
    pool.join()

    # The results list now contains the processed results of each task.
    print(results)
