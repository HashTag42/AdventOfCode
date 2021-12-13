using System;
using System.IO;                    // File class
using System.Diagnostics;           // Debug class
using System.Collections.Generic;   // Queue<T> class

#pragma warning restore format

// Advent of Code
// --- Day 11: Dumbo Octopus ---
// https://adventofcode.com/2021/day/11

namespace _2021_11
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine(SolvePuzzle(@".\inputTest0.txt", 2)); // Expected: 9
            // Console.WriteLine(SolvePuzzle(@".\inputTest.txt", 100)); // Expected: 1656
            Console.WriteLine(SolvePuzzle(@".\input.txt", 100));     // Expected: 1632
        }

        static string SolvePuzzle(string FilePath, int Steps)
        {
            string[] lines= File.ReadAllLines(FilePath);

            string message= null;
            message+= "Using file: " + FilePath + "\n";
            message+= "\t Part 1 answer: " + SolvePart1(lines, Steps) + "\n";
            message+= "\t Part 2 answer: " + SolvePart2(lines, Steps) + "\n";

            return message;
        }

        static string SolvePart1(string[] Lines, int Steps)
        {
            DumboOctopusCell[,] board = BuildOctopiBoard(Lines);
            Console.WriteLine("Before any steps:");
            Console.WriteLine(BoardToString(board));

            Queue<DumboOctopusCell> queue= new Queue<DumboOctopusCell>();

            uint flashesCount= 0;
            for(int step= 1; step <= Steps; step++)
            {
                // Step every octopus
                foreach(DumboOctopusCell dumbo in board)
                {
                    dumbo.Step();
                    if(dumbo.IsFlashing)
                    {
                        flashesCount++;
                        queue.Enqueue(dumbo);
                    }
                }

                Debug.WriteLine("Step {0}: After stepping every octopus:", step);
                Debug.WriteLine(BoardToString(board));

                // Process every flashing octopus
                while(queue.Count > 0)
                {
                    DumboOctopusCell flashingDumbo= queue.Peek();
                    int[,] offsets= { {-1,-1}, {-1,0}, {-1,+1}, {0,-1}, {0,+1}, {+1,-1}, {+1,0}, {+1,+1} };
                    for(int i = 0; i < offsets.GetLength(0); i++)
                    {
                        int row= flashingDumbo.Row+offsets[i,0];
                        int col= flashingDumbo.Col+offsets[i,1];
                        try
                        {
                            DumboOctopusCell targetDumbo= board[row,col];
                            if(!targetDumbo.IsFlashing)
                            {
                                targetDumbo.Step();
                                if(targetDumbo.IsFlashing)
                                {
                                    flashesCount++;
                                    queue.Enqueue(targetDumbo);
                                }
                            }
                        }
                        catch(IndexOutOfRangeException) { }
                    }
                    Debug.WriteLine("Step {0}: After flashing {1},{2}", step, flashingDumbo.Row, flashingDumbo.Col);
                    Debug.WriteLine(BoardToString(board));
                    queue.Dequeue();
                }

                foreach(DumboOctopusCell dumbo in board) { dumbo.StopFlashing(); }

                Console.WriteLine("After step " + step + ":");
                Console.WriteLine(BoardToString(board));
            }

            return flashesCount.ToString();
        }

        static DumboOctopusCell[,] BuildOctopiBoard(string[] Input)
        {
            int colCount= Input[0].Length;
            int rowCount= Input.Length;

            DumboOctopusCell[,] board= new DumboOctopusCell[rowCount,colCount];

            for(int row= 0; row < rowCount; row++)
            {
                for(int col= 0; col < colCount; col++)
                {
                    int energy= int.Parse(Input[row][col].ToString());
                    board[row,col]= new DumboOctopusCell(row, col, energy);
                }
            }

            return board;
        }

        static string BoardToString(DumboOctopusCell[,] Board)
        {
            string output= null;
            for(int row= 0; row < Board.GetLength(0); row++)
            {
                for(int col= 0; col < Board.GetLength(1); col++)
                {
                    output+= Board[row,col].ToString();
                }
                output+= '\n';
            }
            return output;
        }

        static string QueueToString(Queue<DumboOctopusCell> Queue)
        {
            string output= null;
            foreach(DumboOctopusCell dumbo in Queue)
            {
                output+= "(" + dumbo.Row + "," + dumbo.Col + ") ";
            }
            return output;
        }

        static string SolvePart2(string[] Lines, int Steps)
        {
            string result= "Answer 2";
            return result;
        }
    }
}
