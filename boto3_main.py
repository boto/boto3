import time


def benchmark_with_realistic_expectations():
    # Original version
    start = time.time()
    index = 99
    for i in range(100):
        for j in range(100):
            if j == index:
                print(j)  # This I/O dominates the runtime
                index = index - 1
    original_time = time.time() - start

    print("\n" + "=" * 50 + "\n")

    # Optimized version  
    start = time.time()
    for i in range(99, -1, -1):
        print(i)  # Same I/O cost
    optimized_time = time.time() - start

    print(f"Original time: {original_time:.4f} seconds")
    print(f"Optimized time: {optimized_time:.4f} seconds")
    print(f"Actual speedup: {original_time / optimized_time:.1f}x")


benchmark_with_realistic_expectations()
