using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

// Puzzle: https://adventofcode.com/2021/day/9

namespace _2021_09
{
    class Program
    {
        static void Main(string[] args)
        {
            SolvePuzzle(@".\inputTest.txt");
            SolvePuzzle(@".\input.txt");
        }

        static void SolvePuzzle(string FilePath)
        {
            Console.WriteLine("Using: " + FilePath);
            string[] lines= File.ReadAllLines(FilePath);

            Board board= new Board(lines);
            Debug.WriteLine(board);

            //  --- Part One ---
            #if DEBUG
                Debug.Write("Lowpoints: ");
                foreach(Point lowPoint in board.LowPoints)
                {
                    Debug.Write(lowPoint + " ");
                }
                Debug.Write('\n');
            #endif
            Console.WriteLine("Answer to Part 1: " + board.SumRiskLevels.ToString());

            //  --- Part Two ---
            int productOfThreeLargestBasins= 1;
            List<int> basinSizes= board.BasinsSizes;
            basinSizes.Sort();
            basinSizes.Reverse();
            if(basinSizes.Count >= 3)
            {
                for(int i= 0; i < 3; i++)
                {
                    productOfThreeLargestBasins*= basinSizes[i];
                }
            }

            Console.WriteLine("Answer to Part 2: " + productOfThreeLargestBasins.ToString());
        }

        class Basin
        {
            public int Size=> Points.Count;

            public List<Point> Points { get; set; }

            public Basin() { }
        }

        class Board
        {
            public int[,] Grid { get; init; }
            public List<Point>  LowPoints { get; init; }
            public int SumRiskLevels { get; init; }
            public List<Basin>  Basins { get; init; }
            public List<int>    BasinsSizes { get; init; }

            public Board(string[] InputLines)
            {
                this.Grid= this.BuildGrid(InputLines);

                this.LowPoints= this.FindAllLowPoints();
                this.SumRiskLevels= this.CalculateRiskLevels();
                this.Basins= this.FindAllBasins();

                // Build the list of Basins Sizes
                this.BasinsSizes= new List<int>();
                foreach(Basin b in this.Basins)
                {
                    BasinsSizes.Add(b.Size);
                }
            }

            public override string ToString()
            {
                string output= null;
                for(int row= 0; row < Grid.GetLength(0); row++)
                {
                    for(int col= 0; col < Grid.GetLength(1); col++)
                    {
                        int cellValue= Grid[row,col];
                        output+= cellValue == 9 ? "." : cellValue;
                        output+= ' ';
                    }
                    output+= '\n';
                }
                return output;
            }

            private int[,] BuildGrid(string[] InputLines)
            {
                // Parse the input to build the grid
                int colCount= InputLines[0].Length;
                int rowCount= InputLines.Length;
                int[,] myGrid= new int[rowCount,colCount];
                for(int row= 0; row < rowCount; row++)
                {
                    for(int col= 0; col < colCount; col++)
                    {
                        myGrid[row,col]= int.Parse(InputLines[row][col].ToString());
                    }
                }
                return myGrid;
            }

            private List<Point> FindAllLowPoints()
            {
                List<Point> lowPoints = new List<Point>();
                for(int row= 0; row < this.Grid.GetLength(0); row++)
                {
                    for(int col= 0; col < this.Grid.GetLength(1); col++)
                    {
                        int cellValue= this.Grid[row,col];
                        int N, S, E, W;
                        try { N= this.Grid[row-1, col  ]; } catch(IndexOutOfRangeException) { N= int.MaxValue; }
                        try { S= this.Grid[row+1, col  ]; } catch(IndexOutOfRangeException) { S= int.MaxValue; }
                        try { E= this.Grid[row  , col+1]; } catch(IndexOutOfRangeException) { E= int.MaxValue; }
                        try { W= this.Grid[row  , col-1]; } catch(IndexOutOfRangeException) { W= int.MaxValue; }
                        if((cellValue < N) && (cellValue < S) && (cellValue < E) && (cellValue < W))
                        {
                            lowPoints.Add(new Point(row,col));
                        }
                    }
                }
                return lowPoints;
            }

            private int CalculateRiskLevels()
            {
                int sumRiskLevels= 0;
                foreach(Point lowpoint in this.LowPoints)
                {
                    sumRiskLevels+= Grid[lowpoint.X,lowpoint.Y] + 1;
                }
                return sumRiskLevels;
            }

            private bool[,] Visited { get; set; }

            private List<Basin> FindAllBasins()
            {
                List<Basin> outBasinList= new List<Basin>();

                this.Visited= new bool[this.Grid.GetLength(0),this.Grid.GetLength(1)];

                foreach(Point lowPoint in this.LowPoints)
                {
                    Basin basin= new Basin();
                    basin.Points= new List<Point>();
                    basin.Points.Add(lowPoint);
                    Visited[lowPoint.X,lowPoint.Y]= true;
                    AddNeighbors(lowPoint, basin);
                    outBasinList.Add(basin);
                }

                return outBasinList;
            }

            private void AddNeighbors(Point Point, Basin Basin)
            {
                int[,] offsets= { {-1,0}, {0,-1}, {0,+1}, {+1,0} };
                for(int i=0; i < offsets.GetLength(0); i++)
                {
                    int row= Point.X + offsets[i,0];
                    int col= Point.Y + offsets[i,1];
                    try
                    {
                        if(this.Grid[row,col] != 9 && !Visited[row,col])
                        {
                            Point newPoint= new Point(row,col);
                            Basin.Points.Add(newPoint);
                            Visited[row,col]= true;
                            AddNeighbors(newPoint, Basin);
                        }
                    }
                    catch(IndexOutOfRangeException) { }
                }
            }

        } // class Board

    } // class Program

} // Namespace
