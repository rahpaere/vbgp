set terminal postscript enhanced color
set output '| ps2pdf - updates.pdf'
set datafile separator ','

set title 'BGP Failure and Recovery'
set xlabel 'Time (seconds)'
set ylabel 'Connected Routers'
plot 'updates.dat' using ($1/1e6):2 with steps notitle
