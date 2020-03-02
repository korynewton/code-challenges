class SolutionOne:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        total_passengers = [0]*1000
        for i in range(len(trips)):
            passengers, start,end = trips[i]
            for i in range(start,end):
                total_passengers[i] += passengers
        return max(total_passengers)<=capacity



class SolutionTwo:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #sort trips by starting point
        trips=sorted(trips,key=lambda x:x[1])
        current = 0
        start = 0
        stack = []

        for i in range(len(trips)):
            start = 0
            #remove passengers
            while stack and start < len(stack):
                if stack[start][2]<=trips[i][1]:
                    current-=stack[start][0]
                    stack.pop(start)
                else:
                    start+=1

            current += trips[i][0]
            stack.append(trips[i])
            if current>capacity:
                return False

        return True
