using System.IO;    // File

class Board
{
    public int[,] Grid { get; set; }

    public int RowLength { get; init; }
    public int ColLength { get; init; }

    public Board(string[] Lines)
    {
        RowLength= Lines.Length;
        ColLength= Lines[0].Length;

        Grid= new int[RowLength,ColLength];

        for(int row= 0; row < RowLength; row++)
        {
            for(int col= 0; col < ColLength; col++)
            {
                Grid[row,col]= int.Parse(Lines[row][col].ToString());
            }
        }
    }

    public override string ToString()
    {
        string result = null;
        for(int row= 0; row < Grid.GetLength(0); row++)
        {
            for(int col= 0; col < Grid.GetLength(1); col++)
            {
                result+= Grid[row,col];
            }
            result+= '\n';
        }
        return result;
    }
}