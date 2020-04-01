//Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.


int firstUniqChar(char * s){
    // initialize an array for 128 unique asci characters that will hold the count of each character
    int asci_array[128] = { 0 };
    
    // iterate through s and increment asci_array element at a given index
    for (int i = 0; s[i] != '\0'; i++)
    {
        asci_array[s[i]]++;
    }
    
    //iterate through s again and check if an element at a particular index in asci_array is 1
    //This indicates there is only 1 in the string, return that index
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (asci_array[s[i]] == 1)
        {
            return i;
        }
    }
    
    return -1;
}

