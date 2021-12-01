using System;
using System.IO;

/* Puzzle: https://adventofcode.com/2015/day/2

--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

--- Part Two ---
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?
*/

namespace _02
{
    class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine(processInputFile(@".\input.txt"));
            Console.WriteLine(processInputFile(@".\inputTest.txt"));
        }

        private static string processInputFile(string FilePath)
        {
            int[] results = processLine(FilePath);
            int totalSquareFeetOfPaper = results[0];
            int totalRibbon = results[1];

            string result = "Processing " + FilePath + " // ";
            result += "Total square feet of paper: " + totalSquareFeetOfPaper + " // ";
            result += "Total ribbon needed: " + totalRibbon;

            return result;
        }

        private static int[] processLine(string FilePath)
        {
            int totalPaper = 0;
            int totalRibbon = 0;

            foreach(string line in File.ReadLines(FilePath))
            {
                int[] dimensions = getDimensions(line);
                totalPaper += getSquareFeetOfPaper(dimensions);
                totalRibbon += getFeetOfRibbon(dimensions);
            }

            int[] result = new int[] { totalPaper, totalRibbon };
            return result;
        }

        private static int[] getDimensions(string Text)
        {
            string[] terms = Text.Split('x');

            int[] dimensions = new int[terms.Length];

            for (int i = 0; i < terms.Length; i++)
            {
                dimensions[i] = int.Parse(terms[i]);
            }

            Array.Sort(dimensions);

            return dimensions;
        }

        private static int getSquareFeetOfPaper(int[] Dimensions)
        {
            int l = Dimensions[0];
            int w = Dimensions[1];
            int h = Dimensions[2];

            int surfaceArea = (2*l*w) + (2*w*h) + (2*h*l);
            int slack = getSlack(Dimensions);

            int squareFeetOfPaper = surfaceArea + slack;
            return squareFeetOfPaper;
        }

        private static int getFeetOfRibbon(int[] Dimensions)
        {
            Array.Sort(Dimensions);
            int ribbon = Dimensions[0]*2 + Dimensions[1]*2;
            int bow = Dimensions[0]*Dimensions[1]*Dimensions[2];
            int feetOfRibbon = ribbon + bow;
            return feetOfRibbon;
        }

        private static int getSlack(int[] Dimensions)
        {
            Array.Sort(Dimensions);
            int result = Dimensions[0] * Dimensions[1];
            return result;
        }
    }
}
