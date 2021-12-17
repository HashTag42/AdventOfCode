using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

public class Polymer
{
    public List<char> Formula { get; private set; }

    public PolymerInstructions Instructions { get; init; }

    public Polymer(string FilePath, int Steps)
    {
        Formula = new List<char>();
        Instructions = new PolymerInstructions(File.ReadAllLines(FilePath));
        Formula = Instructions.Template;
        Console.WriteLine("Template: {0}", this);
        for(int step = 1; step <= Steps; step++)
        {
            Step();
            // Console.WriteLine("After step {0}: {1}", step, this);
        }
    }

    public void Step()
    {
        int index  = 0;
        while(index < (Formula.Count-1))
        {
            int offset = 1;
            ElementPair currentPair = new ElementPair(Formula[index],Formula[index+1]);
            // Debug.WriteLine("current pair: " + currentPair);

            foreach(PairInsertionRule rule in Instructions.InsertionRules)
            {
                // Debug.WriteLine(rule);
                if(currentPair == rule.Pair)
                {
                    // Debug.WriteLine("Eureka!");
                    Formula.Insert(index+1, rule.Element);
                    offset += 1;
                    break;
                }
            }
            index += offset;
        }
    }

    public int MostCommonMinusLeastCommon()
    {
        int result = 0;
        const int uppercaseA = 65;

        int[] charCounts = new int[26];

        foreach(char c in Formula)
        {
            charCounts[c-uppercaseA]++;
        }

        Array.Sort(charCounts);
        Array.Reverse(charCounts);

        int most = charCounts[0];
        int min = 0;
        for(int i = 0; i < charCounts.GetLength(0); i++)
        {
            if(0 != charCounts[i])
            {
                min = charCounts[i];
            }
        }
        result = most - min;

        return result;
    }

    public override string ToString()
    {
        string output = null;
        foreach(char c in Formula) { output+= c; }
        return output;
    }
}

public class PolymerInstructions
{
    public List<char> Template { get; init; }
    public List<PairInsertionRule> InsertionRules { get; init; }

    public int Count => this.InsertionRules.Count;

    public PolymerInstructions(string[] Lines)
    {
        Template = new List<char>(Lines[0]);

        InsertionRules = new List<PairInsertionRule>();

        for(int l = 2; l < Lines.GetLength(0); l++)
        {
            InsertionRules.Add(new PairInsertionRule(Lines[l]));
        }
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
}

public class ElementPair : IEquatable<ElementPair>
{
    public char First { get; init; }
    public char Second { get; init; }

    public ElementPair(char[] Pair)
    {
        this.First  = Pair[0];
        this.Second = Pair[1];
    }

    public ElementPair(string Pair)
    {
        this.First  = Pair[0];
        this.Second = Pair[1];
    }

    public ElementPair(char First, char Second)
    {
        this.First  = First;
        this.Second = Second;
    }

    public bool Equals(ElementPair Other)
    {
        bool areEquals = false;
        if(null != Other)
        {
            if( this.First  == Other.First
            &&  this.Second == Other.Second)
            {
                areEquals = true;
            }
        }
        return areEquals;
    }

    public override bool Equals(object obj)
    {
        bool areEquals = false;
        if(null != obj)
        {
            ElementPair pair = obj as ElementPair;
            if(null != pair)
            {
                areEquals = Equals(pair);
            }
        }
        return areEquals;
    }

    public static bool operator == (ElementPair pair1, ElementPair pair2)
    {
        bool result = false;

        if(null == (object)pair1 || null == (object)pair2)
        {
            result = object.Equals(pair1, pair2);
        }
        else
        {
            result = pair1.Equals(pair2);
        }

        return result;
    }

    public static bool operator != (ElementPair pair1, ElementPair pair2)
    {
        bool result = false;

        if(null == (object)pair1 || null == (object)pair2)
        {
            result = ! object.Equals(pair1, pair2);
        }
        else
        {
            result = ! pair1.Equals(pair2);
        }

        return result;
    }

    public override int GetHashCode()
    {
        return (First + Second).GetHashCode();
    }

    public override string ToString()
    {
        return (First.ToString() + Second.ToString());
    }
}