import java.util.Scanner;
import java.util.Arrays;

public class geeks3java {

    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);

        System.out.println("Enter the size of the array  ");
        int n = sc.nextInt();

        int arr[] = new int[n];
        System.out.println(("Enter " + n + "Array "));
        for (int i = 0; i < n; i++){
            arr[i] = sc.nextInt();



        }

        int left = 0, right = n - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;


            left++;
            right--;

            
        }

        System.out.println("Reversed array :");
        for(int num : arr){
            System.out.println(num + " ");
        }









    }
}