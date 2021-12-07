using System;
using System.IO;
using System.Diagnostics;

namespace _2021_07
{
    class Program
    {
        static void Main(string[] args)
        {
            bool extra = true;
            Console.WriteLine(solvePuzzle(@".\inputTest.txt")); //Expect 37
            Console.WriteLine(solvePuzzle(@".\input.txt")); //Expect 323647
            Console.WriteLine(solvePuzzle(@".\inputTest.txt", extra)); //Expect 168
            Console.WriteLine(solvePuzzle(@".\input.txt", extra)); //Expect 87640209
        }

        static int solvePuzzle(string FilePath, bool extra = false) {
            int arraySize= 2000;
            string line= File.ReadAllText(FilePath);
            string[] terms= line.Split(',');
            int[] numbers= new int[arraySize];
            foreach(string s in terms) {
                int value= int.Parse(s);
                numbers[value]++;
            }
            int minimumFuel= int.MaxValue;
            for(int target= 0; target < arraySize; target++) {
                int fuel= 0;
                for(int source= 0; source < arraySize; source++) {
                    if(numbers[source] > 0) {
                        int stepFuel= CalculateFuel(numbers[source], source, target, extra);
                        fuel+= stepFuel;
                    }
                }
                if(fuel < minimumFuel) {
                    minimumFuel= fuel;
                }
            }
            return minimumFuel;
        }

        static int CalculateFuel(int Count, int From, int To, bool extra) {
            int fuelCost= 0;
            int distance= Math.Abs(From - To);
            if(extra) {
                for(int i= 0; i <= distance; i++) {
                    fuelCost+= i;
                }
                fuelCost= Count * fuelCost;
            } else {
                fuelCost+= Count * distance;
            }
            return fuelCost;
        }
    }
}