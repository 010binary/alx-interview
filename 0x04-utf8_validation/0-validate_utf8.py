#!/usr/bin/python3
"""
UTF-8 python validator
"""


def validUTF8(data):
    """
    Function to validate UTF-8
    the params data is the data
    """

    # Counter for remaining bytes in current character
    remaining_bytes = 0

    # Bit masks
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Ensure we only consider the 8 least significant bits
        byte = byte & 255

        if remaining_bytes == 0:
            # This byte starts a new character
            if byte >> 5 == 0b110:     # 2-byte character
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                remaining_bytes = 2
            elif byte >> 3 == 0b11110: # 4-byte character
                remaining_bytes = 3
            elif byte >> 7:            # Invalid start byte
                return False
        else:
            # This should be a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False
            remaining_bytes -= 1

    # All characters should be complete
    return remaining_bytes == 0
