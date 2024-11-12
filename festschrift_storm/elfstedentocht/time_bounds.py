import sys

if len(sys.argv) == 1:
    # print the properties we need
    MIN_TIME_BOUND = 0.25
    MAX_TIME_BOUND = 60
    TIME_BOUND_RESOLUTION = 0.25

    timebound = MIN_TIME_BOUND
    while timebound <= MAX_TIME_BOUND:
        print('"pr_event_in_{}_years": P=? [F<={} "elfstedentocht"];'.format(str(timebound).replace(".","_"),timebound))
        timebound += TIME_BOUND_RESOLUTION
else:
    # parse log file and output in csv format
    print("timebound,result")
    with open(sys.argv[1], 'r') as logfile:
        log = logfile.read()
    pos1 = 0
    while True:
        pos1 = log.find("pr_event_in_", pos1)
        if pos1 == -1:
            break
        pos1 += len("pr_event_in_")
        pos2 = log.find("_years", pos1)
        timebound = log[pos1:pos2].replace("_",".")
        pos1 = log.find("Result (for initial states): ", pos2) + len("Result (for initial states): ")
        pos2 = log.find("\n", pos1)
        result = log[pos1:pos2]
        print("{},{}".format(timebound,result))

