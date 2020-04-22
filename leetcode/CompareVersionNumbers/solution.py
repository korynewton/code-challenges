class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        # the level we are comparing versions
        level = 0

        while level < len(version1) and level < len(version2):
            # comparing each level, returning is a deciscion can be made
            if int(version1[level]) > int(version2[level]):
                return 1
            elif int(version2[level]) > int(version1[level]):
                return -1
            level += 1

        # we wont know ahead of time which version we have hit the end on,
        # one or neither of these while loops will run
        while level < len(version1):
            if int(version1[level]):
                return 1
            level += 1
        while level < len(version2):
            if int(version2[level]):
                return -1
            level += 1

        # if still not clear which version is larger, they are the same
        return 0
