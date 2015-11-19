#!/bin/bash
sudo initctl reload-configuration
sudo service otm-unicorn restart
sudo service tiler restart
sudo service ecoservice restart
sudo service nginx restart
