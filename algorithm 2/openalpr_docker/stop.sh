#!/bin/bash

docker stop $(docker ps -a -q --filter ancestor=openalpr --format="{{.ID}}")
