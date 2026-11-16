#!/bin/bash
# Виправлена побудова графіка MTBF (див. DEF-IPERF-01): розбір виводу iperf 2.1+ через awk,
# переведення Gbits/sec у Mbit/sec, вивід у PNG (працює і з gnuplot-nox).
awk '/bits\/sec/ {split($3,t,"-"); if (t[2]-t[1] < 1.5) {v=$7; if ($8 ~ /^G/) v=v*1000; print t[2], v}}' tcp_10.0.0.10.txt > mtbf.dat
gnuplot -e "set terminal png size 1000,500; set output 'mtbf_tcp.png'; set xlabel 'Time, sec'; set ylabel 'Mbit/sec'; set grid; set yrange [0:*]; plot 'mtbf.dat' using 1:2 with linespoints title 'TCP 10.0.0.10 -> 10.0.0.1'"
