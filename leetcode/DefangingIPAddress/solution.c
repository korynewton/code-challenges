char * defangIPaddr(char * address){
    char *defanged = (char *)malloc(sizeof(char) * (strlen(address) + 7));
    memset(defanged, '\0', strlen(address) + 7);

    int d = 0;
    for (int i = 0; address[i] != '\0'; i++)
    {
        if (address[i] == '.')
        {
            defanged[d] = '[';
            defanged[d + 1] = '.';
            defanged[d + 2] = ']';
            d+=3;
        }
        else
        {
            defanged[d] = address[i];
            d++;
        }
    }
    
    return defanged;
}


