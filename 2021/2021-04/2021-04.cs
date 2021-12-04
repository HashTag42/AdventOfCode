using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

namespace _2021_04 {
    class Program {
        static void Main(string[] args) {

            Console.WriteLine(SolvePuzzleUsingFile(@".\inputTest.txt"));
            Console.WriteLine("The expected results were: 4512 and 1924\n");

            Console.WriteLine(SolvePuzzleUsingFile(@".\input.txt"));
            Console.WriteLine("The expected results were: 31424 and 23042\n");
        }

        private static string SolvePuzzleUsingFile(string FilePath) {
            List<string> input = new List<string>();
            foreach(string line in File.ReadAllLines(FilePath)) {
                input.Add(line);
            }
            int[] answers = solvePuzzle(input);
            string result  = "Solving puzzle using file: " + FilePath;
                   result += "\n\t Answer to Part 1: " + answers[0];
                   result += "\n\t Answer to Part 2: " + answers[1];
            return result;
        }

        private static int[] solvePuzzle(List<string> input) {
            List<BingoBoard> boards = LoadBoards(input);

            // Draw numbers to determine the winning board
            bool firstWinnerFound = false;
            int part1score = -1;
            int part2score = -1;
            int numberOfWinners = 0;

            string numbersLine = input[0];
            string[] numbers = numbersLine.Split(',');
            foreach(string number in numbers) {
                int num = int.Parse(number);
                foreach(BingoBoard board in boards) {
                    if(!board.IsBingo) {
                        board.MarkCell(num);
                        if(board.IsBingo) {
                            numberOfWinners++;
                            if(!firstWinnerFound) {
                                firstWinnerFound = true;
                                part1score = board.SumUnmarkedCells() * num;
                            }
                            if(numberOfWinners == boards.Count) {
                                part2score = board.SumUnmarkedCells() * num;
                            }
                        }
                    }
                }
            }

            int[] result = { part1score, part2score };
            return result;
        }

        private static List<BingoBoard> LoadBoards(List<string> input) {
            List<BingoBoard> boards = new List<BingoBoard>();
            for(int i=2 ; i<input.Count; i+=6) {
                int firstLineIndex = i;
                int lineCount = 5;
                List<string> boardInput = input.GetRange(firstLineIndex, lineCount);
                BingoBoard newBoard = new BingoBoard(boardInput);
                boards.Add(newBoard);
            }
            return boards;
        }

    }
}
