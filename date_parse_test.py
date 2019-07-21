from dateutil import parser

source_timestamps = [
    "2019-07-15 02:58:01.886000+00:00",
    "2019-07-15 02:58:09.138000+00:00",
    "2019-07-15 02:58:14.064000+00:00",
    "2019-07-15 02:58:18.908000+00:00",
    "2019-07-15 02:58:19.685000+00:00",
    "2019-07-15 02:58:22.424000+00:00",
    "2019-07-15 02:58:28.313000+00:00",
    "2019-07-15 02:58:32.399000+00:00",
    "2019-07-15 02:58:38.173000+00:00",
    "2019-07-15 02:58:40.921000+00:00",
    "2019-07-15 02:58:42.309000+00:00",
    "2019-07-15 02:58:45.064000+00:00",
    "2019-07-15 02:58:53.020000+00:00",
    "2019-07-15 02:58:53.549000+00:00",
    "2019-07-15 02:58:55.692000+00:00",
    "2019-07-15 02:58:58.507000+00:00",
    "2019-07-15 02:59:00.758000+00:00",
    "2019-07-15 02:59:03.126000+00:00",
    "2019-07-15 02:59:05.876000+00:00",
    "2019-07-15 02:59:10.981000+00:00",
    "2019-07-15 02:59:13.494000+00:00",
    "2019-07-15 02:59:15.846000+00:00",
    "2019-07-15 02:59:21.809000+00:00",
    "2019-07-15 02:59:21.831000+00:00",
    "2019-07-15 02:59:24.178000+00:00",
    "2019-07-15 02:59:26.845000+00:00",
    "2019-07-15 02:59:27.797000+00:00",
    "2019-07-15 02:59:29.018000+00:00",
    "2019-07-15 02:59:31.203000+00:00",
    "2019-07-15 02:59:33.683000+00:00",
    "2019-07-15 02:59:35.995000+00:00",
    "2019-07-15 02:59:35.995000+00:00",
    "2019-07-15 02:59:35.995000+00:00",
    "2019-07-15 02:59:35.995000+00:00",
    "2019-07-15 02:59:35.995000+00:00",
    "2019-07-15 02:59:38.155000+00:00",
    "2019-07-15 02:59:42.461000+00:00",
    "2019-07-15 02:59:43.005000+00:00",
    "2019-07-15 02:59:44.851000+00:00",
    "2019-07-15 02:59:46.656000+00:00",
    "2019-07-15 02:59:48.237000+00:00",
    "2019-07-15 02:59:49.863000+00:00",
    "2019-07-15 02:59:51.502000+00:00",
    "2019-07-15 02:59:54.305000+00:00",
    "2019-07-15 03:00:00.732000+00:00",
    "2019-07-15 03:00:02.732000+00:00",
    "2019-07-15 03:00:03.809000+00:00",
    "2019-07-15 03:00:04.715000+00:00",
    "2019-07-15 03:00:05.360000+00:00",
    "2019-07-15 03:00:06.510000+00:00",
    "2019-07-15 03:00:09.012000+00:00",
    "2019-07-15 03:00:12.217000+00:00",
    "2019-07-15 03:00:16.198000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:16.790000+00:00",
    "2019-07-15 03:00:18.067000+00:00",
    "2019-07-15 03:00:18.711000+00:00",
    "2019-07-15 03:00:18.711000+00:00",
    "2019-07-15 03:00:19.728000+00:00",
    "2019-07-15 03:00:20.055000+00:00",
    "2019-07-15 03:00:20.591000+00:00",
    "2019-07-15 03:00:20.591000+00:00",
    "2019-07-15 03:00:22.297000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:23.803000+00:00",
    "2019-07-15 03:00:24.511000+00:00",
    "2019-07-15 03:00:26.462000+00:00",
    "2019-07-15 03:00:29.553000+00:00",
    "2019-07-15 03:00:35.847000+00:00",
    "2019-07-15 03:00:40.751000+00:00",
    "2019-07-15 03:00:44.364000+00:00",
    "2019-07-15 03:00:45.452000+00:00",
    "2019-07-15 03:01:00.291000+00:00",
    "2019-07-15 03:01:10.777000+00:00",
    "2019-07-15 03:01:19.714000+00:00",
    "2019-07-15 03:01:19.739000+00:00",
    "2019-07-15 03:01:20.919000+00:00",
    "2019-07-15 03:01:25.177000+00:00",
    "2019-07-15 03:01:35.070000+00:00",
    "2019-07-15 03:01:36.198000+00:00",
    "2019-07-15 03:01:40.017000+00:00",
    "2019-07-15 03:01:41.199000+00:00",
    "2019-07-15 03:01:48.027000+00:00",
    "2019-07-15 03:01:55.989000+00:00",
    "2019-07-15 03:02:00.903000+00:00",
    "2019-07-15 03:02:13.662000+00:00",
    "2019-07-15 03:02:18.048000+00:00",
    "2019-07-15 03:02:24.604000+00:00",
    "2019-07-15 03:02:29.750000+00:00",
    "2019-07-15 03:02:39.620000+00:00",
    "2019-07-15 03:02:46.193000+00:00",
    "2019-07-15 03:02:46.193000+00:00",
    "2019-07-15 03:02:46.193000+00:00",
    "2019-07-15 03:02:46.193000+00:00",
    "2019-07-15 03:02:46.196000+00:00",
    "2019-07-15 03:02:46.199000+00:00",
    "2019-07-15 03:02:51.196000+00:00",
    "2019-07-15 03:02:59.005000+00:00"]

timestamps = []
b1 = []
b2 = []
b3 = []

# parse source strings to datetime objects
for i in source_timestamps:
    dt = parser.parse(i)
    timestamps.append(dt)


index = timestamps[0].minute
for i in timestamps:
    if i.minute == index:
        b1.append(i)

    if i.minute == index + 1:
        index = i.minute
        b2.append(i)


print("bin 1")
print(b1)
print("bin 2")
print(b2)
print("bin 3")
print(b3)
