public class RotateString {
  public static boolean rotateString(String A, String B) {
    if (A.length() == 0) {
      if (B.length() == 0) {
        return true;
      } else {
        return false;
      }
    }

    if (A.length() != B.length()) {
      return false;
    }



    char a = A.charAt(0);

    n: for (int k = 0; k < B.length(); k++) {
      if (B.charAt(k) == a) {
        for (int i = 0; i < A.length(); i++) {
          if (B.charAt((k + i) % B.length()) != A.charAt(i)) {
            continue n;
          }
        }
        return true;
      }
    }
    return false;
  }

  public static boolean rotateString2(String A, String B) {
    if (A.length() != B.length()) {
      return false;
    }

    String x = A + A;
    if (x.contains(B)) {
      return true;
    } else {
      return false;
    }
  }

  public static void main(String[] args) {
    String a = "abcde";
    String b = "cdeab";
    System.out.println(rotateString(a,b));
  }
}


