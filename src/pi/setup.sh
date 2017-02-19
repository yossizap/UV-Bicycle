#!/usr/bin/env bash

sudo cp uv_runner.sh /etc/init.d/uv_runner
sudo chmod +x /etc/init.d/uv_runner
sudo update-rc.d uv_runner defaults
