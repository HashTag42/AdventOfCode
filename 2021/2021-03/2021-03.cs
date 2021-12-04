using System;
using System.IO;
using System.Collections.Generic;

namespace _2021_03
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine(solvePart1(@".\inputTest.txt", 5)); // Expected result: 198
            Console.WriteLine(solvePart1(@".\input.txt", 12)); // Expected result: 3374136

            // Console.WriteLine(solvePart2(@".\inputTest.txt", 5)); // Expected result:
            Console.WriteLine(solvePart2(@".\input.txt", 12)); // Expected result: 4432698
        }

        private static int solvePart2(string FilePath, int RowLength) {
            // int[,] summary = getSummary(FilePath, RowLength);
            // printMatrix(summary);

            List<string> o2GeneratorRatingList = new List<string>();
            List<string> co2ScrubberRatingList = new List<string>();
            foreach(string line in File.ReadLines(FilePath)) {
                o2GeneratorRatingList.Add(line);
                co2ScrubberRatingList.Add(line);
            }

            int col;

            // printList(o2GeneratorRatingList);
            col = 0;
            do {
                int countZeros = 0;
                int countOnes = 0;
                foreach(string line in o2GeneratorRatingList) {
                    if('0' == line[col]) {
                        countZeros++;
                    } else {
                        countOnes++;
                    }
                }

                char filter;
                if(countZeros > countOnes) {
                    filter = '0';
                } else {
                    filter = '1';
                }

                o2GeneratorRatingList.RemoveAll(x => !(x[col] == filter));
                // printList(o2GeneratorRatingList);
                col++;
            } while(o2GeneratorRatingList.Count > 1);

            BinaryString o2GeneratorRatingStr = new BinaryString(o2GeneratorRatingList[0]);

            // printList(co2ScrubberRatingList);
            col = 0;
            do {
                int countZeros = 0;
                int countOnes = 0;
                foreach(string line in co2ScrubberRatingList) {
                    if('0' == line[col]) {
                        countZeros++;
                    } else {
                        countOnes++;
                    }
                }

                char filter;
                if(countZeros > countOnes) {
                    filter = '1';
                } else {
                    filter = '0';
                }

                co2ScrubberRatingList.RemoveAll(x => !(x[col] == filter));
                // printList(co2ScrubberRatingList);
                col++;
            } while(co2ScrubberRatingList.Count > 1);

            BinaryString co2ScrubberRatingStr = new BinaryString(co2ScrubberRatingList[0]);

            int o2GeneratorRating = o2GeneratorRatingStr.ToInt();
            int co2ScrubberRating = co2ScrubberRatingStr.ToInt();
            int lifeSupportRating = o2GeneratorRating * co2ScrubberRating;
            return lifeSupportRating;
        }

        private static void printList(List<string> list) {
            Console.Write("[{0}]: ", list.Count);
            foreach(string line in list) {
                Console.Write(line + " ");
            }
            Console.Write('\n');
        }

        private static int solvePart1(string FilePath, int rowLength) {
            int[,] summary = getSummary(FilePath, rowLength);

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

            printMatrix(summary);

            BinaryString gammaRate = new BinaryString(gammaRateString);
            BinaryString epsilonRate = new BinaryString(epsilonRateString);

            int powerConsumption = gammaRate.ToInt() * epsilonRate.ToInt();
            return powerConsumption;
        }

        private static int[,] getSummary(string FilePath, int rowLength) {
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
            return summary;
        }

        private static void printMatrix(int[,] matrix) {
            int maxX = matrix.GetLength(0);
            int maxY = matrix.GetLength(1);
            for(int y = 0; y < maxY; y++) {
                for(int x = 0; x < maxX; x++) {
                    Console.Write(matrix[x,y]);
                    Console.Write(' ');
                }
                Console.Write("\n");
            }
        }
    }
}
