import time
import routine_1

# Record times taken
class RoutineAnalysis:
    def __init__(self):
        self.deltas = []
    
    def time_routine(self, fut, casemaker, size, repetitions):

        # empty deltas
        self.deltas = []

        for i in range(repetitions):
            case = casemaker(size)

            before = time.perf_counter()
            fut(case)
            after = time.perf_counter()

            delta = after - before
            self.deltas.append(delta)

        return self.deltas
    
    def clear_deltas(self):
        self.deltas.clear()

# Repetition experiment with different sizes
def data_generator(fut, casemaker, sizes, repetitions):
    
    experiment = RoutineAnalysis()
    results = {}

      # Save the results as a backup
    with open('routine_1_exp_001.txt', 'w') as f:

        for size in sizes:
            deltas = experiment.time_routine(fut, casemaker, size, repetitions)
            results[size] = deltas

            deltas_str = ', '.join(f"{delta:.6f}" for delta in deltas)
            f.write(f"Size: {size}\nExecution Times (s): {deltas_str}\n\n")

            print(f"Size: {size}, Collected {len(deltas)} deltas")

            experiment.clear_deltas()

    return results

def main():

    # List of different input sizes to test
    sizes = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 100000, 200000]            # Small sizes for quick feedback
    # sizes = [5000, 10000, 20000]             # Mid-sized for deeper evaluation
    # large_sizes = [50000, 100000, 200000]        # Large sizes for long-running tests (overnight)
     
    # Run the experiment
    results = data_generator(routine_1.fut, routine_1.casemaker, sizes, repetitions=1000)

    # test
    print("Done")


if __name__ == "__main__":
    main()