#! /bin/sh

if test $# -ne 1
then
	echo Usage: $0 SIZE
	exit 1
fi

files=
for i in `seq $1`
do
	o=/tmp/vnet$i-rtmon.txt
	files="$files $o"
	ip monitor file /tmp/vnet$i-rtmon.log >$o
done
`dirname $0`/updates.py $files
