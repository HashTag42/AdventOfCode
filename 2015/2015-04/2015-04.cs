using System;
using System.Text;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Diagnostics;

namespace _2015_04
{

    class Program
    {
        static void Main(string[] args)
        {
            List<PuzzleEntry> part1Entries = new List<PuzzleEntry>();

            part1Entries.Add(new PuzzleEntry("abcdef", 5, 609043));
            part1Entries.Add(new PuzzleEntry("pqrstuv", 5, 1048970));
            part1Entries.Add(new PuzzleEntry("yzbqklnj", 5, 282749));
            part1Entries.Add(new PuzzleEntry("yzbqklnj", 6, 9962624));

            foreach(PuzzleEntry entry in part1Entries) {
                Console.WriteLine(entry.result(solvePuzzle(entry.Input, entry.NumberOfZeros)));
            }
        }

        static int solvePuzzle(string Input, int NumberOfZeros) {
            string md5 = null;
            string prefix = null;
            for(int j = 0; j < NumberOfZeros; j ++) {
                prefix += '0';
            }
            int i = -1;
            do{
                i++;
                string number = Input + i.ToString();
                md5 = calculateMD5(number);
            } while (!(md5.Substring(0,NumberOfZeros) == prefix));

            return i;
        }

        static string calculateMD5(string input) {
            System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create();

            byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
            byte[] hashBytes = md5.ComputeHash(inputBytes);

            // Convert the byte array to hexadecimal string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hashBytes.Length; i++)
            {
                sb.Append(hashBytes[i].ToString("X2"));
            }
            return sb.ToString();
        }
    }
}
