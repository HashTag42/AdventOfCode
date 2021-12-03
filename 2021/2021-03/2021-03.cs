using System;
using System.IO;

namespace _2021_03
{
    class Program
    {
        static void Main(string[] args)
        {
            string FilePath = @".\inputTest.txt";
            // string FilePath = @".\input.txt";
            // input = File.ReadAllText(FilePath);

            Console.WriteLine(solve_2021_03_Part1(FilePath));
        }

        private static int solve_2021_03_Part1(string FilePath) {
            int[,] matrix = new int[5,12];
            int lineCount = 0;
            int charCount = 0;
            foreach(string line in File.ReadLines(FilePath)) {
                charCount = 0;
                foreach(char c in line) {
                    matrix[charCount,lineCount] = int.Parse(c.ToString());
                    charCount++;
                }
                lineCount++;
            }
            // printMatrix(matrix);

            int[,] summary = new int[matrix.GetLength(0),4];
            int maxX = matrix.GetLength(0);
            int maxY = matrix.GetLength(1);
            for(int y = 0; y < maxY; y++) {
                for(int x = 0; x < maxX; x++) {
                    if(0 == matrix[x,y]) {
                        summary[x,0]++;
                    } else {
                        summary[x,1]++;
                    }
                }
            }
            for(int x = 0; x < maxX; x++) {
                int countOfZeros = summary[x,0];
                int countOfOnes  = summary[x,1];
                if(countOfZeros > countOfOnes) {
                    summary[x,2] = 0;
                    summary[x,3] = 1;

                } else {
                    summary[x,2] = 1;
                    summary[x,3] = 0;
                }
            }
            // printMatrix(summary);

            BinaryString gammaRate = new BinaryString("10110");
            BinaryString epsilonRate = new BinaryString("01001");

            int powerConsumption = gammaRate.ToInt() * epsilonRate.ToInt();

            return powerConsumption;
        }


        private static void printMatrix(int[,] matrix) {
            int maxX = matrix.GetLength(0);
            int maxY = matrix.GetLength(1);
            for(int y = 0; y < maxY; y++) {
                for(int x = 0; x < maxX; x++) {
                    Console.Write(matrix[x,y]);
                }
                Console.Write("\n");
            }
        }
    }
}
