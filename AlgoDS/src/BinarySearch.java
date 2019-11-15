class BinarySearch {
	
	int BinarySearch(int arr[], int left, int right, int value)
	{
		while(left <= right)
		{
			int mid = (left + right)/2;
			
			if(arr[mid] == value){
				return mid;
			}
			
			if(arr[mid] < value){
				left = mid + 1; 
			}else{
				right = mid - 1;
			}
		}
		
		return -1;
	}
	

	public static void main(String[] args) {
		BinarySearch object = new BinarySearch();
		int arr[] = {1,2,3,7,9,100};
		int arrLength = arr.length-1;
		int value = 7;
		
		int result = object.BinarySearch(arr, 0, arrLength, value);
		if(result == -1){
			System.out.println("Value not found!");
		}else{
			System.out.println("Value found on index : " + result);
		}
	}
}
