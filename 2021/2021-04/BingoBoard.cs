using System;
using System.Collections.Generic;

public class BingoBoard {

    private const int boardSize = 5;

    private BingoCell[,] Board = new BingoCell[boardSize,boardSize];

    private bool _IsBingo { get; set;}
    public bool IsBingo { get => _IsBingo; }

    /// <summary>Returns the sum of the values for all unmarked cells in the board.</summary>
    public int SumUnmarkedCells() {
        int sum = 0;
        for(int row = 0; row < boardSize; row++) {
            for(int col = 0; col <boardSize; col++) {
                if(!Board[row,col].IsMarked) {
                    sum += Board[row,col].Number;
                }
            }
        }
        return sum;
    }

    public override string ToString()
    {   string result = null;
        for(int row = 0; row < boardSize; row++) {
            for(int col = 0; col < boardSize; col++) {
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
        for(int row = 0; row < boardSize; row++) {
            for(int col = 0; col < boardSize; col++) {
                if(Board[row,col].Number == inNumber) {
                    Board[row,col].IsMarked = true;
                    if(EvaluateIfIsBingo()) {
                        _IsBingo = true;
                    }
                    return true;
                }
            }
        }
        return false;
    }

    private bool EvaluateIfIsBingo() {
        bool IsBingo = false;

        for(int row = 0; row < boardSize; row++) {
            for(int col = 0; col < boardSize; col++) {
                if(!Board[row,col].IsMarked) {
                    break;
                }
                if(col == boardSize-1) {
                    return true;
                }
            }
        }

        for(int col = 0; col < boardSize; col++) {
            for(int row = 0; row < boardSize; row++) {
                if(!Board[row,col].IsMarked) {
                    break;
                }
                if(row == boardSize-1) {
                    return true;
                }
            }
        }

        return IsBingo;
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
        _IsBingo = false;
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