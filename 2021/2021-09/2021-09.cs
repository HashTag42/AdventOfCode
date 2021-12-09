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
            Console.WriteLine(SolvePuzzle(@".\inputTest.txt")); // Expected:  15
            Console.WriteLine(SolvePuzzle(@".\input.txt"));     // Expected: 594
        }

        static string SolvePuzzle(string FilePath)
        {
            string[] input= File.ReadAllLines(FilePath);

            string message= null;
            message+= "Using file: " + FilePath + "\n";
            message+= "\t Part 1 answer: " + SolvePart1(input) + "\n";
            message+= "\t Part 2 answer: " + SolvePart2(input) + "\n";

            return message;
        }

        static string SolvePart1(string[] Input)
        {
            int[,] board= BuildBoard(Input);
            Debug.WriteLine(BoardToString(board));

            int sumOfAllLowPoints = 0;

            for(int row=0; row < board.GetLength(0); row++)
            {
                for(int col=0; col < board.GetLength(1); col++)
                {
                    if(IsNumberTheLowestAmonstNeighbors(board, row, col))
                    {
                        sumOfAllLowPoints+= board[row,col] + 1;
                    }
                }
            }

            return sumOfAllLowPoints.ToString();
        }

        static bool IsNumberTheLowestAmonstNeighbors(int[,] board, int row, int col)
        {
            bool result= false;

            int number= board[row,col];
            int N, S, E, W;
            try { N= board[row-1, col  ]; } catch(IndexOutOfRangeException) { N= int.MaxValue; }
            try { S= board[row+1, col  ]; } catch(IndexOutOfRangeException) { S= int.MaxValue; }
            try { E= board[row  , col+1]; } catch(IndexOutOfRangeException) { E= int.MaxValue; }
            try { W= board[row  , col-1]; } catch(IndexOutOfRangeException) { W= int.MaxValue; }

            if((number < N) && (number < S) && (number < E) && (number < W)) {
                result= true;
            }

            return result;
        }

        static int[,] BuildBoard(string[] Input)
        {
            int colCount= Input[0].Length;
            int rowCount= Input.Length;

            int[,] board= new int[rowCount,colCount];

            for(int row= 0; row < rowCount; row++)
            {
                for(int col= 0; col < colCount; col++)
                {
                    board[row,col]= int.Parse(Input[row][col].ToString());
                }
            }

            return board;
        }

        static string BoardToString(int[,] Board)
        {
            string result = null;
            for(int row= 0; row < Board.GetLength(0); row++)
            {
                for(int col= 0; col < Board.GetLength(1); col++)
                {
                    result+= Board[row,col];
                }
                result+= '\n';
            }
            return result;
        }

        static string SolvePart2(string[] Input)
        {
            string result= "Answer 2";
            return result;
        }
    }
}
