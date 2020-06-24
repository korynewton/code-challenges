function toGoatLatin(S: string): string {
    //split string by words
    const strSplit:string[] = S.split(" ")
    
    for(let i:number = 0; i<strSplit.length; i++) {
        
        //check if word begins with a vowel
        if (isVowel(strSplit[i][0])) {
            strSplit[i] = strSplit[i] + "ma"
        //in the case the word starts with consonant
        } else {
            strSplit[i] = strSplit[i].slice(1) + strSplit[i][0] + "ma"   
        }
        //add increasingly more a's to end of word
        strSplit[i] = strSplit[i] + 'a'.repeat(i+1)
    }
    
    //join array to string, joined by ' '
    return strSplit.join(" ")    
};


function isVowel(char:string) {
    return ['a','e','i','o', 'u'].includes(char.toLowerCase())
}
