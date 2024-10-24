#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

if __name__ == "__main__":
    total_file_size = 0
    count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in status_codes}

    def print_stats(stats: dict, total_file_size: int) -> None:
        """Print the statistics"""
        print("File size: {:d}".format(total_file_size))
        for code, value in sorted(stats.items()):
            if value > 0:
                print("{}: {}".format(code, value))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            
       
            if len(data) < 7:
                continue
            
           
            try:
                status_code = data[-2]
                file_size = int(data[-1])

               
                total_file_size += file_size

                
                if status_code in stats:
                    stats[status_code] += 1

            except (ValueError, IndexError):
                continue  
            
           
            if count % 10 == 0:
                print_stats(stats, total_file_size)

       
        print_stats(stats, total_file_size)

    except KeyboardInterrupt:
        print_stats(stats, total_file_size)
        raise 
