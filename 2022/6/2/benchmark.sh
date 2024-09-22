#!/bin/bash

echo ----- Benchmarking -----
go test -bench . # -gcflags="-N -l"
