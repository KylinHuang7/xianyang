# Without autoload

    $ ab -n 10000 -c 100 http://10.1.21.43:8888/
    This is ApacheBench, Version 2.3 <$Revision: 655654 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 10.1.21.43 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        TornadoServer/4.1
    Server Hostname:        10.1.21.43
    Server Port:            8888

    Document Path:          /
    Document Length:        12 bytes

    Concurrency Level:      100
    Time taken for tests:   23.289 seconds
    Complete requests:      10000
    Failed requests:        0
    Write errors:           0
    Total transferred:      2050000 bytes
    HTML transferred:       120000 bytes
    Requests per second:    429.38 [#/sec] (mean)
    Time per request:       232.893 [ms] (mean)
    Time per request:       2.329 [ms] (mean, across all concurrent requests)
    Transfer rate:          85.96 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   27 319.1      1    7002
    Processing:     2  196 291.5    180    8778
    Waiting:        1  195 291.1    179    8778
    Total:         20  223 431.2    181    8779

    Percentage of the requests served within a certain time (ms)
      50%    181
      66%    194
      75%    202
      80%    207
      90%    217
      95%    243
      98%    470
      99%   1202
     100%   8779 (longest request)


# When using autoload

    $ ab -n 10000 -c 100 http://10.1.21.43:8888/
    This is ApacheBench, Version 2.3 <$Revision: 655654 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 10.1.21.43 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        TornadoServer/4.1
    Server Hostname:        10.1.21.43
    Server Port:            8888

    Document Path:          /
    Document Length:        12 bytes

    Concurrency Level:      100
    Time taken for tests:   23.703 seconds
    Complete requests:      10000
    Failed requests:        0
    Write errors:           0
    Total transferred:      2050000 bytes
    HTML transferred:       120000 bytes
    Requests per second:    421.89 [#/sec] (mean)
    Time per request:       237.030 [ms] (mean)
    Time per request:       2.370 [ms] (mean, across all concurrent requests)
    Transfer rate:          84.46 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   14 167.6      1    3089
    Processing:     2  199 267.0    178    9326
    Waiting:        2  198 266.3    177    9326
    Total:         11  214 314.1    179    9328

    Percentage of the requests served within a certain time (ms)
      50%    179
      66%    193
      75%    203
      80%    208
      90%    226
      95%    250
      98%    468
      99%   1175
     100%   9328 (longest request)
