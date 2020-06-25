function canAttendMeetings(intervals: number[][]): boolean {
    //if intervals is empty return true
    if (intervals.length === 0) return true
    
    //sort intervals by starting time ascending
    const sortedByStart: number[][] = intervals.sort((a, b) => a[0] - b[0]) 
    
    let [start,end] = sortedByStart[0]
    for (let i:number = 1; i<sortedByStart.length; i++) {
        const nextStart:number = sortedByStart[i][0]
        const nextEnd:number = sortedByStart[i][1]

	//as long as the nextStart time is greater than or equal
	//to the previos end, continue
        if (nextStart >= end) {
            start = nextStart
            end = nextEnd
        } else {
            return false
        }
    }
    
    return true
};
