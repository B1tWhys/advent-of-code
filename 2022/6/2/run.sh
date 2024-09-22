#!/bin/bash

go build ./solution.go
for _ in {1..5}; do
	./solution
done
