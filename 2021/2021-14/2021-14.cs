using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

// Advent of Code
// --- Day 14: Extended Polymerization ---
// https://adventofcode.com/2021/day/14

namespace _2021_14
{
    class Program
    {
        static void Main(string[] args)
        {
            Polymer polymer = new Polymer(@".\inputTest.txt");
        }
    }

    public class Polymer
    {
        public string PolymerFormula { get; private set; }

        public PolymerInstructions Instructions { get; init; }

        public Polymer(string FilePath)
        {
            this.PolymerFormula = null;
            string[] lines = File.ReadAllLines(FilePath);
            this.Instructions = new PolymerInstructions(lines);

            foreach(PolymerInstructions.PairInsertionRule rule in Instructions.InsertionRules)
            {
                Debug.Print(rule.Pair + " -> " + rule.Element);
            }
        }

        public class PolymerInstructions
        {
            public string Template { get; init; }
            public List<PairInsertionRule> InsertionRules { get; init; }

            public PolymerInstructions(string[] Lines)
            {
                this.Template = Lines[0];
                this.InsertionRules = new List<PairInsertionRule>();

                for(int l = 2; l < Lines.GetLength(0); l++)
                {
                    InsertionRules.Add(new PairInsertionRule(Lines[l]));
                }
            }

            public class PairInsertionRule
            {
                public ElementPair Pair { get; init; }
                public char Element { get; init; }

                public PairInsertionRule(string Line)
                {
                    string[] terms = Line.Split(" -> ");
                    this.Pair = new ElementPair(terms[0].ToCharArray());
                    this.Element = terms[1][0];
                }

                public override string ToString()
                {
                    return (Pair + " -> " + Element);
                }

                public class ElementPair
                {
                    public char First { get; init; }
                    public char Second { get; init; }

                    public ElementPair(char[] Pair)
                    {
                        this.First  = Pair[0];
                        this.Second = Pair[1];
                    }

                    public override string ToString()
                    {
                        return (First.ToString() + Second.ToString());
                    }
                }
            }
        }
    }
}