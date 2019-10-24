### 本质上还是一个DFS问题，因为并不需要一个范围一个范围的搜，搜到一个可行的就继续往更远的地方探查
* 然后能做的就是写一写edge case，然后入口方面限制一下，节约空间
```java
public class Solution {
public boolean exist(char[][] board, String word) {
    if (word.length() == 0 || board.length == 0) {
        return false;
    }
    
    for(int i = 0; i < board.length; i++)
        for(int j = 0; j < board[0].length; j++){
            if (board[i][j] == word.charAt(0)) {
                if(exist(board, i, j, word, 0))
                return true;
            }
        }
    return false;
}
private boolean exist(char[][] board, int i, int j, String word, int ind){
    if(ind == word.length()) return true;
    if(i > board.length-1 || i <0 || j<0 || j >board[0].length-1 || board[i][j]!=word.charAt(ind))
        return false;
    board[i][j]='*';
    boolean result =    exist(board, i-1, j, word, ind+1) ||
                        exist(board, i, j-1, word, ind+1) ||
                        exist(board, i, j+1, word, ind+1) ||
                        exist(board, i+1, j, word, ind+1);
    board[i][j] = word.charAt(ind);
    return result;
}
}
```
