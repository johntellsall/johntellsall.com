LOGS.md


command: ab -t 30 -c 10 web/

bench_1  | Server Software:        nginx/1.11.10
bench_1  | Server Hostname:        web
bench_1  | Server Port:            80
bench_1  | 
bench_1  | Document Path:          /
bench_1  | Document Length:        612 bytes
bench_1  | 
bench_1  | Concurrency Level:      10
bench_1  | Time taken for tests:   6.743 seconds
bench_1  | Complete requests:      50000
bench_1  | Failed requests:        0
bench_1  | Total transferred:      42300000 bytes
bench_1  | HTML transferred:       30600000 bytes
bench_1  | Requests per second:    7414.85 [#/sec] (mean)
bench_1  | Time per request:       1.349 [ms] (mean)
bench_1  | Time per request:       0.135 [ms] (mean, across all concurrent requests)
bench_1  | Transfer rate:          6125.94 [Kbytes/sec] received
bench_1  | 
bench_1  | Connection Times (ms)
bench_1  |               min  mean[+/-sd] median   max
bench_1  | Connect:        0    0   0.3      0       7
bench_1  | Processing:     0    1   0.5      1      12
bench_1  | Waiting:        0    1   0.5      1       9
bench_1  | Total:          1    1   0.6      1      12
bench_1  | 
bench_1  | Percentage of the requests served within a certain time (ms)
bench_1  |   50%      1
bench_1  |   66%      1
bench_1  |   75%      1
bench_1  |   80%      1
bench_1  |   90%      2
bench_1  |   95%      2
bench_1  |   98%      3
bench_1  |   99%      4
bench_1  |  100%     12 (longest request)


# host bench, guest web


Server Software:        nginx/1.11.10
Server Hostname:        localhost
Server Port:            8888

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   10.500 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42300000 bytes
HTML transferred:       30600000 bytes
Requests per second:    4762.05 [#/sec] (mean)
Time per request:       2.100 [ms] (mean)
Time per request:       0.210 [ms] (mean, across all concurrent requests)
Transfer rate:          3934.28 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       4
Processing:     0    2   1.4      2      22
Waiting:        0    2   1.3      1      22
Total:          0    2   1.4      2      22

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      3
  90%      4
  95%      5
  98%      6
  99%      8
 100%     22 (longest request)


# host-bench to host-web


Server Software:        nginx/1.10.1
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   3.378 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42700000 bytes
HTML transferred:       30600000 bytes
Requests per second:    14800.16 [#/sec] (mean)
Time per request:       0.676 [ms] (mean)
Time per request:       0.068 [ms] (mean, across all concurrent requests)
Transfer rate:          12343.10 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       2
Processing:     0    0   0.2      0       6
Waiting:        0    0   0.2      0       6
Total:          0    1   0.2      1       7

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      1
 100%      7 (longest request)


 # host-bench to guest-web; guest mapped w/ host networking


ab -t 30 -c 10 localhost/ 

Server Software:        nginx/1.11.10
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   4.971 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42300000 bytes
HTML transferred:       30600000 bytes
Requests per second:    10058.56 [#/sec] (mean)
Time per request:       0.994 [ms] (mean)
Time per request:       0.099 [ms] (mean, across all concurrent requests)
Transfer rate:          8310.10 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       3
Processing:     0    1   0.3      1       8
Waiting:        0    1   0.3      1       8
Total:          0    1   0.3      1       8

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      2
 100%      8 (longest request)



# B2: guest-guest; host networking

Server Software:        nginx/1.11.10
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   5.046 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42300000 bytes
HTML transferred:       30600000 bytes
Requests per second:    9908.63 [#/sec] (mean)
Time per request:       1.009 [ms] (mean)
Time per request:       0.101 [ms] (mean, across all concurrent requests)
Transfer rate:          8186.23 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       6
Processing:     0    1   0.3      1      10
Waiting:        0    1   0.3      1      10
Total:          1    1   0.3      1      10

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      2
  99%      2
 100%     10 (longest request)


# B3:

Server Software:        nginx/1.10.1
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      10
Time taken for tests:   3.748 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      42700000 bytes
HTML transferred:       30600000 bytes
Requests per second:    13341.31 [#/sec] (mean)
Time per request:       0.750 [ms] (mean)
Time per request:       0.075 [ms] (mean, across all concurrent requests)
Transfer rate:          11126.45 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       5
Processing:     0    0   0.2      0       5
Waiting:        0    0   0.2      0       5
Total:          0    1   0.2      1       5

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      1
  98%      1
  99%      1
 100%      5 (longest request)
