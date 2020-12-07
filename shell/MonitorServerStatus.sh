#!/bin/sh

free -m | grep Mem | awk '{print ($3/$2)*100}'
