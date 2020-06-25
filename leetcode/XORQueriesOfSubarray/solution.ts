function xorQueries(arr: number[], queries: number[][]): number[] {
    //store resulting XORs
    const result: number[] = []
    
    //loop through queries
    for (let i:number = 0; i<queries.length; i++) {
        //destructure each query to get left and right indices
        const [L, R] = queries[i];
        
        //store the value at L
        let temp:number = arr[L];
        for (let j:number = L+1; j<=R; j++) {
            //continue to replace temp with temp XOR with the next element
            temp = temp ^ arr[j]
        }
        //after iterating from L to R indices, push to result to result array
        result.push(temp)
    }

    return result
};
