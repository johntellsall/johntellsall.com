## Systems are Complex

Say you're writing a new system, a workflow where data comes in, gets transformed, and flows out.  There are many factors to consider:

- how does data get from one part to another?

- does one part always take the same time to process an item, or is it faster/slower depending on the data?

- how do the parts affect each other?

- what if a downstream component can't accept data. Do you want an upstream part to wait (for how long?), or store data in a queue? (of what size? how does this affect the output)

## Systems have Business Value

Some systems are better (have more business value) if:

- the first output appears quickly -- we want to _minimize latency_

- others operate in batches, processing lots of data, but first output might take a while -- _maximize throughput_

- part is usually fast, but sometimes slow? -- _optimize consistency_ (minimize deviation or standard deviation)

## Simple problem: how many things should we run in parallel?

- if too few, we'll be waiting for the computer to finish

- if too many: processes themselves have overhead, they can be slow to start, slow to write their results downstream, or take up too much memory(?)

- the concurrency is system-dependent:
	Static:
	- based on number of CPUs
	Data-dependent:
	- some data can be easily be processed in parallel, some can't
	Dynamic:
	- memory available
	- data source (disk, SSD, network share)

## Future

This simple example calculates one small number for an artificial
workload. Each parameter is evaluated given canned data, for a
specified value.  In a production system, we get some of these
evaluations already, for free.  To optimize a production system, we
can randomly tweak some parameters, evaluate their effects, then plug
this data back into the optimizer.

Each server can adjust itself. If the server has a hardware upgrade
(CPUs, RAM, disk), optimal parameters will be calculated.  The system
will automatically adjust itself!

Warning: troubleshooting an auto-optimizing system with variable
workload can be difficult.  Some suggestions:

- provide an Off switch

- set values to be safe and correct, over fast

- set parameter min/max values, and log if the parameters are
optimized to these levels

- optimize slowly, so that values gradually converge to the best
value. If parameters flap back and forth it'll be very difficult to
verify the system is behaving correctly.

