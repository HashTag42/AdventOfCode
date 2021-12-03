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

            Console.WriteLine(solve_2021_03_Part1(FilePath));
        }

        private static int solve_2021_03_Part1(string FilePath) {
            const int rowLength = 5;

            int[,] summary = new int[rowLength,4];

            foreach(string line in File.ReadLines(FilePath)) {
                int x = 0;
                foreach(char c in line) {
                    if('0' == c) {
                        summary[x,0]++;
                    } else {
                        summary[x,1]++;
                    }
                    x++;
                }
            }

            for(int x = 0; x < rowLength; x++) {
                if(summary[x,0] > summary[x,1]) {
                    summary[x,2] = 0;
                    summary[x,3] = 1;
                } else {
                    summary[x,2] = 1;
                    summary[x,3] = 0;
                }
            }

            printMatrix(summary);

            string gammaRateString = "10110";
            string epsilonRateString = "01001";

            BinaryString gammaRate = new BinaryString(gammaRateString);
            BinaryString epsilonRate = new BinaryString(epsilonRateString);

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
