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

            part1Entries.Add(new PuzzleEntry("abcdef", 609043));
            part1Entries.Add(new PuzzleEntry("pqrstuv", 1048970));
            part1Entries.Add(new PuzzleEntry("yzbqklnj", 282749));

            foreach(PuzzleEntry entry in part1Entries) {
                Console.WriteLine(entry.result(solvePart1(entry.Input)));
            }
        }

        static int solvePart1(string input) {
            string md5 = null;
            int i = -1;
            do{
                i++;
                string number = input + i.ToString();
                md5 = calculateMD5(number);
            } while (!(md5.Substring(0,5) == "00000"));

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
