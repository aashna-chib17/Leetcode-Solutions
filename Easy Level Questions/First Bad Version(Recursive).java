/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        return binary(0,n-1);
        
}
    public int binary(int start, int end){
        while(start <= end){
            int mid = start + (end-start)/2;
            if(isBadVersion(mid) == false){
                return binary(mid+1,end);
            }
            else{
                return binary(start,mid-1);
            }
        }
        return start;
    }
}
