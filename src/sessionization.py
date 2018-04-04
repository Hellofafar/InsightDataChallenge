import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Please input the command correctly: sessionization.py input/1 input/2 output")
        exit(1)
    
    input_period_path = sys.argv[1]
    input_log_path = sys.argv[1]
    output_path = sys.argv[3]

    inactivity_period = 0
    with open(input_period_path, 'r') as reader:
        inactivity_period = int(reader.readline().strip())

    if inactivity_period <= 0:
        print("Inactivity period is invalid.")
        exit(2)
    
    with open(input_log_path, 'r') as log_reader:
        headline = log_reader.readline()
        logs = log_reader.readlines()
        for log in logs:
            log = log.strip().split(',')
            if len(log) = 0:
                continue
            ip = log[0].strip()
            date = log[1].strip()
            time = log[2].strip()
            cik = log[4].strip()
            accession = log[5].strip()
            extention = log[6].strip()
            webpage = cik + accession + extention

    print("hello world!")
    
