"""
🌐 IP ADDRESS SORTING 🌐

Task: Read a list of IPv4 addresses and sort them in ascending order based on their single decimal (32-bit integer) representation.

## Context on IPv4:
An IPv4 address is a 32-bit number, represented as four decimal numbers (octets), ranging from 0 to 255, separated by dots (e.g., 192.168.1.2).

## Decimal Conversion Rule (The 'Key' for sorting):
To convert an IPv4 address (a.b.c.d) into a single decimal number, use the formula:
Decimal Value = (a * 256³) + (b * 256²) + (c * 256¹) + (d * 256⁰)
Example: 192.168.1.2
Decimal Value = (192 * 256³) + (168 * 256²) + (1 * 256¹) + (2 * 256⁰) = 3232235778

## Input Format:
1. An integer N (N ≥ 1), the number of IP addresses.
2. N subsequent lines, each containing a valid IPv4 address string.

## Output Format:
Print the IP addresses in ascending order based on their calculated decimal value. Each IP address should be on a separate line, maintaining its original string format.

## Implementation Goal:
The primary implementation challenge is to create a robust sorting key function that correctly performs the IPv4-to-decimal conversion for each address string.
"""

all_ip_address = [input() for _ in range(int(input()))]


def pattern_sorted(iterable):
    res = 0
    for i, n in enumerate(iterable.split(".")[::-1], ):
        res += int(n) * (256 ** i)
    return res


print(*sorted(all_ip_address, key=pattern_sorted), sep="\n")
