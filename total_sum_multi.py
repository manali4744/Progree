import multiprocessing

def calculate_sum(start, end, result_queue):
    total = 0
    for num in range(start, end + 1):
        total += num
    print(result_queue)
    result_queue.put(total)

if __name__ == '__main__':
    num_processes = 4 
    numbers_per_process = 50
    result_queue = multiprocessing.Queue()
    print(result_queue)

    processes = []
    for i in range(num_processes):
        start = i * numbers_per_process + 1
        end = (i + 1) * numbers_per_process
        p = multiprocessing.Process(target=calculate_sum, args=(start, end, result_queue))
        print(p)
        processes.append(p)
        p.start()

    total_sum = 0
    completed_processes = 0
    while completed_processes < num_processes:
        if not result_queue.empty():
            partial_sum = result_queue.get()
            total_sum += partial_sum
            completed_processes += 1

        progress = (completed_processes / num_processes) * 100
        print(f"Progress: {progress:.1f}%")

        if completed_processes == num_processes and result_queue.empty():
            break

    for p in processes:
        p.join()

    print("Sum of numbers from 1 to 200:", total_sum)
