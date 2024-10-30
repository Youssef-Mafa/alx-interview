#!/usr/bin/python3
"""
UTF-8 Validation - Optimized
"""

def validUTF8(data) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    number_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        if number_bytes == 0:
            # Determine the number of bytes in this UTF-8 character
            mask = 1 << 7
            while mask & byte:
                number_bytes += 1
                mask >>= 1

            if number_bytes == 0:
                continue

            # UTF-8 character encoding is invalid if 1 byte or more than 4 bytes
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Subsequent bytes should start with '10' in binary
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        # Decrement the bytes counter
        number_bytes -= 1

    # If we finish with number_bytes != 0, then it was an incomplete character
    return number_bytes == 0
