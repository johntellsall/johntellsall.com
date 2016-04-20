# Output to PNG, with Verdana 8pt font
# set terminal png nocrop enhanced font "verdana,8" size 640,300
set terminal pngcairo nocrop enhanced font "verdana,12" size 640,300
set output "optimize.png"

# set terminal dumb size 60,15


set grid ytics lc rgb "#505050"

# Don't show the legend in the chart
set nokey

# Thinner, filled bars
set boxwidth 0.4
set style fill solid 1.00

set title "Optimal Pool Size"
set xlabel "Pool Size (procs)"
set ylabel "Seconds per Proc"

# Rotate X labels and get rid of the small striped at the top (nomirror)
set xtics nomirror rotate by -45

# Show human-readable Y-axis. E.g. "100 k" instead of 100000.
# set format y '%.0s %c'
set format y '%.1f'

# Replace small stripes on the Y-axis with a horizontal gridlines
set tic scale 0
set grid ytics

# Remove border around chart
unset border

# Set a title and Y label. The X label is obviously months, so we don't set it.
# set title "Number of registrations per month" font ",14" tc rgb "#606060"

# Lighter grid lines
set grid ytics lc rgb "#C0C0C0"

# Manual set the Y-axis range
# set yrange [100000 to 300000]

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5   # --- blue

# f(x)= a*x**b + c*x + y0
# fit f(x) 'optimize.dat' via a,b,c,y0
f(x)= a*x + y0
fit f(x) 'optimize.dat' via a,y0

plot "optimize.dat" using 1:($2/$1) with points#  ls 1
# , f(x) with lines
