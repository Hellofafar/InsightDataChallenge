import sys
import datetime

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
    
    user_list = []  # List of active users/ips basedthat have requested for document.
    user_updated_list = []  # List of active users/ips ordered by last request time.
    request_dict = {}  # Dictionary of users/ips and their relevant information.

    try:
        open(output_path, 'a') as session_writer
    except:
        print('Output path is invalid')
        exit(3)

    with open(input_log_path, 'r') as log_reader:
        headline = log_reader.readline()
        logs = log_reader.readlines()

        currentTime = '1970-01-01 00:00:00'
        timestamp = datetime.datetime.strptime(currenttTime, '%Y-%m-%d %H:%M:%S')
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

            requestTime = date + ' ' + time
            if requestTime != currentTime:  # If a new time shows up, check if any session is expired
                timestamp = datetime.datetime.strptime(requestTime, '%Y-%m-%d %H:%M:%S')
                currentTime = requestTime

                while user_updated_list:
                    user = user_updated_list[0]
                    # Check from the start of user_updated_list until the first user of list is still active
                    if (timestamp - request_dict[user]['lastTime']).seconds > inactivity_period:
                        # If a session is expired, delete all relevant record of this session.
                        values = request_dict.pop(user)
                        user_updated_list.remove(user)
                        user_list.remove(user)

                        start = datetime.datetime.strftime(values['startTime'], '%Y-%m-%d %H:%M:%S')
                        end = datetime.datetime.strftime(values['lastTime'], '%Y-%m-%d %H:%M:%S')
                        session_writer.write('%s,%s,%s,%d,%d\n' % (user, start, end, (values['lastTime'] - values['startTime']).seconds + 1, values['pageCount']))
                    
                    else:
                        break  # All the users in user_updated_list are active so far
            
            if ip not in user_list:  # If user starts a new session, initialize all related record of this session
                user_list.append(ip)
                request_dict[ip] = {'startTime':timestamp, 'lastTime':timestamp, 'pageCount':1}
                user_updated_list.append(ip)

            else:                    # If user is active, update all related record of current session
                request_dict[ip]['lastTime'] = timestamp
                request_dict[ip]['pageCount'] += 1
                user_updated_list.remove(ip)  # Change user's order in user_updated_list by remove and append
                user_updated_list.append(ip)
            


            

    print("hello world!")
    
