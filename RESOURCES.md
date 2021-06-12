# Threading

## [Python Concourency](https://realpython.com/python-concurrency)

- https://github.com/realpython/materials/tree/master/concurrency-overview

Concurrency Type	                 |   Switching Decision	                                                  | Number of Processors
| :---------------------------------:|:-----------------------------------------------------------------------|:----------------------------|
Pre-emptive multitasking (threading) |	The operating system decides when to switch tasks external to Python. |	1
Cooperative multitasking (asyncio)	 | The tasks decide when to give up control.	                          | 1
Multiprocessing (multiprocessing)	 | The processes all run at the same time on different processors.	      | Many

Adding concurrency to your program adds extra code and complications, so you’ll need to decide if the potential speed up is worth the extra effort.

| I/O-Bound Process	         | CPU-Bound Process
|:---------------------------|:-------------------------------------------------------|
Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.	| You program spends most of its time doing CPU operations.
Speeding it up involves overlapping the times spent waiting for these devices.	 | Speeding it up involves finding ways to do more computations in the same amount of time.

