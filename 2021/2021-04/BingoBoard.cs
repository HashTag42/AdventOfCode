using System;

public class BingoBoard {

    public BingoCell[,] board { get; }

    public BingoBoard()
    {
        board = new BingoCell[5,5];
    }


    public class BingoCell {
        public int Number { get; }
        public bool Marked { get; set; }

        public BingoCell() : this(1)
        {
            Console.WriteLine(Number);
        }
        public BingoCell(int inNumber) {
            Number = inNumber;
            Marked = false;
        }
    }
}