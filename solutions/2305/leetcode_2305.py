#------------------------------------------------------
# Solution 1 - recursive (backtracking)
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N?A
# Memory:   N/A


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        result = inf

        cookie_count = len(cookies)

        kids_cookies = [0] * k

        def distributeCookiesRecurse(cookie_index):
            if cookie_index == cookie_count:
                return max(kids_cookies)

            result = inf

            for kid_index in range(k):
                kids_cookies[kid_index] += cookies[cookie_index]

                option = distributeCookiesRecurse(cookie_index + 1)
                result = min(result, option)

                kids_cookies[kid_index] -= cookies[cookie_index]

            return result

        result = distributeCookiesRecurse(0)
        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ early out
#------------------------------------------------------

# Runtime:  52.21%
# Memory:   52.57%


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        result = inf

        cookie_count = len(cookies)
        kids_cookies = [0] * k

        def distributeCookiesRecurse(cookie_index, kids_with_no_cookies):
            nonlocal cookie_count

            remaining_bags = cookie_count - cookie_index
            if remaining_bags < kids_with_no_cookies:
                return inf

            if cookie_index == cookie_count:
                return max(kids_cookies)

            result = inf

            for kid_index in range(k):
                new_kids_with_no_cookies = kids_with_no_cookies
                if kids_cookies[kid_index] == 0:
                    new_kids_with_no_cookies -= 1

                kids_cookies[kid_index] += cookies[cookie_index]

                option = distributeCookiesRecurse(cookie_index + 1, new_kids_with_no_cookies)
                result = min(result, option)

                kids_cookies[kid_index] -= cookies[cookie_index]

            return result

        result = distributeCookiesRecurse(0, k)
        return result