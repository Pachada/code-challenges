"""
Valid IP Addresses | AlgoExpert
You're given a string of length 12 or smaller, containing only digits. 
Write a function that returns all the possible IP addresses that can be created by inserting three .s in the string.

An IP address is a sequence of four positive integers that are separated by .s, 
where each individual integer is within the range 0 - 255, inclusive.

An IP address isn't valid if any of the individual integers contains leading 0s. 
For example, "192.168.0.1" is a valid IP address, but "192.168.00.1" and "192.168.0.01" aren't, 
because they contain "00" and 01, respectively. 
Another example of a valid IP address is "99.1.1.10"; conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.

Your function should return the IP addresses in string format and in no particular order.
If no valid IP addresses can be created from the string, your function should return an empty list.


Sample Input
string = "1921680"
Sample Output
[
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0"
]
// The IP addresses could be ordered differently.
"""

# O(1) time | O(1) space -> at most we can create 2**32 ip addresses
def validIPAddresses(string):
    valid_ip_addresses = [] 

    # Outer loop iterates through the first segment of the IP address.
    for i in range(1, min(len(string), 4)):
        current_ip = ["", "", "", ""] 

        # Slice the first segment and check its validity.
        current_ip[0] = string[:i]
        if not isIPValid(current_ip[0]):
            continue 

        # Middle loop iterates through the second segment of the IP address.
        for j in range(i+1, i + min(len(string) - i, 4)):
            # Slice the second segment and check its validity.
            current_ip[1] = string[i:j]
            if not isIPValid(current_ip[1]):
                continue 

            # Inner loop iterates through the third segment of the IP address.
            for k in range(j+1, j + min(len(string) - j, 4)):
                # Slice the third and fourth segments, and check their validity.
                current_ip[2] = string[j:k]
                current_ip[3] = string[k:]
                if isIPValid(current_ip[2]) and isIPValid(current_ip[3]):
                    # If both segments are valid, join them into an IP address string and append to the result list.
                    valid_ip_addresses.append(".".join(current_ip))

    return valid_ip_addresses 


def isIPValid(ip):
    ip_as_int = int(ip)  # Convert segment to integer to remove leading zeros.
    if ip_as_int > 255:
        return False  # If segment value is greater than 255, it's invalid.

    # Check that the length of the segment is the same before and after conversion to integer (no leading zeros).
    return len(ip) == len(str(ip_as_int))


if __name__ == "__main__":
    string = "1921680"
    print(validIPAddresses(string))  

