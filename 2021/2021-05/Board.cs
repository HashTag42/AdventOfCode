using System;
using System.Diagnostics;

class Board {

    const int maxSize = 1000;

    public Board() { }

    public void AddLine(int x1, int y1, int x2, int y2, bool includeDiagonals) {
        int xDistance = Math.Abs(x2 - x1);
        int yDistance = Math.Abs(y2 - y1);
        int xDirection = x1 <= x2 ? 1 : -1;
        int yDirection = y1 <= y2 ? 1 : -1;
        // do horizonal and vertical lines
        if((x1 == x2) || (y1 == y2)) {
            for(int x = 0; x <= xDistance; x++) {
                for(int y = 0; y <= yDistance; y++) {
                    int row = x1 + (x * xDirection);
                    int col = y1 + (y * yDirection);
                    _board[row, col]++;
                }
            }
        }
        // do diagonals, but only at exactly 45 degrees
        if(includeDiagonals && (xDistance == yDistance)) {
            for(int i = 0; i <= xDistance; i++) {
                int row = x1 + (i * xDirection);
                int col = y1 + (i * yDirection);
                _board[row, col]++;
            }
        }
    }

    public int CountPoints(int number) {
        int count = 0;
        for(int x = 0; x<maxSize; x++) {
            for(int y = 0; y < maxSize; y++) {
                if(_board[x,y] >= number) {
                    count++;
                }
            }
        }
        return count;
    }

    public override string ToString() {
        string output = null;
        for(int x = 0; x < maxSize; x++) {
            for(int y = 0; y < maxSize; y++) {
                if(_board[y,x] == 0) {
                    output += '.';
                } else {
                    output += _board[y,x];
                }
                output += ' ';
            }
            output +='\n';
        }
        return output;
    }

    private int[,] _board = new int[maxSize,maxSize];
}