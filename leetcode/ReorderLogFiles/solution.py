class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_alphanumeric(log):
            identifier, *words = log.split()
            return [words + [identifier]]

        # initialize lists for letter logs and digit logs
        ll = []
        dl = []

        # loop over logs
        for log in logs:
            split = log.split(' ')

            # if the second word in log is a digit, we know it is a digit log
            # appending these as we see them will store them in the correct order
            if split[1].isdigit():
                dl.append(log)
            # else it is a letter log
            else:
                ll.append(log)

        # sort letter logs by words after identifier
        ll.sort(key=sort_alphanumeric)

        return ll + dl
