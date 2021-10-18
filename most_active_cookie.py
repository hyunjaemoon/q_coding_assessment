import sys
from collections import defaultdict


class CustomQueue:
    """
    Idea: CustomQueue takes in a cookie and organizes two dictionaries.

    self.IDdict is a dictionary of (k, v) = (cookieID, counter)
    self.CNTdict is a dictionary of (k, v) = (counter, list(cookieIDs))
    self.maxCNT is max(counter)
    """

    def __init__(self):
        # (k, v) = (cookieID, counter)
        self.IDdict = defaultdict(lambda: 0)
        # (k, v) = (counter, list(cookieIDs))
        self.CNTdict = defaultdict(lambda: [])
        self.maxCNT = 0  # max(counter)

    def add(self, k):
        """
        All the intermediate counters less than self.maxCNT will have the wrong
        list of cookieIDs. However, this is trivial because we only care about
        the 'most' active cookies.
        """
        self.IDdict[k] += 1  # Increment the counter of the cookieID k
        # If the counter of the cookieID k is less than maxCNT, there's no need to do anything.
        if self.maxCNT > self.IDdict[k]:
            return
        self.maxCNT = max(self.maxCNT, self.IDdict[k])  # Update self.maxCNT
        # Append cookieID k to the respective counter value
        self.CNTdict[self.maxCNT].append(k)

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
