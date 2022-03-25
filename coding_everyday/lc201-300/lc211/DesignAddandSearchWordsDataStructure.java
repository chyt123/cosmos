import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

class Node {
    public Node[] children;
    public boolean isEnd;
    public Node () {
        this.children = new Node[26];
        this.isEnd = false;
    }
}

class WordDictionary {
    private Node node;
    public WordDictionary() {
        node = new Node();
    }

    public void addWord(String word) {
        Node curNode = node;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (curNode.children[ch - 'a'] == null) {
                curNode.children[ch - 'a'] = new Node();
            }
            curNode = curNode.children[ch - 'a'];
        }
        curNode.isEnd = true;
    }

    public boolean search(String word) {
        return search(word, 0, node);
    }

    private boolean search(String word, int idx, Node curNode) {

        if (idx == word.length()) {
            return curNode.isEnd;
        }

        char ch = word.charAt(idx);
        int i = ch - 'a';
        if (ch == '.') {
            for (int j = 0; j < 26; j++) {
                if (curNode.children[j] != null && search(word, idx + 1, curNode.children[j])) {
                    return true;
                }
            }
        } else {
            if (curNode.children[i] != null) {
                return search(word, idx + 1, curNode.children[i]);
            }
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

public class DesignAddandSearchWordsDataStructure {
    public static void main(String[] args) {
        String[] cmds = {"WordDictionary","addWord","addWord","addWord","search","search","search","search"};
        String[] vals = {"","bad","dad","mad","basdf","bad",".ad","b.."};
        WordDictionary wordDictionary = null;

        for (int i = 0; i < cmds.length; i++) {
            switch (cmds[i]) {
                case "WordDictionary" -> wordDictionary = new WordDictionary();
                case "addWord" -> wordDictionary.addWord(vals[i]);
                case "search" -> System.out.println(wordDictionary.search(vals[i]));
            }
        }
    }
}

