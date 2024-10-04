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

        mean_time =  statistics.mean(self.deltas)
        median_time =  statistics.median(self.deltas)
        std_time = statistics.stdev(self.deltas) if len(self.deltas) > 1 else 0
        return  mean_time, median_time, std_time
    
    def clear_deltas(self):
        self.deltas.clear()

# Repetition experiment with different sizes and sample sizes
def data_generator(fut, casemaker, sizes, repetitions_list, file_name):
    
    experiment = RoutineAnalysis()

    # Save the results as a backup
    with open(file_name, 'w') as file:
        
        # headers
        file. write("Repetitions,Size,Mean,Median,Std\n")
        results = {}

        for repetitions in repetitions_list:
                for size in sizes:
                    mean_time, median_time, std_time = experiment.time_routine(fut, casemaker, size, repetitions)
         
                    print(f"Size: {size}, Repetitions: {repetitions}, Mean: {mean_time:.5f}, Median: {median_time:.5f}, SD: {std_time:.5f}")

                    results[(repetitions, size)] = (mean_time, median_time, std_time)
                
                    file.write(f"{repetitions},{size},{mean_time:.5f},{median_time:.5f},{std_time:.5f}\n")
                
                    experiment.clear_deltas()    

        return results

def main():

    # input sizes
    small_sizes = [10, 11, 12, 13, 14, 15, 16, 17, 20, 30, 50]
    sm_mid_sizes = [10, 30, 50, 70, 90, 100, 110, 130, 150, 170, 200, 230, 250, 270, 290, 300]
    mid_sizes = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000]
    sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 4000, 7000, 10000, 30000,  50000, 100000, 200000]
    large_sizes = [500000, 1000000, 2000000, 4000000, 10000000]

    # number of samples
    small_samples = [20, 50, 70, 90, 100]
    mid_samples = [50, 100, 500, 1000, 2000, 5000]
    samples = [5000, 10000, 30000, 50000, 100000]

    # Run the experiments
    data_generator(routine_1.fut, routine_1.casemaker, large_sizes, samples, "routine_1.txt")
    data_generator(routine_2.fut, routine_2.casemaker, small_sizes, [300, 500, 1000], "routine_2.txt")
    data_generator(routine_3.fut, routine_3.casemaker, [3000, 5000, 10000], mid_samples, "routine_3.txt")
    data_generator(routine_4.fut, routine_4.casemaker, sm_mid_sizes, [500, 1000, 2000, 5000], "routine_4.txt")
    data_generator(routine_5.fut, routine_5.casemaker, sizes, mid_samples, "routine_5.txt")
   

    print("Done")


if __name__ == "__main__":
    main()