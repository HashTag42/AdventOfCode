using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

// Puzzle: https://adventofcode.com/2021/day/8

namespace _2021_08
{
    class Program
    {
        const int lowerA= 97;
        const int upperA= 65;
        static Dictionary<char,char> Decoder= new Dictionary<char, char>();

        static void Main(string[] args)
        {
            // Console.WriteLine(SolvePuzzle(@".\inputTest1.txt"));
            // Console.WriteLine(SolvePuzzle(@".\inputTest2.txt"));
            Console.WriteLine(SolvePuzzle(@".\input.txt"));
        }

        static string SolvePuzzle(string FilePath) {
            string[] input= File.ReadAllLines(FilePath);
            string message= null;
            message+= "Using input: " + FilePath + "\n";
            // message+= "\t Part 1 answer: " + SolvePart1(input) + "\n";
            message+= "\t Part 2 answer: " + SolvePart2(input) + "\n";
            return message;
        }

        static int SolvePart1(string[] Input) {
            List<int> filter= new List<int> {2, 4, 3, 7}; // Filtering bythe string.Length of each easy digit.
            int countEasyDigits= 0;
            foreach(string line in Input) {
                string[] segments= line.Split('|');
                string[] encodedSignals= segments[1].Split(' ', StringSplitOptions.RemoveEmptyEntries);
                foreach(string signal in encodedSignals) {
                    if((filter.IndexOf(signal.Length)) != -1) {
                        countEasyDigits++;
                    }
                }
            }
            return countEasyDigits;
        }

        static string SolvePart2(string[] Input)
        {
            uint answer= 0;
            foreach(string line in Input)
            {
                // Parse the encoded Signals and encoded digits
                string[] encodedSignals= null;
                string[] encodedValues= null;

                string[] segments= line.Split(" | ");
                Debug.WriteLine(segments[0]);
                encodedSignals= segments[0].Split(' ', StringSplitOptions.RemoveEmptyEntries);
                encodedValues= segments[1].Split(' ', StringSplitOptions.RemoveEmptyEntries);

                #if DEBUG
                    foreach(string s in encodedSignals)
                    {
                        Debug.Write(s + " ");
                    }
                    Debug.Write("\n");
                #endif

                // Initialize the Decoder dictionary.
                Decoder.Clear();
                for(int i= 0; i < 7; i++)
                {
                    // Add to the decoder the keys a-z
                    Decoder.Add((char)(i+lowerA),(char)0);
                }

                // Decode some letters based on their frequency in the encoded signals

                // Count each letter on all encoded signals
                int[] letterCount= new int[7];
                foreach(string s in encodedSignals)
                {
                    foreach(char c in s)
                    {
                        letterCount[c-lowerA]++;
                    }
                }

                // Assign the decoded letter values to the dictionary
                for(int i= 0; i < letterCount.GetLength(0); i++)
                {
                    switch(letterCount[i])
                    {
                        case 4: Decoder[(char)(i + lowerA)] = 'E'; break;
                        case 6: Decoder[(char)(i + lowerA)] = 'B'; break;
                        case 9: Decoder[(char)(i + lowerA)] = 'F'; break;
                    }
                }

                // Decode all other letters based on the specific digits they are part of.

                // Find the signals for all the known digits.
                string one=   null;
                string four=  null;
                string seven= null;
                string eight= null;
                foreach(string s in encodedSignals)
                {
                    switch(s.Length)
                    {
                        case 2: one=   s; break;
                        case 3: seven= s; break;
                        case 4: four=  s; break;
                        case 7: eight= s; break;
                    }
                }

                // On the signal for one, find the wire for C.
                foreach(char c in one)
                {
                    if(Decoder[c] == (char)0)
                    {
                        Decoder[c]= 'C';
                        break;
                    }
                }

                // On the signal for four, find the wire for D.
                foreach(char c in four)
                {
                    if(Decoder[c] == (char)0)
                    {
                        Decoder[c]= 'D';
                        break;
                    }
                }

                // On the signal for seven, find the wire for A.
                foreach(char c in seven)
                {
                    if(Decoder[c] == (char)0)
                    {
                        Decoder[c]= 'A';
                        break;
                    }
                }

                // On the signal for eight, find the wire for G.
                foreach(char c in eight)
                {
                    if(Decoder[c] == (char)0)
                    {
                        Decoder[c]= 'G';
                        break;
                    }
                }

                // Decode all values from the 2nd portion of the line.
                string[] decodedValues= new string[encodedValues.GetLength(0)];
                for(int s= 0; s < encodedValues.GetLength(0); s++)
                {
                    decodedValues[s]= DecodeValue(encodedValues[s]);
                }

                // Get the digits
                string digits= null;
                foreach(string dv in decodedValues)
                {
                    digits+= GetDigitFromString(dv);
                }
                answer+= uint.Parse(digits);
            }
            return answer.ToString();
        }

        static string DecodeValue(string EncodedValue)
        {
            string decodedSignal= null;
            foreach(char c in EncodedValue)
            {
                decodedSignal+= Decoder[c];
            }
            return(decodedSignal);
        }

        static char GetDigitFromString(string Input) {
            char digit= (char) 0;
            string sorted= SortString(Input);
            switch(sorted.ToUpper()) {
                case "ABCEFG"  : digit= '0'; break;
                case "CF"      : digit= '1'; break;
                case "ACDEG"   : digit= '2'; break;
                case "ACDFG"   : digit= '3'; break;
                case "BCDF"    : digit= '4'; break;
                case "ABDFG"   : digit= '5'; break;
                case "ABDEFG"  : digit= '6'; break;
                case "ACF"     : digit= '7'; break;
                case "ABCDEFG" : digit= '8'; break;
                case "ABCDFG"  : digit= '9'; break;
                default        : digit= 'X'; break;   // Unexected value.
            }
            return digit;
        }

        static string SortString(string Input) {
            char[] characters= Input.ToCharArray();
            Array.Sort(characters);
            return new string(characters);
        }
    }
}