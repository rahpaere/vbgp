set terminal postscript enhanced color
set output '| ps2pdf - updates.pdf'
set datafile separator ","
plot "updates.dat" using 1:2 with steps notitle
