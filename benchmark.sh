

for i in 1 .. 3 ; do
ps -C $1 -o pid=,%mem=,vsz= >> /tmp/mem.log
gnuplot /tmp/gnuplot.script
sleep 1
done &
