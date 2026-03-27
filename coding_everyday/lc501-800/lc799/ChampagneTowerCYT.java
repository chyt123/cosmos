public class ChampagneTower {
  public static double solution(int pours, int i, int j) {
    double[] prev = new double[1];
    double[] next = new double[1];
    for (int k = 0; k <= i; k++) {
      for (int l = 0; l <= k; l++) {
        if (k == 0 && l == 0) {
          next[l] += pours;
        } else if (l == 0){
          if (prev[l] > 1) {
            double diff = (double) ((prev[l] - 1) * 0.5);
            next[l] += diff;
          }
        } else if (l == k) {
          if (prev[l-1] > 1) {
            double diff = (double) ((prev[l-1] - 1) * 0.5);
            next[l] += diff;
            prev[l-1] = 1;
          }
        } else {
          if (prev[l-1] > 1) {
            double diff = (double) ((prev[l-1] - 1) * 0.5);
            next[l] += diff;
            prev[l-1] = 1;
          }

          if (prev[l] > 1) {
            double diff = (double) ((prev[l] - 1) * 0.5);
            next[l] += diff;
          }
        }
      }
      prev = next;
      next = new double[k+2];
    }
    return prev[j] > 1 ? 1 : prev[j];
  }


  public static void main(String[] args) {
    double d = solution(6, 3, 1);
    System.out.println(d);
  }
}
