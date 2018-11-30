# Docker Examples

These are three examples which demonstrate some of the features of Docker and containers in general!

## Why Docker?
Its awesome.  But additionally it solves several problems in reasonable (subjective I know) ways.  Docker helps manage *containers* a technology which leverages the OS kernels ability isolate system resources and processes.  This means instead of a single machine (or virtual machine, its a cloud world after all), to run each application to ensure the applications do not interfere, we can use containers to run several processes on the same host.  Its important to remember that containers however, are not VM's, they are more of a collection of isolated process than a true isolated system.  This means containers are more "lightweight" than VM's and have almost bare metal performance, but can have increased security concerns.

Docker does a few things with containers, but at the heart its an abstraction for making it easy to create, distribute, and abstract containers (yes, layers of abstractions).  It differs from other containerization techniques in that it is meant to build an environment for running a single process, if you want multiple processes, use multiple Docker containers.  There are ways to get around this sort of philosophy especially when it does odd things (see [dump-init](https://github.com/Yelp/dumb-init)), but for most part it works just fine.  Now you might ask, "How do I coordinate a bunch of different processes if they are all in different Docker containers and need to communicate and what not?"  This is why we have things like Kubernetes and more generally container-orchestration.
## hello-world
{{ hello-world }}
## hello-code
{{ hello-code }}
## hello-flask
{{ hello-flask }}
