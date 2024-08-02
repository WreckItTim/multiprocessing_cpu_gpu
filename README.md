# multiprocessing_cpu_gpu
Example of how to run multiple jobs in parallel across gpu and/or cpu in Python (including pytorch)

Some tips:
* one job is one method you wish to execute
* rather or not running parallel saves time depends on two things: the computational power of each job being run, and how many jobs you are running.
* it is likely quicker to split your jobs into batches
* you may need to play with the number of threads and batch size to find the optimal run time
* in the end it depends on what computations you need to execute, how parallelizable they are, and the hardware running the computations on. So trial and error has been my friend in the past, to see what runs quicker -- sometimes just simply running in series is the way to go.
