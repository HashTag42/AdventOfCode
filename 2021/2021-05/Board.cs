using System;

class Board {

    const int maxSize = 1000;

    public Board() { }

    /// <summary>Returns true if the line was added to the board.</summary>
    public bool AddLine(string line) {
        bool Added = false;

        int startIndex = 0, length = line.IndexOf(',');
        int x1 = int.Parse(line.Substring(startIndex, length));
        startIndex = length + 1; length = line.IndexOf(' ') - startIndex;
        int y1 = int.Parse(line.Substring(startIndex, length));
        startIndex = line.IndexOf("> ") + 2; length = line.IndexOf(',', startIndex) - startIndex;
        int x2 = int.Parse(line.Substring(startIndex, length));
        startIndex = line.IndexOf(',', startIndex) + 1;
        int y2 = int.Parse(line.Substring(startIndex));

        if((x1 == x2) || (y1 == y2)) {
            int xDistance = Math.Abs(x2 - x1);
            int yDistance = Math.Abs(y2 - y1);
            int xDirection = x1 <= x2 ? 1 : -1;
            int yDirection = y1 <= y2 ? 1 : -1;
            for(int x = 0; x <= xDistance; x++) {
                for(int y = 0; y <= yDistance; y++) {
                    _board[x1+(x*xDirection),y1+(y*yDirection)]++;
                    Added = true;
                }
            }
        }

        return Added;
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
                    Console.Write('.');
                } else {
                    Console.Write(_board[y,x]);
                }
            }
            Console.Write('\n');
        }
        return output;
    }

    private int[,] _board = new int[maxSize,maxSize];
}