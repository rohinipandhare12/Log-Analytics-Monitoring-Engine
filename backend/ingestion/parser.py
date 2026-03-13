#which is used to handle the data and reuseable code which is seperate from the dask 
#loading the data 
#parsing the data 
#structure the data and load the data using injection files 
#parser: parser is a python method which is used to convert the raw data into structured data based on the schema which we have defined(translator) 
#without parser: no columns are defined
#no filtering is done 
#no anomaly is detection or no aggregation 
#with parsing: we can filter error logs 
#detect the unsual patterns 
#it converts raw log data to the machine readable language 
import re  #to work with regular expressions

# LOG_PATTERN = re.compile(
#     r"(?P<timestamp>[\d\-:\s]+)\s"
#     r"(?P<level>\w+)\s"
#     r"(?P<service>\w+)\s"
#     r"(?P<message>.*?)(?:\suser_id=(?P<user_id>\d+))?$"
# )
# def parse_log_line(line):
#     #logic to matching log pattern
#     match=LOG_PATTERN.match(line) 
#     if not match: #if match is not found
#         return None
#     return {
#         "timestamp": match.group("timestamp"),
#         "level": match.group("level"),
#         "service": match.group("service"),
#         "message": match.group("message")
#     }

# from datetime import datetime #import datetime is a module

# LOG_PATTERN = re.compile(       #initializing regular exptessions. which creates a regex patterns.
#     r'(?P<timestamp>\S+ \S+)\s+'
#     r'(?P<level>\S+)\s+'
#     r'(?P<service>\S+)\s+'
#     r'(?P<message>.*)'
# )

# def parse_log_line(line):
#     match = LOG_PATTERN.match(line) #line is the one to be matched with LOG_PATTERN.

#     if not match:  #if no match found
#         return None

#     data = match.groupdict()

#     data["timestamp"] = datetime.strptime(  #strptime-->Converts timestamp into string(datetime object)
#         data["timestamp"], "%Y-%m-%d %H:%M:%S"
#     )

#     data["service"] = "system"            #default value
#     data["raw"] = line.strip()
    
#     return data

from datetime import datetime

def parse_log_line(line):
    try:
        parts = line.strip().split()

        # Skip invalid lines
        if len(parts) < 3:
            return None

        # Combine date + time
        timestamp_str = parts[0] + " " + parts[1]

        level = parts[2]

        # Everything else = message
        message = " ".join(parts[3:])

        timestamp = datetime.strptime(
            timestamp_str,
            "%Y-%m-%d %H:%M:%S"
        )

        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }

    except Exception as e:
        print("Parse error:", line)
        return None

#Groupdict()
#Strip()
#re.compile(): recompile is a method in python which is use to create regex patterns.
#python regex: python regular expression are used for searching matching and extract the data pattern from the given text.
#r-> raw data (log data)
#?-> starting of pattern code
#P<timestamp>,P<level>,P<service>, P<message>:which is used to capture the names of particular data.
#\s-> use to remove the white spaces between the name given. 
#parser=>parsing the data. convert the raw data into structured data
#groupdict() -> convert raw data into structure data (dictionary)
# r'' -> raw Data
#?P<timestamp> -> named group
#s+ -> for removing spaces one or more
#^ -> start of line
#$ -> end of line
#\S -> non-space character. for removing space in mid of the line

