using System;
using System.IO;
using System.Diagnostics;

namespace _2021_07
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePart1(@".\inputTest.txt")); //Expect 37
            Console.WriteLine(solvePart1(@".\input.txt")); //Expect 323647
        }

        static int solvePart1(string FilePath) {
            int arraySize= 2000;
            string line= File.ReadAllText(FilePath);
            string[] terms= line.Split(',');
            int[] numbers= new int[arraySize];
            foreach(string s in terms) {
                int value= int.Parse(s);
                numbers[value]++;
            }
            int minimumFuel= int.MaxValue;
            for(int position= 0; position < arraySize; position++) {
                if(numbers[position] > 0) {
                    int fuel= 0;
                    for(int i= 0; i < arraySize; i++) {
                        if(numbers[i] > 0) {
                            int stepFuel= numbers[i] * Math.Abs(position-i);
                            fuel+= stepFuel;
                        }
                    }
                    if(fuel < minimumFuel) {
                        minimumFuel= fuel;
                    }
                }
            }
            return minimumFuel;
        }
    }
}