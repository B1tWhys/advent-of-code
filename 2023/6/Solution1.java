import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Solution1 {

  public static void main(String[] args) {
    String fname = args[0];
    try {
      FileInputStream inputStream = new FileInputStream(fname);
      List<Integer> times = readIntListLine(inputStream);
      List<Integer> dists = readIntListLine(inputStream);

      System.out.printf("Times:\t%s\nDists:\t%s\n", times.toString(), dists.toString());
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  private static List<Integer> readIntListLine(FileInputStream inputStream) {
    String line = readLine(inputStream);
    String numListStr = line.split(":", 2)[1];
    return Arrays.stream(numListStr.split(" "))
        .filter(i -> !i.isBlank())
        .map(s -> Integer.valueOf(s))
        .collect(Collectors.toList());
  }

  private static String readLine(FileInputStream inputStream) {
    StringBuilder ret = new StringBuilder();
    try {
      while (true) {
        int ch = inputStream.read();
        if (ch == '\n' || ch == -1) {
          break;
        }
        ret.append((char) ch);
      }
    } catch (Exception e) {
      return "";
    }

    return ret.toString();
  }
}