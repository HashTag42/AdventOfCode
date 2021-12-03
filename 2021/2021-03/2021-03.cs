using System;
using System.IO;

namespace _2021_03
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePuzzle_2021_03_Part1(@".\inputTest.txt", 5)); // Expected result: 198
            Console.WriteLine(solvePuzzle_2021_03_Part1(@".\input.txt", 12)); // Expected result: 3374136
        }

        private static int solvePuzzle_2021_03_Part1(string FilePath, int rowLength) {
            int[,] summary = new int[rowLength,2];
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

            string gammaRateString = null;
            string epsilonRateString = null;
            for(int x = 0; x < rowLength; x++) {
                if(summary[x,0] > summary[x,1]) {
                    gammaRateString += '0';
                    epsilonRateString += '1';
                } else {
                    gammaRateString += '1';
                    epsilonRateString += '0';
                }
            }

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
