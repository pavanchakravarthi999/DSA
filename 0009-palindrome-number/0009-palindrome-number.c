

bool isPalindrome(int x){
     long int y,sum=0,temp;
    temp=x;
    if(x<0){
        return false;
    }
    while(x>0){
    y=x%10;
    sum=sum*10+y;
    x=x/10;
    }
    x=temp;
    if(sum==x)
    return true;
    else 
    return false;
    
    return 0;
}

