using System;
using System.Collections.Generic;
using System.Diagnostics;

public class BingoBoard {

    public BingoCell[,] Board = new BingoCell[5,5];

    public bool IsBingo { get; }

    public int SumUnmarkedCells() {
        int sum = 0;
        for(int row = 0; row < 5; row++) {
            for(int col = 0; col <5; col++) {
                if(!Board[row,col].IsMarked) {
                    sum += Board[row,col].Number;
                }
            }
        }
        return sum;
    }

    public override string ToString()
    {   string result = null;
        for(int row = 0; row < 5; row++) {
            for(int col = 0; col < 5; col++) {
                result += Board[row,col].Number.ToString("D2");
                if(Board[row,col].IsMarked) {
                    result += "X ";
                } else {
                    result += "  ";
                }
            }
            result += "\n";
        }
        return result;
    }

    public bool MarkCell(int inNumber) {
        for(int row = 0; row < 5; row++) {
            for(int col = 0; col < 5; col++) {
                if(Board[row,col].Number == inNumber) {
                    Board[row,col].IsMarked = true;
                    // TODO: Invoke method to evaluate and update IsBingo status;
                    return true;
                }
            }
        }
        return false;
    }

    public BingoBoard(List<string> input) {
        int row = 0, col = 0;
        foreach(string line in input) {
            string[] terms = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            foreach(string term in terms) {
                BingoCell cell = new BingoCell(int.Parse(term));
                Board[row,col] = cell;
                col++;
            }
            col = 0;
            row++;
        }
        Board[2,2].IsMarked = true;
        IsBingo = false;
    }

    public class BingoCell {
        public int Number { get; }
        public bool IsMarked { get; set; }

        // public BingoCell() : this(1) { }

        public BingoCell(int inNumber) {
            Number = inNumber;
            IsMarked = false;
        }
    }
}