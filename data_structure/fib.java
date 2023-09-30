public class fib {
    
    public static int fibonacci(int num){
        int[] arr = new int[num+2];//num이 0일경우 index 예외 발생방지
        arr[1] = 1;
        return fibo_arr(num,arr);
    }
    public static int fibo_arr(int num,int[] arr){
        if (num ==0){
            return 0;
        }
        else if (arr[num] == 0){
            arr[num] = fibo_arr(num-1,arr) + fibo_arr(num-2,arr);
        }
        //System.out.println(Arrays.toString(arr));
        return arr[num];
    }

}
