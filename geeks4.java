import java.util.Scanner;
import java.util.Arrays;

public class geeks4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number element of an array :");
        int n = sc.nextInt();

        int[] array = new int[n];

        System.out.println("Enter  an array  elements: ");
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();

        }

        System.out.println("Orignal Array:" + Arrays.toString(array));

        int[] reversedArray = reverseArray(array);
        System.out.println("reversed array :" + Arrays.toString(reversedArray));

        sc.close();

    }

    public static int[] reverseArray(int[] arr) {
        int start = 0, end = arr.length - 1;
        while (start < end) {

            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;

        }

        return arr;

    }
}