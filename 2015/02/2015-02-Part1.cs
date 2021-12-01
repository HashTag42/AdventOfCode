﻿using System;
using System.IO;

// Puzzle: https://adventofcode.com/2015/day/2

// --- Day 2: I Was Told There Would Be No Math ---
// The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

// Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

// For example:

// A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
// A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
// All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

namespace _02
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine( AddupSquareFeetOfPaper(@".\testInput.txt"));
            Console.WriteLine( AddupSquareFeetOfPaper(@".\input.txt"));
        }

        static int AddupSquareFeetOfPaper(string filePath)
        {
            int answer = 0;
            foreach(var line in File.ReadLines(filePath))
            {
                answer += getSquareFeetOfPaper(line);
            }
            return answer;
        }

        static int getSquareFeetOfPaper(string expression)
        {
            int[] dimensions = splitDimensions(expression);
            int l = dimensions[0];
            int w = dimensions[1];
            int h = dimensions[2];
            int surfaceArea = (2*l*w) + (2*w*h) + (2*h*l);
            int slack = getSlack(l, w, h);
            int result = surfaceArea + slack;
            return result;
        }

        static int[] splitDimensions(string Text)
        {
            string[] terms = Text.Split('x');
            int[] result = new int[terms.Length];
            for (int i = 0; i < terms.Length; i++)
            {
                result[i] = int.Parse(terms[i]);
            }
            return result;
        }

        static int getSlack(int l, int w, int h)
        {
            int[] dimensions = new[] {l, w, h};
            Array.Sort(dimensions);
            int result = dimensions[0] * dimensions[1];
            return result;
        }
    }
}
