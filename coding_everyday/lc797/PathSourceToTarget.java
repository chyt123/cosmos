import java.util.*;

public class PathSourceToTarget {
  public static List<List<Integer>> allPathsSourceTarget(int[][] graph) {
    List<List<Integer>> result = new LinkedList<>();
    int[] visited = new int[graph.length];

    PriorityQueue<Integer> q = new PriorityQueue<>();

    q.add(0);
    LinkedList<Integer> init = new LinkedList<>();
    init.add(0);
    result.add(init);

    while (q.size() > 0) {

      int a = q.poll();
      if (visited[a] > 0) {
        continue;
      } else {
        visited[a] = 1;
      }

      Set<List<Integer>> toDelete = new HashSet<>();
      for (int i = 0; i < graph[a].length; i++) {
        q.add(graph[a][i]);
        List<List<Integer>> toAdd = new LinkedList<>();
        if (toDelete.size() == 0) {
          for (List<Integer> list : result) {
            if (list.get(list.size() - 1) == a) {
              LinkedList<Integer> newList = new LinkedList<>(list);
              newList.add(graph[a][i]);
              toAdd.add(newList);
              toDelete.add(list);
            }
          }
        } else {
          for (List<Integer> list : toDelete) {
            if (list.get(list.size() - 1) == a) {
              LinkedList<Integer> newList = new LinkedList<>(list);
              newList.add(graph[a][i]);
              toAdd.add(newList);
            }
          }
        }
        result.addAll(toAdd);
      }
      result.removeAll(toDelete);


    }

    return result;
  }

  public static List<List<Integer>> allPathsSourceTarget2(int[][] graph) {
    List<List<Integer>> result = new LinkedList<>();
    LinkedList<Integer> path = new LinkedList<>();
    Stack<List<Integer>> stack = new Stack<>();
    path.add(0);
    a(0, path, result, graph);
    return result;
  }

  public static void a(int target, LinkedList<Integer> path, List<List<Integer>> result, int[][] graph) {
    int[] list = graph[target];
    for (int i : list) {
      path.add(i);
      if (i == graph.length - 1) {
        List<Integer> res = new LinkedList<>(path);
        result.add(res);
      } else {
        a(i, path, result, graph);
      }
      path.removeLast();
    }
  }

  public static void main(String[] args) {
    int[][] input = {{4,3,1},{3,2,4},{3},{4},{}};
    //int[][] input = {{1,2}, {3}, {3}, {}};
    List<List<Integer>> res = allPathsSourceTarget2(input);
    System.out.println(res.size());
  }
}
