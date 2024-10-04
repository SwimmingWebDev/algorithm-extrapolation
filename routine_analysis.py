import time
import routine_1, routine_2, routine_3, routine_4, routine_5
import statistics

# Record times taken
class RoutineAnalysis:
    def __init__(self):
        self.deltas = []
    
    def time_routine(self, fut, casemaker, size, repetitions):

        # clear deltas before running new test
        self.deltas = []

        for i in range(repetitions):
            case = casemaker(size)

            before = time.perf_counter()
            fut(case)
            after = time.perf_counter()

            delta = after - before
            self.deltas.append((delta) * 1000000)

        return statistics.mean(self.deltas)
    
    def clear_deltas(self):
        self.deltas.clear()

# Repetition experiment with different sizes and sample sizes(100, 500, 1000)
def data_generator(fut, casemaker, sizes, repetitions_list):
    
    experiment = RoutineAnalysis()
    results = {}

    # Save the results as a backup
    with open('routine_1_exp_001.txt', 'w') as file:

        for size in sizes:
            means = []

            for repetitions in repetitions_list:
                mean_time = experiment.time_routine(fut, casemaker, size, repetitions)
                means.append(mean_time)

                print(f"Size: {size}, Repetitions: {repetitions}, Mean: {mean_time:.5f}")
                
                results[(size, repetitions)] = mean_time
                file.write(f"{size},{repetitions},{mean_time:.5f}\n")
                
                experiment.clear_deltas()    

    return results

def main():

    # List of different input sizes to test
    # sizes = [10, 20]
    sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]     # small sizes     
    # sizes = [5000, 10000, 20000]             # Mid-sized
    # sizes = [50000, 100000, 200000]        # Large sizes 
    
    # samples at size
    repetitions_list = [100, 500, 1000]

    # Run the experiment
    results = data_generator(routine_1.fut, routine_1.casemaker, sizes, repetitions_list)

    # test
    print("Done")


if __name__ == "__main__":
    main()