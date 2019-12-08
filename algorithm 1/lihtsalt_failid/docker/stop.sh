#!/bin/bash

docker stop $(docker ps -a -q --filter ancestor=nomeroff-net --format="{{.ID}}")
