#!/usr/bin/python3
"""
log parsing
"""
import sys
import re


def extract_input(input_line):
    """Extracts sections of the log."""
    # Define the pattern for matching log lines
    fp = (
        r'(?P<ip>\S+)\s-\s',  # Match IP address
        r'\[(?P<date>[^\]]+)\]\s',  # Match date enclosed in square brackets
        r'"GET /projects/260 HTTP/1.1"\s',  # Match the specific request pattern
        r'(?P<status_code>\d{3})\s',  # Match the 3-digit status code
        r'(?P<file_size>\d+)'  # Match the file size
    )
    # Combine the patterns into a single regular expression
    log_fmt = '{}{}{}{}{}'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    # Match the log line against the combined pattern
    match = re.match(log_fmt, input_line)
    # If the line matches, extract and return the status code and file size
    if match:
        return {
            'status_code': match.group('status_code'),  # Extract status code
            'file_size': int(match.group('file_size'))  # Extract file size and convert to integer
        }
    # Return None if the line does not match the expected format
    return None


def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated log stats."""
    # Print the total file size
    print('File size: {}'.format(total_file_size))
    # Print the count of each status code in ascending order
    for status_code in sorted(status_codes_stats.keys()):
        count = status_codes_stats[status_code]  # Get the count for the status code
        # Print only if the count is greater than 0
        if count > 0:
            print('{}: {}'.format(status_code, count))


def main():
    """Main function to read log lines and compute metrics."""
    # Initialize the total file size
    total_file_size = 0
    # Initialize a dictionary to count the occurrences of each status code
    status_codes_stats = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    # Initialize a counter for the number of lines processed
    line_count = 0

    try:
        # Read lines from standard input (stdin)
        for line in sys.stdin:
            line_count += 1  # Increment the line counter
            # Extract information from the current log line
            line_info = extract_input(line.strip())
            if line_info:
                # Add the file size to the total file size
                total_file_size += line_info['file_size']
                status_code = line_info['status_code']  # Get the status code
                # If the status code is one of the expected codes, increment its count
                if status_code in status_codes_stats:
                    status_codes_stats[status_code] += 1

            # Every 10 lines, print the statistics
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass
    finally:
        # Print the final statistics when the script ends
        print_statistics(total_file_size, status_codes_stats)


if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
