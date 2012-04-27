#! /bin/sh

cat >connected.gnuplot <<END
set terminal postscript enhanced color
set output '| ps2pdf - connected.pdf'
set datafile separator ','
set title 'Connected Routers'
set xlabel 'Time (seconds)'
set ylabel '# Routers'
END

prefix='plot '
for i
do
	s=`echo $i | sed s/nexthops/stretch/`
	c=`echo $i | sed s/nexthops/connected/`
	`dirname $0`/stretch.py <$i >$s
	`dirname $0`/connected.py <$s >$c
	printf "${prefix}'$c' with steps notitle" >>connected.gnuplot
	prefix=", \\\\\\n  "
done

gnuplot connected.gnuplot
