import re

def extract_data(log_file):
    regex = '([\d\.]+) - - \[(.*?)\] "(.*?)" (\d+) (.+) "(.*?)" "(.*?)"'
    data = []
    log_file = open(log_file,'r')
    for log_line in log_file:
        log_line = list(re.match(regex,log_line).groups())
        parsed_line = {}
        parsed_line['IP'] = log_line[0]
        parsed_line['Timestamp'] = log_line[1]
        parsed_line['URL'] = log_line[2]
        parsed_line['Status Code'] = int(log_line[3])
        if '-' in log_line[4]:
            log_line[4] = 0
        else:
            log_line[4] = int(log_line[4])
        parsed_line['Return Size'] = log_line[4]
        parsed_line['Referer'] = log_line[5]
        parsed_line['User Agent'] = log_line[6]
        data.append(parsed_line)
    return data


