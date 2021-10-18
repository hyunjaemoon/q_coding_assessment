import sys
from collections import defaultdict

"""
@author: Hyun Jae Moon
To run this Python Code, write the following line in the console:

% python most_active_cookie.py cookie_log.csv <date>
"""


class CustomQueue:
    """
    Idea: CustomQueue takes in a cookie and organizes two dictionaries.

    self.IDdict is a dictionary of (k, v) = (cookieID, counter)
    self.CNTdict is a dictionary of (k, v) = (counter, list(cookieIDs))
    self.maxCNT is max(counter)
    """

    def __init__(self):
        self.IDdict = defaultdict(lambda: 0)  # (k, v) = (cookieID, counter)
        # (k, v) = (counter, list(cookieIDs))
        self.CNTdict = defaultdict(lambda: [])
        self.maxCNT = 0  # max(counter)

    def add(self, k):
        """
        Q: Why is it OK to append each cookieID to each counter keys?
            Ex) self.CNTdict == {0: ['AtY0laUfhglK3lC7'], 1: ['AtY0laUfhglK3lC7'], ...}

        A: This is because we are only interested in the 'most' active cookies,
        which means that we care only about the self.maxCNT key value for self.IDdict.
        Only the largest counter key would contain the correct list of cookieIDs,
        thus outputting our desired answer. All the intermediate counters are trivial.
        """
        self.IDdict[k] += 1  # Increment the counter of the cookieID k
        # Append cookieID k to the respective counter value
        self.CNTdict[self.IDdict[k]].append(k)
        self.maxCNT = max(self.IDdict[k], self.maxCNT)  # Update self.maxCNT

    def mostActive(self):
        return self.CNTdict[self.maxCNT]  # Return the most active cookieID(s)


class Solution:
    """
    Idea: Solution takes in csvFile, date and solves for the most active cookie.

    Since the log file is sorted. There is no need to read lines that has dates
    prior to the input date. The solution will first reach to the line with
    the input date, and will parse through each line until a different date is
    encountered.

    The solution utilizes a self customized queue to add cookieIDs and track the
    most active cookie on the fly.
    """

    def __init__(self, csvFile, date):
        self.csvFile = csvFile
        self.date = date

    def solve(self):
        # Initiate key variable
        queue = CustomQueue()
        reached = False

        # Reading the Files
        file = open(self.csvFile, 'r')
        file.readline()  # First line of csv is just labels
        line = file.readline()  # First cookie, timestamp pair

        # Parse through each line
        while line:
            cookie, timestamp = line.split(',')
            if reached:  # Once we 'reached' our desired date, we can continue
                # Once we are done, we may break the loop
                if not timestamp.startswith(self.date):
                    break
                queue.add(cookie)
            # First time 'reach'ing our desired date
            elif timestamp.startswith(self.date):
                reached = True
                queue.add(cookie)
            line = file.readline()  # Read the next line
        file.close()
        return queue.mostActive()  # Return the most active cookie(s)


if __name__ == '__main__':
    csvFile = sys.argv[1]
    date = sys.argv[2]
    s = Solution(csvFile, date)
    answer = s.solve()
    for cookie in answer:
        print(cookie)
