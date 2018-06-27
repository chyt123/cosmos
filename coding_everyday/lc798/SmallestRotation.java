//798
public class SmallestRotation {
  public static int solution(int[] arr) {
    int[] score1 = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
      int diff = arr[i] - i;
      if (diff < (arr.length - i) && diff >= 0) {
        score1[diff]++;
        score1[(arr.length-i) % arr.length]--;
      } else if (-diff <= i && diff < 0) {
        score1[arr.length-(-diff)]++;
        score1[(arr.length-i) % arr.length]--;
      }
    }

    score1[0] = 0;


    for (int i = 1; i < arr.length; i++) {
      score1[i] = score1[i - 1] + score1[i];
    }

    int k = 0;
    int tmp = score1[0];
    for (int i = arr.length - 1; i > 0; i--) {
      if (score1[i] > tmp) {
        tmp = score1[i];
        k = i;
      }
    }
    return (arr.length - k) % arr.length;

  }

  public static void main(String[] args) {
    int[] a = {2, 3, 1, 4, 0};
    System.out.println(solution(a));
  }
}
