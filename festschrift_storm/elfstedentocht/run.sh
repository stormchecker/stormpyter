#!/bin/zsh

STORM_CMD="$HOME/storm/build/bin/storm"
echo "Checking Properties..."
$STORM_CMD --engine dd-to-sparse --bisimulation --sylvan:threads 1 -pc --prism elfstedentocht.prism --prop elfstedentocht.props --precision 1e-9 > storm.log
cat storm.log


echo ""
echo "Checking Time Bounds... (This may take a minute)"
python3 time_bounds.py > time_bounds.props
$STORM_CMD --engine dd-to-sparse --bisimulation --sylvan:threads 1 -pc --prism elfstedentocht.prism --prop time_bounds.props > time_bounds.log
python3 time_bounds.py time_bounds.log > time_bounds.csv
cat time_bounds.csv