public class Kata
{
    public static int FindEvenIndex(int[] arr)
    {
        //Code goes here!
        int sumleft = 0;
        int sumright = 0;
        int index = -1;
        for(int i = 0; i < arr.Length; i++) {
            sumleft += arr[i];
        }
        for (int j = arr.Length - 1; j > -1; j--)
        {
            sumleft -= arr[j];
            if (j <= arr.Length - 2)
            {
                sumright += arr[j + 1];
                if (sumleft == sumright)
                    index = j;
            }
        }
        return index;
    }
}