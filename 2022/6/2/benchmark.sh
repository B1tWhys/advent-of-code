#!/bin/bash

go test -bench . -gcflags="-N -l"
