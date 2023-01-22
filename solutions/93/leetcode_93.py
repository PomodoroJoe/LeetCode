#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  70.23%
# Memory:   79.91%

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        # ip address = [0, 0, 0, 0]
        partial_ips = [[]]

        for c in s:
            num = int(c)

            new_partial_ips = []

            for ip in partial_ips:
                # add num as new element
                if len(ip) < 4:
                    new_ip = ip.copy()
                    new_ip.append(num)
                    new_partial_ips.append(new_ip)

                # add num to the last element
                new_ip = ip.copy()
                last_element = new_ip[-1] if len(new_ip) > 0 else None

                if last_element:
                    new_last_element = (last_element * 10) + num
                    if new_last_element < 256:
                        new_ip[-1] = new_last_element
                        new_partial_ips.append(new_ip)

            partial_ips = new_partial_ips

        for ip in partial_ips:
            if len(ip) != 4:
                continue

            ip_string = "{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3])
            result.append(ip_string)

        return result


#------------------------------------------------------
# Solution 2 - pythonic string w/ join
#------------------------------------------------------

# Runtime:  50.26%
# Memory:   31.67%

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        # ip address = [0, 0, 0, 0]
        partial_ips = [[]]

        for c in s:
            num = int(c)

            new_partial_ips = []

            for ip in partial_ips:
                # add num as new element
                if len(ip) < 4:
                    new_ip = ip.copy()
                    new_ip.append(num)
                    new_partial_ips.append(new_ip)

                # add num to the last element
                new_ip = ip.copy()
                last_element = new_ip[-1] if len(new_ip) > 0 else None

                if last_element:
                    new_last_element = (last_element * 10) + num
                    if new_last_element < 256:
                        new_ip[-1] = new_last_element
                        new_partial_ips.append(new_ip)

            partial_ips = new_partial_ips

        for ip in partial_ips:
            if len(ip) != 4:
                continue

            ip_string = '.'.join(map(str, ip))
            result.append(ip_string)

        return result


#------------------------------------------------------
# Solution 3 - index vs. iterator
#------------------------------------------------------

# Runtime:  89.39%
# Memory:   31.67%

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        # ip address = [0, 0, 0, 0]
        partial_ips = [[int(s[0])]]

        for i in range(1, len(s)):
            num = int(s[i])

            new_partial_ips = []

            for ip in partial_ips:
                # add num as new element
                if len(ip) < 4:
                    new_ip = ip.copy()
                    new_ip.append(num)
                    new_partial_ips.append(new_ip)

                # add num to the last element
                new_ip = ip.copy()
                last_element = new_ip[-1] if len(new_ip) > 0 else None

                if last_element:
                    new_last_element = (last_element * 10) + num
                    if new_last_element < 256:
                        new_ip[-1] = new_last_element
                        new_partial_ips.append(new_ip)

            partial_ips = new_partial_ips

        for ip in partial_ips:
            if len(ip) != 4:
                continue

            ip_string = "{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3])
            result.append(ip_string)

        return result
