import numpy as np
# trainer class handles processing each thread in multiprocessing
# also holds data, so that we do not set over multiple threads
class Trainer:
    def __init__(self, X, Y):
        # set data (read only)
        # optionally create a data loader if using pytorch
            # you may want to create a seperate data loader for each thread
        self.X = X
        self.Y = Y

    # use this to run a job in paralel by passing in params dict (otherwise takes a list by default)
    def single_job(self, job_name, params):
        job_func = getattr(self, job_name)
        return job_func(**params)
    
    # use this to run a batch of jobs
    def batch_job(self, batch):
        results = []
        for job in batch:
            job_name, params = job
            results.append(self.single_job(job_name, params))
        return results
    
    # dummy func just does some matrix operations for us to use as benchmarks
    def dummy_func(self, alpha, beta, multi_gpu=False):
        # if running GPU in parallel, get unique cuda device for multiprocessing
        if multi_gpu:
            params = locals()
            multiprocess_ID = int(mp.current_process().name.split('-')[1]) % n_gpus
            device = 'cuda:' + str(multiprocess_ID) # use this device for cuda pytorch
        
        # dummy operation to just take linear combination of X and Y
        result = np.sum(alpha*self.X*beta*self.Y)
        
        # you can return the result from this paralell thread
        # however, I find it is better to write this result to file with a unique name,
            # and then after running all threads create a collector that agregates all written results
            # this allows you to start and restart the process if something goes wrong
        return result
        
        
# simple stopwatch to time whatevs, in (float) seconds
# keeps track of laps along with final time
import time
class Stopwatch:
    def __init__(self):
        self.start_time = time.time()
        self.last_time = self.start_time
        self.laps = []
    def lap(self):
        this_time = time.time()
        delta_time = this_time - self.last_time
        self.laps.append(delta_time)
        self.last_time = this_time
        return delta_time
    def stop(self):
        self.stop_time = time.time()
        self.delta_time = self.stop_time - self.start_time
        return self.delta_time