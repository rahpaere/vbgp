#! /bin/sh

cat >converged.gnuplot <<END
set terminal postscript enhanced color
set output '| ps2pdf - converged.pdf'
set datafile separator ','
set title 'Convergence Time'
set xlabel 'Time (seconds)'
set ylabel '# Routers'
END

prefix='plot '
for i
do
	s=`echo $i | sed s/nexthops/stretch/`
	c=`echo $i | sed s/nexthops/converged/`
	`dirname $0`/stretch.py <$i >$s
	`dirname $0`/converged.py <$s >$c
	printf "${prefix}'$c' with steps notitle" >>converged.gnuplot
	prefix=", \\\\\\n  "
done

gnuplot converged.gnuplot
