using System;
using System.Collections.Generic;
using System.Diagnostics;

class Transparency
{
    public int[,] Grid { get; private set; }

    public int VisiblePoints { get; private set; }

    private int VirtualMaxRow { get; set; }

    private int VirtualMaxCol { get; set; }

    public Transparency(Instructions Instructions)
    {
        this.VirtualMaxRow= Instructions.MaxX+1;
        this.VirtualMaxCol= Instructions.MaxY+1;
        this.Grid= new int[VirtualMaxRow,VirtualMaxCol];

        foreach(Point dot in Instructions.Dots) { this.Grid[dot.X,dot.Y]= 1; }

        this.VisiblePoints= Instructions.Dots.Count;
    }

    public void Fold(FoldInstruction FoldInstruction)
    {
        Console.WriteLine(FoldInstruction);

        VisiblePoints= 0;
        if(FoldInstruction.Direction == FoldInstruction.Directions.Up)
        {
            // Folding Up
            int maxRow= FoldInstruction.Line;
            int maxCol= VirtualMaxCol;
            for(int row= 0; row < maxRow; row++)
            {
                for(int col= 0; col < maxCol; col++)
                {
                    int otherRow= VirtualMaxRow-row-1;
                    Grid[row,col]+= Grid[otherRow,col];
                    if(Grid[row,col] > 0) { VisiblePoints++; }
                }
            }

            // Resize the grid
            VirtualMaxRow= maxRow;
            VirtualMaxCol= maxCol;
        }
        else
        {   // Folding Left
            int maxRow= VirtualMaxRow;
            int maxCol= FoldInstruction.Line;
            for(int row= 0; row < maxRow; row++)
            {
                for(int col= 0; col < maxCol; col++)
                {
                    int otherCol= VirtualMaxCol-col-1;
                    Grid[row,col]+= Grid[row,otherCol];
                    if(Grid[row,col] > 0) { VisiblePoints++; }
                }
            }

            // Resize the grid
            VirtualMaxRow= maxRow;
            VirtualMaxCol= maxCol;
        }

    }

    public override string ToString()
    {
        string output= null;
        // for(int x=0; x < this.VirtualMaxRow; x++)
        // {
        //     for(int y=0; y < this.VirtualMaxCol; y++)
        //     {
        //         output+= Grid[x,y] == 0 ? '.' : '#';
        //     }
        //     output+= '\n';
        // }
        output+= "Visible points = " + this.VisiblePoints;
        return output;
    }
}

class Instructions
{
    public List<Point> Dots { get; init; }
    public List<FoldInstruction> FoldInstructions { get; init; }

    public int MaxX { get; init; }
    public int MaxY { get; init; }

    public Instructions(string[] Lines)
    {
        Dots= new List<Point>();
        FoldInstructions = new List<FoldInstruction>();

        MaxX= 0;
        MaxY= 0;
        ReadingMode readingMode= ReadingMode.ReadingDots;
        int count= 0;
        foreach(string line in Lines)
        {
            count++;
            Debug.Write(count + " ");
            switch(readingMode)
            {
                case ReadingMode.ReadingDots:
                    if(line != "")
                    {
                        string[] XY= line.Split(',');
                        int X= int.Parse(XY[1]);
                        if(X > MaxX) { MaxX= X; }
                        int Y= int.Parse(XY[0]);
                        if(Y > MaxY) { MaxY= Y; }
                        Point Dot= new Point(X,Y);
                        Dots.Add(Dot);
                    }
                    else
                    {
                        readingMode= ReadingMode.ReadingFoldInstructions;
                    }
                    break;

                case ReadingMode.ReadingFoldInstructions:
                    string[] parts= line.Split("fold along ");
                    string[] parts2= parts[1].Split('=');
                    string Axis= parts2[0];
                    int Amount= int.Parse(parts2[1]);
                    FoldInstruction foldInstruction= new FoldInstruction(Axis, Amount);
                    FoldInstructions.Add(foldInstruction);
                    break;
            }
        }

        this.Dots= Dots;
        this.FoldInstructions= FoldInstructions;
    }

    enum ReadingMode { ReadingDots, ReadingFoldInstructions }
}

class FoldInstruction
{
    public Directions Direction { get; init; }
    public int Line { get; init; }

    public FoldInstruction(string Axis, int Line)
    {
        this.Direction= (Axis == "x") ? Directions.Left: Directions.Up;
        this.Line= Line;
    }

    public override string ToString()
    {
        return ("Folding " + Direction + " at line " + Line);
    }

    public enum Directions { Up, Left }
}