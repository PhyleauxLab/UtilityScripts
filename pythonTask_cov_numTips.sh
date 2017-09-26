#!/bin/bash
python TreeScaperWrapper.py -c "../CLVTreeScaper" -i $1 -n "Covariance" -f "Both" -mc 10 -m "CPM" -w 0 -r 1 -lf 0.05 -hf 0.95 -s "gnu,1:1,NA"
