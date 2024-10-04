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

# Repetition experiment with different sizes and sample sizes
def data_generator(fut, casemaker, sizes, repetitions_list, file_name):
    
    experiment = RoutineAnalysis()

    # Save the results as a backup
    with open(file_name, 'w') as file:
        
        results = {}

        for repetitions in repetitions_list:
                for size in sizes:
                    mean_time = experiment.time_routine(fut, casemaker, size, repetitions)
         

                    print(f"Size: {size}, Repetitions: {repetitions}, Mean: {mean_time:.5f}")

                    results[(repetitions, size)] = mean_time
                
                    file.write(f"{repetitions},{size},{mean_time:.5f}\n")
                
                    experiment.clear_deltas()    

        return results

def main():

    routines = {}

    # test
    routine_1_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 7000, 10000, 20000, 30000,  50000, 100000, 200000]
    routine_2_sizes = [1, 2, 3, 5, 7, 9, 10, 13, 15, 17, 20 ]
    routine_3_sizes = [10, 20, 50, 100, 200, 300, 400, 500, 600, 700]
    routine_4_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    routine_5_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

    # routine_1_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 7000, 10000, 20000, 30000,  50000, 100000, 200000]
    # routine_2_sizes = [3, 5, 7, 9, 10, 13, 15, 17, 20, 23, 25, 27,29, 30, 32, 33, 35, 37, 38, 40]
    # routine_3_sizes = [10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000]
    # routine_4_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
    # routine_5_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

    repetitions_list = [20, 50, 70, 100]
    # repetitions_list = [50, 100, 500, 1000]

    # List of different input sizes to test
    # sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 7000, 10000, 20000, 30000,  50000, 100000, 200000, 400000, 600000, 800000, 100000]
    # repetitions_list = [100, 500, 1000, 3000, 5000, 10000]
    
    # Run the experiments
    data_generator(routine_1.fut, routine_1.casemaker, routine_1_sizes, repetitions_list, "routine_1.txt")
    data_generator(routine_2.fut, routine_2.casemaker, routine_2_sizes, repetitions_list, "routine_2.txt")
    data_generator(routine_3.fut, routine_3.casemaker, routine_3_sizes, repetitions_list, "routine_3.txt")
    data_generator(routine_4.fut, routine_4.casemaker, routine_4_sizes, repetitions_list, "routine_4.txt")
    data_generator(routine_5.fut, routine_5.casemaker, routine_5_sizes, repetitions_list, "routine_5.txt")

    print("Done")


if __name__ == "__main__":
    main()